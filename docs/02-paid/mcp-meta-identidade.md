# MCP da Meta + identidade do negócio — o que aconteceu e o caminho limpo

**Autor:** thread Mídia Paga · **Última atualização:** 2026-07-08
**Para:** contexto de sessões futuras. Se for retomar a conexão do MCP oficial da Meta, leia isto antes de tentar qualquer coisa — evita repetir a novela abaixo.

---

## TL;DR

O MCP oficial da Meta (`mcp.facebook.com/ads`) **não conectou à conta certa** e a tentativa de consertar via perfil de Facebook pessoal **acabou com esse perfil desabilitado**. Nada disso afetou o negócio. **Decisão: MCP parado até depois do launch (10/07).** Dados continuam sendo puxados via **Chrome logado** (funciona 100%).

## Linha do tempo (2026-07-08)

1. MCP conectou, mas autorizado como o perfil de Facebook **`61584288455982`**, cuja única conta de anúncios é `1599312301063044` (**vazia**). A conta real **Aura Business `1598770224460932`** retornou `DENY_RULE:EntAdAccountPrivacyPolicy` — esse viewer não tem acesso.
2. Tentamos logar no connector com a **conta certa** (identidade Instagram/Meta que administra o BM) → connector recusou: *"Não é possível se conectar ao ads MCP server com essa conta."*
3. Plano: convidar o perfil de Facebook pessoal pro portfólio e atribuí-lo à conta de anúncios. Ao aceitar o convite em **janela anônima**, o Facebook disparou checkpoint de segurança e depois **desabilitou** o perfil pessoal.

## Causa-raiz (a real)

- O connector autentica por **Facebook Login** e exige um **perfil de Facebook** admin do Business Portfolio.
- O negócio da Aura é **Instagram-first**: o admin do BM é um **login de Instagram** (@aurapokeranalytics), e **não há perfil de Facebook nem Página** no portfólio. Login de Instagram não serve para o Facebook Login do connector.
- Logo: falta um **perfil de Facebook dentro do portfólio**. Sem isso, a API não alcança a Aura Business.

## Fatos que corrigem confusões comuns

- **Instagram-first não é estado quebrado.** Bloqueia só integrações via Facebook Login (o MCP e afins). Postar, impulsionar, insights, conta de anúncios, pixel e Business Suite via Chrome **funcionam normal**.
- **Adicionar um perfil/Página de Facebook NÃO desvincula o Instagram.** Acesso (pessoas) e ativos (IG/Página) são coisas separadas. O IG só sai se for removido explicitamente.
- **Não precisa de e-mail novo** para um Facebook: dá pra criar **só com telefone**.
- **O perfil desabilitado (`61584288455982`) nunca teve acesso ao negócio** — sua queda não impacta BM, IG, conta de anúncios nem pixel.

## Caminho limpo para retomar (pós-launch, sem pressa)

1. Ter um **perfil de Facebook saudável** dedicado ao negócio (recuperar o pessoal via appeal do Facebook, OU criar um novo — só com telefone — num aparelho confiável; **não** logar/hammerar em anônimo nem criar conta nova no mesmo IP logo após uma queda).
2. Como admin (identidade Instagram), **Configurações da empresa → Usuários → Pessoas → Convidar** esse perfil de Facebook com **controle total**.
3. **Aceitar o convite logado NAQUELE perfil** (app do Facebook do celular ou 2º navegador normal — nunca anônimo, nunca a sessão do admin).
4. **Contas de anúncios → Aura Business → Atribuir pessoas** → atribuir o perfil com **Acesso total** (é o passo que vira o DENY em acesso).
5. Criar uma **Página do Facebook "Aura Poker Analytics"** e adicionar ao portfólio (necessária como identidade de anúncio de qualquer forma — gap G2).
6. Reconectar o connector via Facebook Login com esse perfil; selecionar o portfólio **Aura Poker Analytics**.
7. Possível 2º gate: rollout do MCP é **por conta de anúncios**; se a Aura Business vier "não habilitada", é fila da Meta (sem fix self-service) → seguir via Chrome.

## Enquanto o MCP não volta

Puxar públicos/dados/eventos pela navegação no Gerenciador (Chrome logado). Foi assim que o [publicos-diagnostico.md](publicos-diagnostico.md) foi levantado. Regra que não muda: criar/editar público é ok (não gasta); **subir/ativar campanha, não** — tudo pausado, ativação só pelo Rafael.

**IDs de referência:** BM `830069129552748` · Aura Business `1598770224460932` · dataset/pixel `1405949840871947` · IG @aurapokeranalytics `17841468976680108` · perfil FB pessoal (desabilitado) `61584288455982` · conta vazia do MCP `1599312301063044`.
