# Sessões de produto que o plano de marketing pede (22/10/2026)

As duas pendências abaixo saíram da entrevista (fase 0) e ficam fora do repo de marketing. Cada uma é uma sessão própria, aberta pelo Rafael, na pasta indicada. Ordem: a 1 primeiro (alimenta o programa de coaches); a 2 pode correr em paralelo, porque não toca nos mesmos arquivos.

## 1. aura-novofront · campo de Instagram · desenho

**Pasta:** `aura-main` (front em `aura-novofront`, API em `aura_api`) · **Modelo:** Opus esforço médio (tarefa acoplada entre front, API e banco) · **Branch:** `feat/instagram-handle-opcional`, a partir da main de cada repo

Primeira mensagem:

```
Modelo: Opus, esforço médio. Renomeie esta sessão com set_session_title para "aura-novofront · campo de Instagram · desenho".

Tarefa: adicionar um campo opcional "Seu Instagram" à conta do usuário da Aura, para o marketing mapear contas com muitos seguidores e convidar parceiros (decisão do Rafael de 22/10, plano de marketing em aura-main/_wt-mkt-plano/docs/00-strategy/entendimento-compartilhado-2026-11.md, Q23 e Q24).

Regras de desenho já decididas:
- O campo NÃO entra no formulário de cadastro (dois terços já desistem nele). Entra depois: no onboarding e em Minha Conta.
- Rótulo PT "Seu Instagram (opcional)", ajuda "Para conectarmos você com coaches e a comunidade". EN "Your Instagram (optional)", "So we can connect you with coaches and the community".
- Aceitar @usuario ou URL, gravar só o usuário normalizado (sem @, minúsculas), validar o formato do Instagram.

Escopo: aura-novofront (tela e i18n PT/EN, teste), aura_api (endpoint de perfil lê e grava o campo, teste), aura-database (migration aditiva, coluna nullable em tbl_user do AuraBusiness).

Branch feat/instagram-handle-opcional em cada repo, a partir da main. Worktree próprio, nunca junção de node_modules.

Limites: a migration no AuraBusiness de produção é do Rafael; você só escreve e testa num banco descartável. Nenhum deploy. O merge do front publica, então PR em rascunho.

Pronto quando: três PRs abertos (db, api, front) com gates verdes, prints PT e EN, e mensagem à HUB com os links e os números dos testes. Atualize o STATE.md do aura-main.
```

## 2. aura · aposentar o Team Mode · inventário

**Pasta:** `aura-main` (landing em `aura-landing`, app em `aura-novofront`) · **Modelo:** Sonnet esforço baixo para o inventário; a decisão do que sai é do Rafael · **Branch:** nenhuma no inventário

Primeira mensagem:

```
Modelo: Sonnet, esforço baixo. Renomeie esta sessão com set_session_title para "aura · aposentar o Team Mode · inventário".

Contexto: em 22/10 o Rafael decidiu aposentar o Team Mode como ferramenta (o time sobe os próprios dados). O B2B passa a ser pacote de contas Individual por volume, relatório do field por encomenda e programa de coaches (plano de marketing em aura-main/_wt-mkt-plano/docs/00-strategy/entendimento-compartilhado-2026-11.md, Q9 e Q18).

Tarefa, só leitura: listar tudo que menciona ou serve o Team Mode, com arquivo e linha:
- aura-landing: card de planos, FAQ, textos PT/EN, rotas.
- aura-novofront: telas, rotas, i18n, flags, menus.
- aura_api: endpoints e configuração do modo time (catálogo exclusivo do time).
- aura-context e STATE.md do aura-main (§1 lista o Team Mode em produção).
- Clientes ativos no Team Mode hoje (contagem agregada, sem dado pessoal; se exigir AuraBusiness, só leitura).

Para cada item, proponha: remover, esconder por flag ou trocar o texto (o card da landing vira "Times e coaches: fale conosco" para o pacote por volume). Não altere nada.

Pronto quando: o inventário estiver em aura-context/docs/08-planning/team-mode-aposentadoria/00-inventario.md, commitado numa branch docs/team-mode-inventario, e a mensagem à HUB trouxer a contagem de itens por repo e se há cliente ativo no modo time.
```

## 3. aura · Field Exploits · um card por spot, stacks dentro

Pedido do Rafael (23/10): "o field exploits tem spots exatamente iguais em que só alteram os stacksizes, eles tem que fazer parte do mesmo card.. e o detalhamento por stack depois de selecionar o card."

**Pasta:** `aura-main` (front em `aura-novofront`, API em `aura_api`, calendário em `aura-database/scripts/pool_vs_gto/exploit/`) · **Modelo:** Opus esforço médio (decisão de agrupamento entre banco, API e front) · **Branch:** `feat/field-exploits-card-por-spot`, a partir da main de cada repo

Primeira mensagem:

```
Modelo: Opus, esforço médio. Renomeie esta sessão com set_session_title para "aura · Field Exploits card por spot · desenho".

Pedido do Rafael, 23/10: no Field Exploits, spots iguais que só mudam o stack (mesmo par, mesmo pote, mesma classe de flop, mesma ação e tamanho) têm de virar um card só. O detalhe por stack aparece depois de selecionar o card.

Antes de codar, meça e proponha:
1. Na janela atual (tbl_pool_vs_gto_release × tbl_pool_vs_gto_rank, Azure aura_database, só leitura), quais dos 8 spots são o mesmo spot em stacks diferentes, e quantos cards sobram.
2. A regra de janela (release_rule.py: WINDOW = 8, PER_WEEK = 2, um spot por célula par × stack) passa a contar card ou spot? O Grátis (1 spot) vê o card inteiro ou só um stack?
3. O desenho do card agrupado e do detalhe por stack, em PT e EN, com print.

Mande a proposta à HUB antes de implementar. Depois: PRs em rascunho nos repos que mudarem, gates verdes, nada publicado (o merge do front publica).

Atenção ao marketing: os e-mails da reconquista (aura-marketing, content/email/reconquista-2026-11/) dizem "8 spots" e "toda segunda entram 2 novos". Se a contagem mudar, avise a sessão do plano de marketing antes de 26/10.

Pronto quando: proposta aprovada pela HUB, PRs abertos com prints, STATE.md do aura-main atualizado e reporte à HUB com os links.
```
