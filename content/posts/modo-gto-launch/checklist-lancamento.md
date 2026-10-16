# Checklist de lançamento do Modo GTO (16/10)

Pacote: `content/posts/modo-gto-launch/` · PR [aura-marketing#4](https://github.com/Aura-Poker-Analytics/aura-marketing/pull/4) (head `17e4d24`, MERGEABLE) · Nada foi postado, enviado nem criado no Resend.
Legenda: ✅ feito e conferido hoje · ⏳ falta · 👤 só o Rafael.

## O que já está feito (conferido hoje, sem o Rafael)

| Item | Estado | Como conferi |
| --- | --- | --- |
| aura-api#84 (turn/river de co_btn, utg_bb@25 e outros) | ✅ mesclado 14/10 20:47Z | `gh pr view` |
| aura-api#91 (amostra do GTO na conta Grátis) | ✅ mesclado 15/10 19:56Z · deploy não conferido (gate 2) | `gh pr view` |
| Landing, "incluso no Individual por tempo limitado" (aura-landing#24) | ✅ mesclado 15/10 20:13Z, SWA success; o bundle público `index-C_lG8rrP.js` já traz "incluso no plano Individual" e "por tempo limitado" (PT e EN) | `gh run list` + leitura do bundle público |
| Imagens do e-mail do PR #17 = imagens do pacote | ✅ SHA igual nas duas (`modo-gto-pt.png`, `modo-gto-en.png`) | `git show` do branch × arquivo do pacote |
| E-mail HTML | ✅ `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé PT e EN; CTA para `www.aurapoker.com` com UTM; logo `www.aura.poker/email/aura-logo.png` responde 200 | leitura do HTML + `curl -I` |
| Cobertura na legenda do carrossel | ✅ "more than 2,100 flop spots … Updated October 15" (2.172 spots, 28 situações, snapshot 20261015; revisão de marca feita) | `numeros-verificados.md`, seção "Cobertura de spots de flop" |
| Resend, só leitura | ✅ não existe rascunho do Modo GTO; os 8 broadcasts são `sent`; segmentos: **General** (base completa, usado no Field Trends de 08/10), "Field Ranges — não receberam (192)", "Board Selection leads (174)" | `list-broadcasts`, `list-segments` |
| Preço no código da landing | ✅ PT R$ 150 / 745 / 1.295, EN US$ 29 / 149 / 259 (`src/content/pricing.ts`) | leitura da `main` |

## Gates, um por linha

| # | O que é | Quem | Estado de hoje | Passo exato |
| --- | --- | --- | --- | --- |
| 1 | **P-61: o Modo GTO aberto ao plano Individual.** Sem isso, o post promete algo que o assinante de R$ 150 não vê. | HUB confere a config; Rafael vê na tela | ⏳ código mesclado (aura-api#63, `GtoOverlay:OpenToTiers`); o valor em produção não foi conferido | HUB: ver só a chave `GtoOverlay__OpenToTiers` do App Service (deve conter `individual`; não listar o resto). Rafael: ver o gate 4 com conta Individual. |
| 2 | **API em produção com #84 e #91.** O número de turn/river e a amostra do Grátis dependem desses dois. | HUB | ⏳ mesclados; deploy não conferido | HUB: comparar o commit/dll em produção com a `main` do aura-api e dizer se #84 e #91 estão dentro. |
| 3 | **Preço Stripe: Individual US$ 29 / R$ 150 por mês.** É o preço normal do plano, não promoção. | 👤 Rafael | ⏳ o código da landing bate; o Stripe live não é lido por esta sessão | Stripe (live) → Produtos → Individual → mensal: conferir USD 29 e BRL 150. Opcional: abrir o checkout do Individual em PT e em EN e ver o mesmo valor, sem pagar. |
| 4 | **Teste logado do Rafael (3 contas).** Os números das peças precisam bater com a tela. | 👤 Rafael | ⏳ | **Conta paga** em www.aura.poker: (a) Postflop, SRP, RFI CO × caller BB, 30,1–60bb, Regular, flop K-high two-tone sem par desconectado, reação do BB ao c-bet de 33 %: field **46,0 %**, GTO **38,8 %**, faixa **37,1–40,4 %**; (b) Preflop, Regular, 30–50bb, RFI do CO: **31,6 %** × **37,0 %**; (c) Turn Delayed CBet 51,7 / 44,1 (37,8–50,3) e Second Barrel 54,2 / 57,2 (50,8–63,5), mesmo recorte largo do arquivo de 14/10. Field Ranges → Field vs GTO: roteiro `_ops/golive-p53-2026-10-15/roteiro-conferencia-rafael.md` (SB RFI 50bb+: **132** raise · **148** limp · **74** fold). Se um número não bater, a peça com ele sai ou é refeita. |
| 5 | **Amostra do GTO na conta Grátis.** A frase "A conta grátis inclui uma amostra do GTO" entra em feed, legenda, Discord, landing e e-mail. | 👤 Rafael | ⏳ aura-api#91 mesclado: um spot do flop, só a reação ao c-bet (BTN × BB SRP, 30,1–60bb) | **Conta Grátis**: Postflop, BTN × BB, SRP, 30,1–60bb, reação ao c-bet com número GTO visível; trocar para outro spot e ver o cadeado. Se não confirmar, a frase sai de todas as peças (o checklist de arquivos está na Pendência 11 do `copy.md`). |
| 6 | **Hospedar as imagens do e-mail (aura-landing#17).** Sem isso o e-mail sai com imagem quebrada. | HUB valida; 👤 Rafael mescla (publica) | ⏳ PR aberto, MERGEABLE, imagens idênticas às do pacote; hoje `www.aurapoker.com/email/modo-gto-pt.png` e `-en.png` dão 404 | HUB: `/validar-pr` do #17 (ou via rápida, só arquivos estáticos). Rafael: mesclar. Depois a HUB ou esta sessão roda `curl -I` nas duas URLs e espera 200 `image/png`. |
| 7 | **Rascunho do e-mail no Resend (só rascunho, nunca enviar).** | HUB, ou esta sessão com o "pode criar" do Rafael | ⏳ não existe; **não criei**: a instrução original do pacote proíbe criar no Resend sem ele, e a imagem ainda dá 404 | Só depois do gate 6 (imagem em 200): `create-broadcast` com `email-pt.html`, assunto "O GTO no flop, turn e river, ao lado do field", remetente `news@news.aurapoker.com`, status rascunho. EN: ver gate 8. Nunca `send-broadcast`; o envio é do Rafael. |
| 8 | **Segmento e descadastros.** Define quem recebe e garante que quem saiu não volta. | 👤 Rafael decide; HUB prepara | ⏳ General (base completa) foi o segmento dos lançamentos de 08/10; **não existe segmento EN** | Decidir: (a) PT para General inteiro ou excluindo quem já é pago; (b) quem recebe a versão EN (hoje não há lista EN; sem lista, a EN fica só no Discord e no Instagram). Descadastro: o broadcast do Resend já respeita quem se descadastrou e o HTML tem o link; conferir no teste do rascunho (enviar o teste só para o próprio Rafael, pelo painel do Resend). |
| 9 | **Landing no modo de lançamento.** A home precisa dizer que o GTO está no ar, não "em breve". | HUB (sessão aura-landing) | ⏳ a frase do plano já está no ar; a chave `VITE_LAUNCH_MODO_GTO=1` no build do SWA não foi confirmada, e o bundle público ainda tem 2 "em breve" | Conferir a chave no workflow/segredos do SWA (só o nome e o valor `1`) e abrir a home em PT e EN depois. Checklist em `aura-landing/docs/lancamento-modo-gto.md`. |
| 10 | **Data de fim (interna) do "por tempo limitado".** Urgência sem data pode ser questionada (CONAR/CDC). | 👤 Rafael | ⏳ as peças dizem "por tempo limitado", sem data (decisão dele de 15/10) | Decidir se há uma data a honrar, mesmo sem divulgar. Se houver, anotar no `copy.md`; se divulgar, vai em todas as peças ao mesmo tempo. |
| 11 | **Oferta em dólar para o público BR (CDC art. 31).** As peças PT usam R$ e as EN usam US$, sem misturar. | HUB decide | ⏳ | HUB confirma que o carrossel (EN, em US$) não vai a audiência BR, ou aprova. |
| 12 | **Linha de fonte do preço no `numeros-verificados`.** As peças citam US$ 29 / R$ 150. | HUB | ⏳ (Pendência 10) | HUB põe a linha "Individual US$ 29 / R$ 150 mensal" com a origem (`pricing.ts` + Stripe). |
| 13 | **Data da cobertura no dia de postar.** A legenda diz "Updated October 15". | HUB confere no dia | ✅ hoje; muda a cada snapshot novo | No dia: ver o `ReferenceSnapshot` servido; se for outro, trocar a data na legenda (`copy.md`, "Proposta de 16/10"). |
| 14 | **Merge do PR #4 (aura-marketing).** | HUB (nada publica) | ⏳ revisão de marca feita; sem o merge o Rafael não tem os arquivos na `main` | HUB confere o diff e mescla, ou o Rafael pede. |

## Ordem sugerida

1. HUB: gates 1, 2, 9, 12 e 14 (sem o Rafael).
2. Rafael: gates 3, 4 e 5 (uma sessão de uns 15 min, três contas).
3. Rafael: gate 6 (mescla do #17) → esta sessão confere o 200 → HUB cria o rascunho (gate 7).
4. Rafael: decide gates 8, 10 e 11.
5. Postar, nesta ordem: Discord → Instagram (carrossel, feed, story) → e-mail (enviar do painel, depois do teste a si mesmo). A landing já mostra o plano; o e-mail e o post só saem com os gates 1 a 6 verdes.

## O que sobra para o Rafael

- **Gate 3:** conferir US$ 29 / R$ 150 no Stripe live.
- **Gates 4 e 5:** logar com conta paga e conta Grátis e conferir os números e a amostra.
- **Gate 6:** mesclar o aura-landing#17 (publica as imagens).
- **Gates 8, 10 e 11:** escolher o segmento (e se há lista EN), decidir a data interna do "tempo limitado" e (com a HUB) a oferta em dólar.
- **Postar e enviar:** Discord, Instagram e o envio do e-mail.
