# Checklist do dev — migração + tracking (o que NÃO é feito por IA)

**Autor:** thread Mídia Paga · **Data:** 2026-07-08 · **Para:** Betiato (dev)
**Contexto completo:** [handoff-landing-pixel-migracao.md](handoff-landing-pixel-migracao.md) · [pixel-capi-spec.md](pixel-capi-spec.md)

Landing nova = **Azure Static Web App** `Aura-Landing-Page` (+ API `aura-api-production`, Postgres `aura-production`). Domínio final = **`aurapoker.com`** (cutover do WordPress). Cobrança nova = **Stripe direto**. Pixel Meta reaproveitado = **`1405949840871947`**.

---

## O que a IA já cobre (pra você não refazer)

- **Agente da landing (IA):** escreve o **código** do tracking na branch nova — pixel browser, CAPI, captura/persistência de UTM, consentimento, e o handler do webhook do Stripe (`Subscribe`). Abre PR.
- **Thread de Mídia Paga (IA, aqui):** docs, criação de públicos, campanhas (pausadas), e validação dos eventos depois.

O que sobra abaixo é **humano** — infra, segredos, decisões e o "apertar o botão".

---

## A. Infra da landing nova (Azure) — dev

- [ ] Configurar **`aurapoker.com` como domínio customizado** na Static Web App `Aura-Landing-Page` (Azure gera o SSL).
- [ ] Confirmar a **rota de sucesso do cadastro** (o `pixel-capi-spec` assume `/signup/success`) — o pixel/CAPI dispara ali. Se for outra URL, avisar.
- [ ] Fazer **deploy da branch/PR** depois de revisado (a IA não faz merge sozinha).

## B. Segredos e credenciais — dev (nunca no código/repo)

- [ ] Pegar o **token da Conversions API** (gerado no Events Manager do BM → configurações do dataset → Conversions API). *Quem gera é o Rafael no BM; você recebe e guarda.*
- [ ] Guardar em **Azure Key Vault / variáveis de ambiente da SWA**: o token da CAPI, a **secret key do Stripe** e a **signing secret do webhook** do Stripe.

## C. Stripe (cobrança direta + webhook) — dev

- [ ] Criar o **endpoint de webhook no Stripe** apontando pra API/Function da landing (eventos `checkout.session.completed` / `invoice.paid`).
- [ ] No webhook: **liberar o acesso** do usuário **e** deixar o handler da IA disparar o `Subscribe` (CAPI).
- [ ] Confirmar que os **3 preços** batem no checkout (USD): $29/mês, $149/6m, $259/ano (produto `AURA Plano Individual`).

## D. Cutover do domínio `aurapoker.com` (WordPress → Azure) — dev

> É o passo mais delicado. Ordem importa.

- [ ] **Backup do WordPress** antes de tudo (o plugin WPvivid já está no site).
- [ ] Repontar o **DNS** de `aurapoker.com` do Hostinger (WordPress) pra Static Web App do Azure.
- [ ] Garantir que o **WordPress não fique servindo** `aurapoker.com` depois do repoint (senão dois sites/pixels no mesmo domínio).

## E. Desligar o rastreamento do WordPress velho — dev

> Pra não ter **evento duplicado** no pixel durante/depois do cutover.

- [ ] Desativar os plugins **PixelYourSite** e **Meta for WooCommerce** no WordPress (ou tirar o WP do domínio de produção).
- [ ] Manter os **dados do WooCommerce** (não apagar) — ele só deixa de receber coisa nova.

## F. Migração dos clientes legados — dev (em paralelo, NÃO trava o launch)

- [ ] Conferir no **dashboard do Stripe** quantas assinaturas legadas **ativas** existem de verdade (a busca via API achou ~1 — provavelmente são poucas).
- [ ] Tentar **adotar as assinaturas que já existem no Stripe** no app novo (casar por customer/email e liberar acesso) — evitar cancelar + re-assinar.
- [ ] ⚠️ **Não** disparar `Subscribe` (pixel) pra esses legados migrados — não são conversão de mídia nova.

## G. Testes antes de ir pro ar — dev

- [ ] Testar o fluxo de cadastro e assinatura em **modo de teste do Stripe** + **Test Events do Meta**.
- [ ] Validar: `PageView`, `CompleteRegistration` (browser+server deduplicado) e `Subscribe` chegando; `_fbp/_fbc` e UTM gravados na conta.

---

## O que é do Rafael (no BM da Meta — não é o dev)

- [ ] **Gerar o token da CAPI** no Events Manager e repassar ao dev (item B).
- [ ] **Aceitar o alerta "confirme o domínio"** no Diagnóstico do dataset (`aurapoker.com`).
- [ ] **Verificar `aurapoker.com`** no BM (Adequação e segurança → Domínios).
- [ ] Itens de higiene da conta de anúncios (2FA, verificação da empresa, etc.) — ver [readiness-dia10.md](readiness-dia10.md). Nada disso trava o dia 10.

## Ordem sugerida

**IA escreve o código →** B (segredos) + C (Stripe webhook) **→** G (testar em modo teste) **→** D (cutover DNS) + E (desligar pixel do WP) **→** Rafael faz a verificação de domínio no BM **→** validar eventos ao vivo.
