# Mapeamento e melhoria de processos de agências reguladoras a partir do SEI

Repositório do curso. Ensina a **mapear, avaliar e redesenhar processos de uma agência reguladora a partir do
registro real do SEI** (andamentos, documentos juntados e texto das peças), em vez de entrevistas, e a fazer isso
com IA de forma verificável. Traz o método completo, o código que o executa e um **exemplo resolvido de ponta a ponta**:
o caso da AGENERSA (RJ), com todas as saídas reais.

A ideia é que você clone o repositório e **a sua IA (Claude Code, Codex ou equivalente) replique a metodologia no
seu órgão**, seguindo [`AGENTS.md`](AGENTS.md) e o [roteiro de replicação](docs/metodologia/ROTEIRO_REPLICACAO.md).

## O que o método entrega

| Fase | Pergunta | Produto |
|---|---|---|
| 0. Base e trilhas | Por onde cada processo passou, quanto tempo ficou em cada unidade e com quem estava? | Trilha, posse e espera por processo; classificação no catálogo de processos |
| 1. Piloto de conteúdo | O que cada peça fez e quanto trabalho ela contém? | Ficha de trabalho por peça, esforço (piso–teto), BPMN AS-IS, avaliação Lean/VSM/TOC |
| 2. Do caso ao procedimento | O fluxo dos casos-piloto vale para o tipo de demanda? | Coorte por tipo, distribuições por atividade, BPMN com % dos casos |
| 3. Do AS-IS ao TO-BE | O que a lei exige, quanto se cumpre, o que funciona em outros lugares e quanto se ganha? | Conformidade legal medida, benchmarking verificado, melhorias em 3 fases simuladas em 3 cenários, controles e metas |
| 4. Do TO-BE ao sistema | Que processo serve de piloto para um sistema de IA que o automatize por inteiro, e quanto custa e retorna? | Matriz de priorização com critérios medidos, custo × retorno em 3 cenários, capacidades de IA transversais e insumos para especificar o sistema |

No caso de referência, a fase 3 projeta, no cenário esperado, redução de 48% a 67% no tempo mediano dos três
processos-piloto (detalhes e faixas em [09_TOBE_SIMULACAO.md](docs/metodologia/09_TOBE_SIMULACAO.md)). Na fase 4, a matriz de priorização aponta o reajuste tarifário como piloto do sistema
([PRIORIZACAO_AUTOMACAO.md](docs/PRIORIZACAO_AUTOMACAO.md)). Horas de trabalho e custo são **hipótese até a calibração com
os servidores**.

## Por onde começar

1. **Leia a metodologia**, que é o centro deste repositório: [`docs/metodologia/`](docs/metodologia/00_VISAO_GERAL.md).
   - [00 Visão geral](docs/metodologia/00_VISAO_GERAL.md): ideia central, fases, fluxo de artefatos e os três tipos de etapa (script, agente com especificação, verificação).
   - Capítulos de 01 a 11, um por bloco: [coleta](docs/metodologia/01_COLETA_E_BASE.md), [trilha, tempo e posse](docs/metodologia/02_TRILHA_TEMPO_POSSE.md), [conteúdo e esforço](docs/metodologia/03_CONTEUDO_ESFORCO.md), [classificação e coorte](docs/metodologia/04_CLASSIFICACAO_COORTE.md), [BPMN](docs/metodologia/05_MODELAGEM_BPMN.md), [avaliação AS-IS](docs/metodologia/06_AVALIACAO_ASIS.md), [conformidade legal](docs/metodologia/07_CONFORMIDADE_LEGAL.md), [benchmarking](docs/metodologia/08_BENCHMARKING.md), [TO-BE e simulação](docs/metodologia/09_TOBE_SIMULACAO.md), [controles e metas](docs/metodologia/10_CONTROLES_METAS.md), [priorização da automação](docs/metodologia/11_PRIORIZACAO_AUTOMACAO.md).
   - [Boas práticas](docs/metodologia/BOAS_PRATICAS.md): os princípios que tornam o resultado confiável e como o código os impõe.
   - [Verificação da IA](docs/metodologia/VERIFICACAO_IA.md): tudo que foi produzido ou julgado por IA, como foi verificado e o que ainda não foi.
   - [Dados levantados](docs/metodologia/DADOS_LEVANTADOS.md): cada dado usado na melhoria, com fonte, script, confiança e o que obter no seu órgão.
2. **Escolha a sua trilha** no [roteiro de replicação](docs/metodologia/ROTEIRO_REPLICACAO.md):
   - **Rio de Janeiro (SEI-RJ):** o coletor e o perfil do SEI já funcionam. Basta o perfil do seu órgão.
   - **Outro Estado:** as instalações do SEI variam em rótulos, versão do módulo de pesquisa pública e redação dos
     andamentos. Crie o perfil do SEI do seu Estado ([COLETA_SEI.md](docs/adaptacao/COLETA_SEI.md)), o perfil do
     órgão (`perfis/modelo.py`), o catálogo de processos e a base normativa ([BASE_NORMATIVA.md](docs/adaptacao/BASE_NORMATIVA.md)).
3. **Abra a sua IA na raiz do repositório** e peça: *"Leia AGENTS.md e siga o roteiro de replicação para o meu órgão"*.

## Instalação

Python 3.12.

```bash
pip install -r requirements.txt -r requirements-coleta.txt
```

```bash
python -m pytest tests
```

Os testes devem passar logo após o clone: confirmam que o ambiente reproduz o caso de referência. Chaves de API, só
para as etapas com LLM, vão sempre por variável de ambiente (`ANTHROPIC_API_KEY` ou `OPENROUTER_API_KEY`) e nunca
entram no repositório.

## Mapa do repositório

| Pasta | Conteúdo |
|---|---|
| [`docs/metodologia/`](docs/metodologia/) | **A metodologia**: o que a IA do aluno lê para replicar |
| [`docs/adaptacao/`](docs/adaptacao/) | Como adaptar a outro Estado: coleta do SEI e base normativa |
| [`coleta/`](coleta/) | Coletor da Pesquisa Pública do SEI com perfil por Estado, texto das peças, análise por peça (LLM) e portão da coleta |
| [`perfis/`](perfis/) | Parâmetros do órgão: feriados, início do SEI, unidades, custo-hora, códigos. `rj_agenersa.py` (caso de referência) e `modelo.py` (para copiar). Escolhido pela variável `PERFIL` |
| [`catalogo/`](catalogo/) | Inventário de processos organizacionais (P01–P36 na AGENERSA) |
| [`scripts/`](scripts/) | Etapas determinísticas e portões; [`pipeline.py`](scripts/pipeline.py) encadeia tudo |
| [`tests/`](tests/) | `test_regras.py` (cada falha encontrada virou um caso sintético), `test_saidas.py` (propriedades das saídas), `test_coleta.py` |
| [`saida/`](saida/) | Saídas reais do caso AGENERSA: tabelas, modelos BPMN, avaliações, normas, benchmarking, melhorias, simulação, controles e priorização da automação (`saida/fase4/`). As `ESPECIFICACAO_*.md` em `saida/bpmn/` e `saida/fase3/` são as instruções das etapas feitas por agente |
| [`docs/`](docs/) (raiz) | Relatórios do caso de referência; [`docs/site/index.html`](docs/site/index.html) é o site navegável do mapeamento |

## Regras que não se negociam

- **Toda métrica sai de código reprodutível.** A IA escreve nomes, fluxos, decisões e propostas; o código escreve os
  números. Número em texto só como citação de um fato calculado, conferido por validador.
- **Toda etapa feita por IA tem especificação escrita antes, saída em formato fixo e verificação** (portão
  automático ou auditoria às cegas por outro agente).
- **Hipótese é marcada como hipótese.** Horas, custo e ganhos sem benchmark ficam como faixa e premissa explícita.
- **Dados pessoais ficam fora do git.** `dados/` está no `.gitignore`. Não republique nomes, e-mails nem o conteúdo
  de processos restritos.
- **Entregável para o órgão** (relatório, planilha, apresentação) não menciona IA nem caminhos locais. O material
  do curso pode e deve falar de IA.

## Sobre o caso de referência

Base: 251 processos do gabinete de um conselheiro da AGENERSA (dump de 16/06/2026), com piloto de 13 processos em
8 processos organizacionais, coorte de 117 processos em 12 códigos e TO-BE de três processos: reajuste tarifário
(P01), fiscalização (P06) e ocorrência de usuário (P21). As saídas estão em `saida/` como foram geradas, com três
ajustes nesta versão pública:

- **Nomes de pessoas trocados pela função.** Conselheiros viram "Conselheiro A", "Conselheiro B" etc. (a mesma letra
  para a mesma pessoa em todos os arquivos). Servidores, representantes de concessionárias, usuários e agentes
  políticos viram `[servidor da agência]`, `[representante da concessionária]`, `[usuário]` etc. Autores de doutrina,
  de estudos e julgadores de tribunais citados nas peças continuam com o nome, porque são citações públicas.
- **Texto integral das peças omitido** nas amostras da auditoria (`saida/auditoria/amostra_fichas*.jsonl`); as fichas
  ficam.
- **Notas internas do gabinete omitidas** no insumo da classificação.

Números de processo SEI e unidades da agência continuam, porque vêm da Pesquisa Pública do SEI. A especificação do
sistema (fase 5) não faz parte deste repositório.
