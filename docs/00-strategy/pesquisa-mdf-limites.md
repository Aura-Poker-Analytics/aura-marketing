# MDF — o que a copy pode e não pode afirmar (pesquisa verificada)

**Data:** 2026-07-22 · **Método:** deep-research (6 ângulos de busca → 18 fontes → 25 afirmações ×
3 votos de verificação adversarial cada). Fonte dominante: blog do GTO Wizard (referência interna
de convenção — **nunca citar nominalmente em peça**).
**Motivo:** definir qual frase sobre o painel de MDF é defensável, antes de virar padrão de copy.

> Leitura dos veredictos: "refutado" = **a fonte/citação não sustentou aquela redação**, não que a
> proposição seja falsa. Várias proposições refutadas numa fonte aparecem confirmadas em outra.

---

## 1. A identidade aritmética — CONFIRMADA (3-0, múltiplas fontes)

MDF e alpha são complementos exatos, por construção:

```
MDF   = P / (P + B)
alpha = B / (P + B)          alpha = 1 − MDF
```

Onde `alpha` é a frequência de fold em que um blefe de equity zero fica break-even. Logo
**"defende abaixo do MDF" e "folda acima do break-even de blefe" são a mesma frase**, em qualquer
street. Isso é definição, não hipótese.

⚠️ **Qualificador confirmado 3-0:** a identidade só vale **sob a premissa de equity zero**. MDF é
definido como a frequência que deixa as mãos de *equity zero* do vilão indiferentes. Fora dessa
premissa, a equivalência não é exata. **Por isso "blefe puro" não é enfeite — é o que torna a frase
verdadeira.**

## 2. O limite inferior de EV — CONFIRMADO, com escopo estreito

`EV(blefe) = fold% × P − (1 − fold%) × B` é a fórmula da literatura, **derivada assumindo que o
blefe perde a aposta inteira quando pago** — ou seja, o apostador desiste e perde exatamente `B`.

Caveat registrado: a moldura de uma street **não** vale para um plano de blefe multi-street. Quem
pretende continuar apostando no turn/river arrisca mais do que `B`, e aí o limite inferior não vale
mais. **O bound é válido só para um plano "aposta e desiste se pago"** — que é exatamente o que a
palavra *"na hora"* precisa carregar na copy.

## 3. Flop/turn — CONFIRMADO: abaixo do MDF **não** é leak

- A premissa de equity zero **falha no flop e no turn**, porque quase todo candidato a blefe tem
  alguma equity — então o apostador não precisa do fold imediato para lucrar (3-0).
- MDF é caracterizado como **simplificação grosseira** cuja lógica de indiferença só vale para um
  blefe de EV 0, e **não descreve a defesa de equilíbrio antes do river** (3-0).
- Solvers defendem **rotineiramente abaixo do MDF** no flop e no turn, e isso é a estratégia de
  equilíbrio correta, não um erro (2-1).
- No equilíbrio **existem muitas situações em que o vilão deve mesmo ter blefes lucrativos** — logo
  defesa abaixo do MDF, por si só, **não é evidência de leak nem de desvio de equilíbrio** (3-0).

➡️ **"O field overfolda vs MDF, logo tem leak" é falso no flop.** Nosso spot de XR Flop CBet é flop.

## 4. River — as duas metades confirmadas

- No river as mãos estão definidas e não há cartas por vir, então **a objeção "MDF ignora equity
  futuro" não se aplica** (2-1). *(Era a pergunta original do Rafael: sim, ali essa objeção morre.)*
- **Mas a defesa de equilíbrio no river ainda não é igual ao MDF.** Dois casos resolvidos:
  - defensor folda ~41% onde o MDF pediria 40% — desvio atribuído a **blockers/card removal** (3-0);
  - defensor folda **muito mais** que o MDF no equilíbrio, porque **o range do apostador não tem
    candidatos a blefe suficientes** — resultado de composição de range, não leak (3-0).

## 5. Exploitativo ≠ equilíbrio — CONFIRMADO (3-0)

Calcular o EV de uma ação contra uma frequência **medida** é um exercício distinto da análise de
equilíbrio, e **não precisa de solver** — a literatura faz exatamente isso (ex.: break-even de 67%
contra vilão que folda 30% ⇒ o blefe perde dinheiro; conta feita só com a frequência observada).
MDF é descrito como **guia defensivo, não requisito de equilíbrio**.

---

## 6. 🚨 ACHADO NÃO ANTECIPADO — ICM derruba o MDF em MTT

Existe material específico sobre **MDF vs ICM em MTTs**, e ele bate direto no nosso produto:

- **Em spots com ICM o MDF não é o benchmark correto**, ponto: a frequência de defesa de equilíbrio
  se afasta do MDF porque **fichas perdidas valem mais que fichas ganhas** (3-0).
- Solver num toy game de river com ICM mostra o defensor **pagando MENOS** que no equivalente em
  chip-EV, **mesmo com o agressor blefando MAIS** — descrito explicitamente como **contraexemplo a
  ler defesa abaixo do MDF em dados de torneio como leak de overfold** (3-0).

**Por que isso é grave pra nós:** a Aura é 100% MTT. O contexto das nossas telas é "Any Stage" —
inclui bolha e mesa final, onde o ICM morde mais forte. Ou seja, **parte do "overfold" que medimos é
o field jogando certo por causa de ICM**, não errado.

Isso afeta o **badge Overfold do produto**, não só a copy do anúncio.

---

## 7. Veredicto por frase

| Frase | Status |
|---|---|
| "O field defende 57,7% onde o MDF pede 64,5%" | ✅ **Airtight** — medição pura, sem inferência |
| "Board desconexo 9,9% vs conectado 6,9%" | ✅ **Airtight** — compara duas frequências medidas, MDF só como baseline comum |
| "Acima dessa linha, blefe puro nesse size lucra na hora" | 🟡 **Verdadeiro em chip-EV**, mas em MTT com ICM o break-even em $ é mais alto. Só usar sem ressalva em estágio de ICM baixo |
| "O field overfolda vs MDF, logo tem leak / gap explorável" | ❌ **Overclaim** — refutado no flop (§3) e em torneio (§6) |

**Consequência de copy:** liderar por **descrição** e por **comparação relativa** (o V3 já faz isso),
não por inferência de exploit a partir do MDF. A comparação textura-contra-textura é imune a tudo
isso, porque o MDF entra só como linha de referência igual nos dois lados.

## 8. Abertos

1. Dá pra segmentar o badge Overfold por estágio, mostrando-o só onde o ICM é desprezível (early game)?
2. Vale trocar o rótulo "Overfold" por algo descritivo ("defesa vs MDF") no produto?
3. Existe um baseline ICM-aware calculável com o que temos no lake?
