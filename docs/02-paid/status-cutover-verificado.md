# Status do Cutover — Verificado AO VIVO (2026-07-08, tarde)

**Método:** navegação real em `aurapoker.com` (Chrome) + Events Manager do dataset `1405949840871947` (Chrome) + WebFetch direto no `fbevents.js`. Não assumido — checado.

---

## 1. DNS cutover — ✅ CONFIRMADO

`https://aurapoker.com` já serve a **landing nova** (tema escuro, brand kit 2.0, "Field Intelligence for MTT", CTA "Start for free"). WordPress **não é mais servido nesse domínio**.

## 2. Pixel na landing — ✅ FUNCIONANDO

- `fbq('init', '1405949840871947')` + `fbq('track','PageView')` disparando. `window.fbq.loaded === true`, versão 2.0.
- **Pixel ID correto** — o mesmo dataset que já usávamos.
- ⚠️ Ruído: a extensão do Chrome reporta **503** pro `fbevents.js` no log de rede — é **falso positivo** (confirmado via WebFetch direto: arquivo carrega normal, 372KB, válido). Provável ad/tracking-blocker da extensão interceptando o request. Não é problema real de produção.

## 3. Pixel já chegando de MAIS lugares do que eu sabia — 🎉 boa notícia

O dataset `1405949840871947` está instalado em **5 sites** (últimos 28 dias):

| Domínio | Eventos (28d) | Leitura |
|---|---|---|
| `aurapoker.com` | 130 | landing (WP até ontem + Azure hoje) |
| `localhost` | 12 | dev, inofensivo |
| **`www.aura.poker`** | 11 | **o APP já está com pixel disparando** |
| **`beta.aura.poker`** | 4 | beta antigo, também instrumentado |
| `invalid.invalid` | 3 | ruído conhecido da Meta, ignorar |

Ou seja: a instrumentação do app (`aura.poker`) **já existe e já está no ar**, pelo menos em parte — provavelmente da instrumentação local que você mencionou ter pronta. **Não confirmei quais eventos** (só PageView? já tem CompleteRegistration?) — próximo passo de verificação, não assumir.

## 4. WooCommerce — evidência de que já não recebe tráfego novo

`Iniciar finalização da compra` (InitiateCheckout) e `Adicionar ao carrinho` (AddToCart) — **últimos eventos há 1 dia**, ou seja, **antes** do cutover de hoje. Consistente com: WordPress parou de receber visita real assim que o DNS mudou.

## 5. Pergunta "posso desativar o pixel do WordPress?" — ✅ SIM, seguro

Motivos:
- DNS já migrado e confirmado ao vivo — `aurapoker.com` não é mais WordPress pra ninguém que resolva o domínio hoje.
- Os eventos de checkout (WooCommerce/PixelYourSite/Meta-for-WooCommerce) já pararam há 1 dia — não há sinal de tráfego real ainda batendo lá.
- Desativar **agora** só reduz risco (elimina qualquer chance residual de disparo duplicado durante a cauda de propagação de DNS que alguns resolvers/ISPs possam ainda ter em cache).

**Ressalva:** o **WordPress MCP está desconectado nesta sessão** — não consegui entrar no wp-admin pra clicar em "desativar" ou confirmar o estado atual dos plugins. A ação de desativar **PixelYourSite** e **Meta for WooCommerce** no WP precisa ser feita manualmente (ou reconectar o MCP).

## 6. Gaps que restam (não bloqueiam nada, mas ficam registrados)

- ⚠️ **CTA "Start for free" NÃO propaga UTM/fbclid.** Aponta pra `https://aura.poker/Login?tab=signup` sem nenhum query param. É o elo cross-domain que faz a atribuição sobreviver — ver [definicao-pronto-tracking.md](definicao-pronto-tracking.md) §1. Ainda não implementado.
- ⏳ **Diagnóstico do dataset:** ainda mostra o alerta pendente "confirme o domínio" pra `aurapoker.com` — ação do Rafael no BM (não fiz essa ação, é clique de permissão).
- ❓ Não confirmado quais eventos exatos disparam em `www.aura.poker`/`beta.aura.poker` — verificar se já inclui `CompleteRegistration` com `eventID`.
