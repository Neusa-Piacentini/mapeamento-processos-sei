# Plano — auditoria de acurácia e ampliação da base

30/10/2026

## Fase 1 — Auditoria de acurácia (prioritária)

Objetivo: medir, por camada do pipeline, quanto do que está no site é **verificável na fonte**, e corrigir
o que for alucinação até que cada camada passe num critério de aceite. Só depois disso a base é ampliada.

### Camadas e risco

| Camada | Produzida por | Risco | Como auditar |
|---|---|---|---|
| A. Trilha (estadias, posse, tempos) | código | regra errada | caso conferido à mão + consistência SEI 2 × banco do relator + propriedades (partição do tempo, datas) |
| B. Fichas de trabalho por documento (357) | LLM sobre o texto | alucinação de número, norma, insumo ou cálculo | (1) ancoragem automática: todo número, percentual, valor e norma da ficha tem que aparecer no texto da peça; (2) auditor independente lê o texto e julga cada campo numa amostra estratificada |
| C. Classificação dos 251 processos (P01–P36) | LLM | rótulo errado | reclassificação cega de uma amostra por outro auditor; concordância (kappa) |
| D. Modelos BPMN canônicos | LLM sobre evidências | etapa, laço ou número sem lastro | consistência automática modelo × vínculos × trilha (frequência, dias, horas, unidade); auditor confere decisões e laços |
| E. Vínculos atividade → peças e descritivos | LLM | peça ligada à atividade errada; descritivo inventado | unidade da peça × raia, ordem cronológica × ordem do fluxo; auditor confere descritivos |
| F. Avaliações (síntese, gargalo, desperdícios, oportunidades) | LLM sobre as fichas | número ou fato sem lastro, causalidade inventada | ancoragem automática dos números nas fontes; auditor verifica cada afirmação factual |

### Critério de aceite (por camada)

- **Alucinação** (afirmação sem lastro ou contraditada pela fonte): ≤ 2% das afirmações auditadas e
  nenhuma em número que sustente conclusão (lead time, espera, horas, gargalo).
- **Imprecisão** (lastro parcial, arredondamento, atribuição a caso errado): ≤ 10%.
- **Classificação:** concordância ≥ 85% no código principal (kappa ≥ 0,8); divergências explicadas.
- Toda falha encontrada é corrigida na origem (prompt, regra ou dado) e a camada é reauditada.

### Travas permanentes no pipeline

1. Validador de ancoragem: números, normas e referências de documento só passam se existirem na fonte
   (texto da peça, ficha ou trilha); o que não ancorar vira "a verificar" ou sai.
2. Afirmações das avaliações com referência rastreável (atividade, caso, campo da ficha).
3. Relatório de auditoria regenerável a cada rodada (`scripts/auditoria.py`).

## Fase 2 — Ampliação da base: do caso ao procedimento

Objetivo: trocar "o fluxo de 2 casos" por "o procedimento interno para aquele tipo de demanda", com
variantes, frequências e distribuições.

### Acervo disponível

- 251 processos do SEI 2 já classificados (P06 32, P01 29, P21 24, P04 23, P35 20, P08 18, P19 16 …);
- banco do relator: 25.781 documentos de 398 processos, com texto e análise por documento;
- trilha de todos (estadias, posse, tempos).

### Passos

1. **Coorte por processo organizacional:** todos os processos do código com trilha nativa do SEI e
   texto suficiente (cobertura de peças substantivas ≥ 60%); processos migrados entram só no conteúdo.
2. **Fichas de trabalho para todas as peças da coorte** (mesmo prompt auditado; custo ≈ US$ 1 a cada
   100 peças; cache por documento).
3. **Classificador de atividade:** cada passagem de cada processo da coorte é rotulada com a atividade
   canônica do código (ou "fora do modelo"), a partir da unidade, do tipo de peça e da ficha. É o passo
   que transforma documentos soltos em eventos comparáveis.
4. **Mineração de processo sobre a coorte:**
   - variantes (sequências de atividades) com frequência;
   - conformidade de cada caso com o modelo canônico (atividades puladas, extras, laços);
   - caminhos alternativos que aparecem em ≥ 15% dos casos viram ramo do BPMN; os raros viram exceção
     anotada.
5. **Distribuições por atividade** (mediana, quartis e n, não faixa de 2 casos):
   - espera e permanência;
   - esforço;
   - laudas;
   - frequência de insumos, ferramentas, saídas e competências;
   - taxa de retrabalho e de diligência.
6. **Modelo de procedimento revisado:** BPMN com caminho principal, variantes frequentes, probabilidades
   nas decisões e tempos em distribuição.
7. **Avaliação refeita** sobre a coorte, com a mesma trava de ancoragem: os desperdícios e as
   oportunidades passam a valer para o tipo de demanda, não para o caso.
8. **Site** com distribuição por atividade e seletor de variante.

### Critério para cada código entrar

- Pelo menos 5 casos com trilha nativa e texto (P06, P01, P21, P04, P35, P08 e P19 atendem; P03, P36,
  P22, P05 e P12 ficam como estudo de caso até ampliar o acervo).
- Classificador de atividade auditado: concordância ≥ 85% com a rotulagem humana ou independente de uma amostra.

### Fora do acervo atual

P20 (Ouvidoria) e P07 (sanção) precisam de processos de outras unidades: ampliar a lista de processos
do SEI 2 e hidratar no relator. Essa etapa depende de acesso e entra depois.
