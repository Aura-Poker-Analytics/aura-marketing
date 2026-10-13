# Field Ranges: números verificados para o lançamento (06/10)

Fonte de todos os números: folhas v3 do Field Ranges no Postgres LOCAL. São as tabelas `observed_ranges_staging.pop_pf_leaf_v3` e `obs_pf_leaf_v3`, da passada completa de 06/10. É o mesmo dado que vai para a Azure no promote, com conferência 964.372 / 183.142.522 e 30.806 / 2.073.190.849.

O recorte do módulo é stack efetivo de 20bb para cima, todos os buy-ins, pote sem caller antes do agressor.

## 1. Tamanho da base
- **1,42 bilhão de decisões pré-flop** no recorte do módulo: 1.423.474.657. A base inteira tem 2.073.190.849.
- **96,4 milhões de mãos com cartas conhecidas** no recorte: 96.394.883. A base inteira tem 183.142.522.

Consulta: `sum(n)` de `pop_pf_leaf_v3` e de `obs_pf_leaf_v3` com `stack_pf in (4,5,6) and not multiway`.

## 2. Cobertura da trilha
- **90 situações** da trilha da mão, todas com amostra para a grade (≥ 2.000 mãos com cartas cada).
  - 5 opens (EP, MP, CO, BTN, SB);
  - 17 respostas ao open;
  - 17 de quem abriu contra 3-bet, mais 17 contra 3-bet all-in;
  - 17 de quem deu 3-bet contra 4-bet, mais 17 contra 4-bet all-in.
- Contagem: nós (árvore, posição, quem agiu antes, all-in antes) que a tela alcança, pela regra de quem pode responder a quem, com `sum(n) >= 2000` em `obs_pf_leaf_v3`.

## 3. Desvio marcante: o field larga contra 3-bet
Quanto o field folda depois de abrir e levar 3-bet, contando só o 3-bet não all-in:
- **BTN: 56,9 %** (4.244.321 decisões);
- SB: 51,1 %;
- CO: 49,8 %;
- MP: 43,0 %;
- EP: 39,0 % (8.493.861 decisões).

O botão, que abre o range mais largo, é quem mais desiste contra 3-bet.

Consulta: `pop_pf_leaf_v3`, `tree='facing_3bet'`, sem all-in antes, `action='fold'` sobre o total do nó.

## 4. Uma mão: AA do BB contra o open do CO
- **13 % das vezes o field só paga com AA** em vez de dar 3-bet. 84 % dão 3-bet não all-in e 3 % vão all-in.
- Base, mãos com cartas conhecidas: 20.425 3-bets não all-in, 1.484 all-in e 3.351 calls (`obs_pf_leaf_v3`, `facing_rfi`, BB vs CO, AA, 20bb+).
- O percentual é o da tela: a estimativa calibrada do `/api/field-ranges/strategy` (aura-api#51) sobre as folhas completas.

## Cuidados para o texto
- É **estimativa do field**: a frequência total de cada ação vem de todas as mãos; a divisão por mão vem das mãos que foram ao showdown. Não chamar de "range exato".
- "Decisões" ≠ "mãos": uma mão gera várias decisões (abrir, responder, reagir ao 3-bet).
- O lake está congelado desde 20/08. Não dizer "dados de hoje".
