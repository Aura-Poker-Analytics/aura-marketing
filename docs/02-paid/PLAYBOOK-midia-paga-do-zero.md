# PLAYBOOK — Mídia paga do zero: instrumentar, descobrir, converter

**Destinatário:** agente de IA replicando esta metodologia em outra empresa.
**Origem:** derivado de uma implementação real (SaaS B2C de nicho, mercado BR, orçamento inicial ~R$1.500/mês, conta de anúncios sem histórico utilizável).
**O que transfere:** o método, a ordem das fases, os critérios de decisão e as armadilhas. **O que NÃO transfere:** números, interesses e verticais — são exemplos, não parâmetros.

> ⚠️ **Leia o "porquê" de cada decisão, não só o "o quê".** Copiar a receita sem o raciocínio produz erro quando o contexto diverge — e ele vai divergir.

---

## 0. Princípio organizador

**Gastar mídia sem medição é comprar um resultado que você não consegue ler.** A ordem correta é sempre:

```
instrumentar → descobrir quem responde → converter quem responde → escalar
```

Pular etapa é a causa mais comum de queimar verba. A tentação universal é começar em "converter" — e ela falha quando não existe público conhecido nem baseline.

---

## 1. FASE 0 — Auditoria antes de qualquer gasto (custo zero)

Antes de propor campanha, levante o estado real. Nunca assuma; verifique.

### 1.1 Inventário de ativos
| Verificar | Por que importa |
|---|---|
| Conta de anúncios: existe? tem histórico? moeda? | Conta nova tem limite de gasto e menos confiança do algoritmo |
| Pixel/dataset: existe? recebe eventos? de quais domínios? | Pixel em domínio errado = medição cega |
| Públicos salvos: tamanho e origem | Público pequeno demais não sustenta campanha |
| Campanhas antigas: **status real** | 🔴 Campanha antiga "pausada só por falta de saldo" volta a rodar quando entra dinheiro |
| Identidade (página/perfil) vinculada à conta | Sem identidade, não se cria anúncio |
| Verificação da empresa, 2FA, contato de recuperação | Reduz risco de bloqueio — que interrompe campanha no meio |

### 1.2 Auditoria de campanhas históricas (se houver)
Se existe histórico, **audite antes de repetir**. Procure, em ordem:

1. **Qual era o `optimization_goal`?** — é a causa nº 1 de público errado. Ver §8.1.
2. **Qual era o CTA/destino?** — CTA para perfil social ≠ CTA para site.
3. **Como o público foi construído?** — lookalike sobre semente contaminada propaga o ruído.
4. **Breakdowns de entrega** (idade/gênero/região/posicionamento) — comparar com o perfil real do cliente. Divergência grande = sinal de público errado.

> **Técnica útil:** procure uma variável demográfica que separe cliente real de não-cliente (no caso original, `% masculino`, porque o nicho era ~95% masculino). Ela vira **termômetro precoce** — aparece em 48h, muito antes do custo por conversão estabilizar.

### 1.3 Inteligência competitiva
Varra a biblioteca de anúncios da plataforma pelos concorrentes. Extraia:
- Quem anuncia ativamente, em quais mercados, há quanto tempo
- **Padrões de mensagem** (vendem por feature? resultado? medo? autoridade?)
- **Ângulos desocupados** — o que ninguém está dizendo

O ângulo vago costuma ser a maior oportunidade, e é gratuito de descobrir.

---

## 2. FASE 1 — Instrumentação (pré-requisito absoluto)

Sem isso, não gaste. A arquitetura mínima:

### 2.1 As camadas
```
Anúncio (UTM na URL)
   ↓
Landing (pixel browser + captura first-touch de utm/click-id)
   ↓
App/produto (propaga utm no handoff cross-domain)
   ↓
Backend (persiste utm no registro do usuário + dispara evento server-side)
   ↓
Banco próprio ← FONTE DE VERDADE
```

### 2.2 Por que o banco próprio é a fonte de verdade
Pixel e analytics de terceiro sofrem com bloqueio de rastreamento, consentimento e limites de plataforma. **O registro no seu banco não sofre.** Se você conseguir gravar `utm_source/medium/campaign/content` na conta do usuário no momento do cadastro, você tem atribuição imune a tudo isso.

**Essa é a maior vantagem competitiva de medição que existe, e quase ninguém monta.**

### 2.3 Checklist de instrumentação
- [ ] Evento de conversão disparando **browser + server-side**, com `event_id` compartilhado para deduplicação
- [ ] UTM capturado em **first-touch** (não sobrescrever em navegação subsequente)
- [ ] UTM sobrevive ao **handoff cross-domain** (landing → app), se houver
- [ ] UTM **persistido no banco** no momento do cadastro
- [ ] Click-id da plataforma (`fbclid`/`gclid`) capturado e convertido no formato do cookie
- [ ] **Validado com um cadastro real ponta a ponta** — código deployado não é código funcionando

### 2.4 🔴 Armadilha crítica: redirect que come UTM
**Verifique com `curl` se redirects preservam a query string.**

Caso real: o apex do domínio redirecionava para `www` com `301` e `Location` sem path nem query. Todo UTM morria antes da landing carregar. Sintomas: 100% do tráfego como "direct", campos de UTM nulos no banco, campanha invisível no analytics.

```bash
curl -sSI "https://dominio.com/?utm_source=teste" | grep -i location
# Se o Location vier sem "?utm_source=teste", está quebrado.
```

Corolário: **todo link com UTM deve usar exatamente o hostname canônico** (com ou sem `www`, conforme o que serve o site sem redirect).

### 2.5 Consentimento (LGPD/GDPR) — decisão de negócio, não técnica
Gate de opt-in bloqueante (nada dispara até "Aceitar") produz **subcontagem severa** — quem ignora o banner gera zero telemetria, nem sessão anônima. Em navegador in-app de rede social, isso tende a zerar.

Alternativa: **opt-out com Consent Mode**, sinais declarados como `granted` por padrão e revogação ativa no "Recusar". Sob LGPD é defensável (analytics por legítimo interesse, com aviso e opt-out funcional); sob GDPR, não presuma — verifique.

> Observação que resolve o dilema: **a atribuição de primeira parte (UTM → banco) normalmente não depende de consentimento de marketing** — só as tags de terceiro dependem. Ou seja, mesmo com gate restritivo, a medição que importa sobrevive.

---

## 3. FASE 2 — Campanha de DESCOBERTA (não de conversão)

### 3.1 Quando usar
Quando **não se sabe quem é o comprador**. Sinais: sem histórico utilizável, público salvo pequeno (<1.000), nenhum criativo validado.

**Não otimize por conversão nessa fase.** Com poucas conversões, o algoritmo estreita a entrega num bolso minúsculo e mata a amplitude de que a descoberta depende.

### 3.2 O desenho experimental
**N células = N hipóteses de persona/ângulo.** Não N variações do mesmo argumento — isso ensina CTR agregado, não *quem*.

Regra de ouro: **muda UMA variável por vez.**

| Experimento | Variável | Constante | Responde |
|---|---|---|---|
| Descoberta (primeiro) | **criativo** (N ganchos) | público, geo, idade, orçamento, otimização | qual **mensagem** ressoa |
| Targeting (depois) | **público** | criativo (o vencedor) | qual **audiência** responde |

Fazer os dois juntos produz resultado sem interpretação — se a célula 2 vencer, não se sabe se foi o gancho ou o público.

### 3.3 Como desenhar as células
Cada célula deve mirar uma população **identificável e mutuamente distinta**. Heurística que funciona: **segmente por ferramenta/comportamento que a pessoa já tem**, não por demografia.

Exemplo real (SaaS de análise para um nicho técnico):
| Célula | Persona | Gancho (estrutura) |
|---|---|---|
| 1 | quem já usa a ferramenta teórica do nicho | *"Você domina [a teoria]. Seu [contexto real] não segue."* |
| 2 | quem busca vantagem prática | *"[Métrica teórica] diz X. [Realidade medida] é Y."* |
| 3 | **controle** — sem contexto prévio | *"Não é [categoria A]. Não é [categoria B]. É [nova categoria]."* |
| 4 | testa **posicionamento**, não persona | *"Isso não existia."* + nome da categoria |

**Inclua sempre uma célula de controle** (a mais ampla, sem pressupor conhecimento prévio). Se ela vencer, o conceito vende sozinho; se perder, o comprador é quem já tem contexto. Essa comparação vale para o posicionamento da marca inteira, não só para o anúncio.

### 3.4 O primeiro frame é o instrumento
Em vídeo curto, o primeiro frame decide se a pessoa para ou rola. **Em campanha de descoberta ele não é enfeite — é a abertura do instrumento de medição.**

- Frame vago e bonito → coleta ruído demográfico, resultado ilegível
- Frame que **nomeia conceito + persona** → a população que engaja fica legível

**Jargão técnico filtra melhor que segmentação.** Quem não é do nicho não decodifica e passa direto. Num caso real, o criativo com jargão denso teve **12,85% de CTR** contra ~2% do criativo institucional genérico.

> Isso vira **infraestrutura** quando a plataforma remove exclusões de interesse (§7.3): o criativo passa a ser a única defesa contra público errado. Suavizar a linguagem para "vender melhor" destrói o filtro.

### 3.5 Estrutura de campanha
```
1 campanha
├── Célula 1 (orçamento próprio)  ← ABO, não CBO
├── Célula 2 (orçamento próprio)
├── Célula 3 (orçamento próprio)
└── Célula 4 (orçamento próprio)
```

🔴 **Nunca use orçamento de campanha (CBO) em descoberta.** O algoritmo concentra 70–90% das impressões no "vencedor" em 24–72h e as outras células ficam sem amostra. Excelente para conversão, **fatal para descoberta** — você queria o perfil de cada célula e recebe o de uma.

**Teste A/B formal é opcional.** Ele adiciona audiência mutuamente exclusiva. Com frequência baixa (~1,0–1,5) e público grande, a sobreposição é desprezível — N conjuntos com orçamento igual já resolvem o essencial.

### 3.6 Segmentação em nicho pequeno
Distinção que evita dois erros opostos:

| Segmentar por… | Enviesa a descoberta? |
|---|---|
| **Persona** (ex.: só quem usa a ferramenta X) | ❌ **Sim** — pré-decide a resposta que a campanha deveria dar |
| **Pertencimento ao nicho** (ex.: interessados na categoria) | ✅ **Não** — só garante que a pergunta chega à população certa |

Se o nicho é ~0,5% da população, targeting amplo puro gasta a maior parte do orçamento redescobrindo que a maioria não é do nicho. **Filtre por nicho; deixe o criativo filtrar persona.**

⚠️ **Evite o termo genérico da categoria.** Taxonomias de interesse agregam adjacências indesejadas (no caso real, o interesse genérico do nicho incluía uma vertical correlata mas irrelevante, e foi a causa de anos de público errado). **Prefira marcas, produtos e mídia especializada** — mais específicos e menos contaminados.

**Melhor sinal encontrado:** interesse com **intenção** (ex.: "[nicho] strategy" — quem estuda) supera interesse com **afinidade** (ex.: marca do setor — quem só consome).

### 3.7 Orçamento e leitura
- **Concentre geografia.** Geo não é a variável em descoberta — cortar países caros multiplica impressões por real sem enviesar nada. Num caso real, concentrar num só mercado deu ~5× mais impressões pelo mesmo orçamento.
- **Não estreite a demografia que você quer descobrir.** Se quer saber qual faixa etária converte, não trave idade.
- **Aceite leitura direcional.** Orçamento pequeno não produz significância estatística. O objetivo é apontar direção, não provar.

---

## 4. Gates durante a campanha — de SAÚDE, não de performance

**O risco a proteger não é "gastar numa campanha ruim" — é gastar e terminar com dado ilegível.**

### ❌ Proibido em campanha de descoberta
- **Matar célula por métrica baixa.** Métrica baixa **é achado** ("este gancho não faz ninguém parar"), e matar apaga o perfil daquela célula.
- **Realocar verba para o vencedor** — é otimização, o oposto de descoberta.
- **Decidir com resultado parcial** — *peeking* infla falso-positivo e invalida a comparação.

### ✅ Os gates
| Momento | Checar | Ação se vermelho |
|---|---|---|
| **D3** | Todos os anúncios aprovados? Cada célula gastando? CPM na faixa? Frequência baixa? Variável-termômetro dentro do esperado? | corrigir **entrega**, nunca pausar por performance |
| **D7** | No ritmo atual, cada célula chega ao fim com amostra? | distinguir *"teve impressão e não engajou"* (= achado) de *"não teve impressão"* (= problema) |
| **~50% do orçamento** | Único ponto de abort — **só por qualidade de dado** | CPM muito acima do estimado ou célula que nunca entregou → parar e redesenhar escopo |

### 🔴 Todas as células devem largar juntas
Se metade começa hoje e metade em dois dias, a diferença entre elas passa a incluir *o dia em que rodaram* — leilão, concorrência e disponibilidade de público diferentes. **O tempo vira variável escondida e a comparação morre.**

Se um anúncio ficar em análise da plataforma, **pause os que já estão rodando** e comece todos juntos.

---

## 5. Leitura dos resultados

### 5.1 O que medir
| Camada | Fonte | Confiabilidade |
|---|---|---|
| Alcance/impressão por célula | plataforma | alta |
| **Perfil demográfico por célula** | breakdowns da plataforma | alta ← **o entregável real** |
| Cliques por célula | plataforma | alta |
| **Visitas e conversões por célula** | **banco próprio via UTM** | **máxima** |

### 5.2 A pergunta que a campanha responde
Não é *"qual anúncio teve mais cliques"*. É **"qual enquadramento atrai qual perfil, e a que custo"**.

Saída esperada: *"a célula 2 gerou N conversões a R$X cada, concentradas na faixa etária A e região B; a célula 3 gerou M a R$Y, com perfil C."* Isso vira insumo de segmentação, criativo e posicionamento.

### 5.3 O que a campanha constrói (além do aprendizado)
- **Semente limpa para lookalike** — e aqui está a lição mais cara: use como semente **quem executou uma ação** (viu vídeo, visitou site, converteu), **nunca seguidores**. Semente passiva contamina fácil, e lookalike herda o ruído permanentemente.
- Pool de retargeting para a fase de conversão
- Interesses e criativos validados

---

## 6. FASE 3 — Conversão (só depois)

Gatilho: volume de conversões suficiente para o algoritmo aprender (referência da indústria: ~50 eventos/semana por conjunto).

Mudanças em relação à descoberta:
- Otimização passa para o **evento de conversão real**
- Lookalike sobre **convertidos** (não sobre seguidores)
- Retargeting sobre o pool construído na fase anterior
- CBO passa a fazer sentido (agora você **quer** que o algoritmo concentre)
- Criativo: o vencedor da descoberta, com variações

---

## 7. Armadilhas de plataforma (Meta — verifique equivalentes em outras)

### 7.1 Campos imutáveis após criação
**`destination_type` (local de conversão) do conjunto de anúncios não pode ser alterado depois de criado.** Se errar, só deletando e recriando.

➡️ **Sempre defina explicitamente na criação.** Omitir faz a plataforma escolher um default que pode não ser o desejado.

Editáveis: `optimization_goal`, `targeting`, orçamento, nome.

### 7.2 Combinações inválidas de objetivo × destino × otimização
Nem toda combinação existe. Exemplo real: objetivo Engajamento + destino Site + otimização ThruPlay faz a plataforma exigir pixel e evento de conversão, bloqueando a publicação.

➡️ **Teste a combinação criando UM conjunto antes de criar todos.** Erro de combinação descoberto no quarto conjunto custa quatro recriações.

### 7.3 Taxonomia de interesse é volátil e incompleta
- Ferramentas de nicho e marcas pequenas **não existem** como interesse — só marcas com escala de consumo são indexadas.
- **A exclusão de interesses foi removida** de muitas contas. Não presuma que dá para excluir adjacências indesejadas.
- Segmentação por **cargo** puxa do perfil de uma rede específica — se seu público declara a profissão em outra rede, o sinal não existe lá. Verifique o tamanho estimado antes de confiar.

### 7.4 Tamanhos exibidos na busca são globais
O número ao lado do interesse na caixa de busca é alcance mundial. **O que importa é o estimador após aplicar geo e demografia.**

### 7.5 Valores de configuração são depreciados sem aviso
Exemplo real: tipos de direcionamento por localização foram aposentados; conjuntos criados por API com o valor implícito ficaram inválidos e bloqueados para publicação.

➡️ **Defina valores explicitamente em vez de aceitar defaults**, e revalide após mudanças de plataforma.

### 7.6 Cache de interface engana
Editar um objeto deletado em aba antiga é silencioso e perde trabalho. **Confirme estado pela API, não pela tela.** Se a API e a interface divergem, a API está certa.

---

## 8. Anti-padrões documentados (erros reais, custo real)

### 8.1 🔴 Otimizar por ação barata e superficial
**O erro mais caro documentado.** Uma campanha otimizou por *visita ao perfil* com CTA para a rede social. O algoritmo fez exatamente o pedido: encontrou quem completa a ação mais barata possível — curiosos. Resultado: milhares de seguidores sem relação com o produto, que depois precisaram ser removidos manualmente.

**Princípio:** *o público que você constrói é função do que você otimizou.* Otimizar por visita de perfil constrói audiência de visitantes de perfil.

➡️ Otimize sempre pela **ação mais profunda que o volume sustentar**.

### 8.2 Lookalike sobre semente contaminada
LAL replica semelhança com a semente. Semente pequena e ruidosa amplifica o ruído para milhões. E **limpeza posterior da semente não corrige lookalikes já criadas** — elas congelam o estado do dia em que nasceram.

### 8.3 Desconfie de CPM barato
Num caso real, CPM baixo foi indicador de **audiência pouco disputada e irrelevante**, não de eficiência. O criativo que trouxe público qualificado tinha CPM 4× maior — e CTR 6× melhor.

### 8.4 Confiar em log de envio como prova de entrega
"Evento enviado" no seu log ≠ "evento aceito pela plataforma". Verifique no painel da plataforma ou via API de diagnóstico do dataset.

### 8.5 Assumir que código deployado está funcionando
Um pipeline pode estar tecnicamente correto, deployado e nunca ter sido exercitado. **Só um teste ponta a ponta real prova** — e ele frequentemente revela que um elo silencioso está quebrado.

---

## 9. Checklist de replicação

**Antes de qualquer gasto:**
- [ ] Auditoria de conta, pixel, públicos e campanhas antigas concluída
- [ ] Campanhas antigas **desativadas** antes de adicionar método de pagamento
- [ ] Instrumentação validada com **conversão real ponta a ponta**
- [ ] Redirects testados com `curl` (preservam query string?)
- [ ] Postura de consentimento decidida
- [ ] Verificação da empresa e 2FA em andamento
- [ ] Inteligência competitiva mapeada (ângulos ocupados e vagos)

**Ao desenhar a descoberta:**
- [ ] N células = N hipóteses distintas, uma delas de controle
- [ ] Primeiro frame de cada uma nomeia conceito + persona
- [ ] **Tudo idêntico entre células, menos o criativo**
- [ ] ABO (orçamento por conjunto), nunca CBO
- [ ] Otimização por evento de topo, nunca por conversão escassa
- [ ] Segmentação por nicho, não por persona
- [ ] Geografia concentrada
- [ ] UTM único e estável por célula

**Ao publicar:**
- [ ] Combinação objetivo × destino × otimização testada em UM conjunto primeiro
- [ ] `destination_type` definido explicitamente
- [ ] Estado confirmado **pela API**, não pela interface
- [ ] **Todas as células ativadas no mesmo momento**

**Durante:**
- [ ] Gates de saúde em D3 e D7; abort só por qualidade de dado
- [ ] Nenhuma célula pausada por performance

---

## 10. Regra de governança

**Nenhum agente ativa campanha nem autoriza gasto.** Todo trabalho de configuração sobe **pausado**; a ativação é sempre decisão humana explícita.

Isso não é formalidade: campanha ativada por engano gasta dinheiro real e, pior, contamina dados de forma irreversível (uma célula que rodou sozinha por dois dias não volta a ser comparável).
