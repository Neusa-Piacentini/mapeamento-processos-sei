# Avaliação AS-IS — melhoria e automação com IA

Gerado por `scripts/gerar_site.py` a partir de `saida/bpmn/avaliacao_<código>.json`; navegação completa no site `docs/site/index.html`.

**Portfólio:** 7 atividades em 1 processos — 1 com alto potencial de IA, 5 com potencial médio; 3 agregam valor, 4 são necessárias sem valor (rito legal e controle) e 0 não agregam valor.

## P06 — Fiscalização técnica de campo (programada e por demanda)

Situação do código: estudo de caso. A coorte tem um único processo, nativo do SEI (SEI-480002/001314/2024, fiscalizações programadas de 2024 nas unidades da Águas do Rio – Bloco 1), com um só caminho e sem auditoria de classificador; a mediana de um caso nativo é o próprio caso, e nada aqui autoriza generalizar para o tipo de processo. O trabalho é pequeno diante do tempo: 297,7–480,3 h de trabalho estimado (hipótese, a calibrar com servidores) para um lead time de 636 du, dos quais 552 du são espera entre atividades e 84 du, execução das atividades. Dois blocos concentram a espera: 306 du sem nenhuma unidade com o processo aberto, que não se separam de processo parado (e incluem prazos dados à concessionária, que não são desperdício), e 203 du com a Procuradoria antes do Parecer 759/2025, assinado em 28/08/2026 (a data no corpo da peça é 25/06/2026), no mesmo dia em que o processo foi sobrestado. A concessionária contestou o alcance da fiscalização, e o processo terminou sobrestado, sem encerramento. A IA ajuda na conferência e na redação das peças e no controle de prazos; reduzir a espera depende de dar dono, marco e prazo-alvo a cada etapa, sobretudo à fila da Procuradoria.

| Caso | Lead time (du) | Trabalho (h) | Eficiência do ciclo | Espera dominante |
|---|---|---|---|---|
| SEI-480002/001314/2024 (estudo de caso) | 636 | 297.7–480.3 | 7.8–12.6% | 89% |

**Gargalo:** A fila na Procuradoria antes do Parecer 759/2025: é a maior posse por unidade do caso e a maior espera antes de uma atividade, e vem depois de esperas sem nenhuma unidade com o processo antes do parecer técnico e antes da resposta à contestação, e de uma espera com a Secretaria antes da primeira ciência. Não há como saber, só pela linha do tempo, se foi fila de carga, pendência de diligência ou parecer pronto aguardando assinatura. — A espera antes da ciência do parecer jurídico é de 205 du, das quais 203 du com a Procuradoria e 2 du com a Secretaria; o Parecer 759/2025 e a ciência saem em 28/08/2026, de modo que a espera aparece antes da ciência (antes do parecer, o fato registra 0 du). A data no corpo do parecer é 25/06/2026, diferente da assinatura, o que sugere intervalo de assinatura ou de juntada a confirmar com a Procuradoria. A segunda maior espera é de 106 du sem nenhuma unidade com o processo aberto, entre a última remessa de relatórios à concessionária, em 30/01/2025, e o Parecer CASAN 250/2025, de 08/07/2025: não se separa processo parado de prazo dado à concessionária. Entre as esperas ligadas a este trecho do fluxo há ainda 55 du com a Secretaria antes da ciência do parecer técnico e 24 du sem unidade antes da resposta à contestação (a lista não inclui as esperas entre vistorias).

**Desperdícios:** Espera (alta); Estoque (alta); Defeitos/retrabalho (média); Transporte (média); Movimentação (média); Superprocessamento (baixa); Talento não aproveitado (baixa).

**Oportunidades prioritárias:**

1. **Fila de pareceres da Procuradoria com marco de entrada, prazo-alvo e alerta de idade** (IA + Lean; impacto alto, esforço baixo) — Ataca a espera, não o trabalho: 203 du com a Procuradoria antes da ciência do parecer jurídico, a maior posse por unidade do caso, com data no corpo do parecer (25/06/2026) diferente da assinatura (28/08/2026). Com um caso, não se estima redução; a medir.
2. **Dono e marco para o processo entre as etapas, com alerta de processo sem unidade e sem ato final** (IA + Lean; impacto alto, esforço baixo) — Ataca a espera: 306 du sem nenhuma unidade com o processo aberto, dos quais 106 du antes do parecer técnico e 24 du antes da resposta à contestação. Parte do total é prazo dado à concessionária e intervalo programado do ciclo, que o painel deve excluir; a redução depende da resposta da gestão ao alerta (a medir).
3. **Registro e vínculo da resposta da concessionária no processo principal no dia em que chega** (Lean; impacto médio, esforço baixo) — Não reduz trabalho de forma relevante (mediana de 0,8–1,1 h por ocorrência do ofício, nos casos nativos), mas elimina a ambiguidade: hoje a resposta só é datada pela juntada do processo anexado (138 du de espera da concessionária e 41 du indeterminados, não separáveis de processo parado); com o registro no dia da chegada, a espera de resposta passa a ter data real.

## Dados: o que existe e o que falta

| Campo | Situação | Como completar |
|---|---|---|
| Sequência de unidades e atividades | disponível | — |
| Tempo de espera | disponível | — |
| Tempo de trabalho | estimado | Estudo de tempo curto com as unidades (~20 peças-tipo) para calibrar a faixa |
| Descritivo, gatilho e saída | disponível | Validar redação com a unidade |
| Entradas (insumos) | disponível | — |
| Ferramentas, cálculos e testes | disponível | Sistemas e planilhas fora do SEI não aparecem nas peças — confirmar com a unidade |
| Competências | inferido | Validar com a gestão de pessoas e cruzar com a matriz de competências da agência |
| Base normativa | disponível | — |
| Executor (cargo) | parcial | Quem prepara a peça nem sempre assina: confirmar equipe com a unidade |
| Volume por ano | parcial | Extrair a lista completa de processos por tipo no SEI de todas as unidades |
| Custo da atividade (R$) | ausente — possível | Remuneração por cargo (Portal da Transparência RJ) × horas calibradas |
| Força de trabalho por unidade (FTE) | ausente — possível | Dados de RH da agência |
| Qualidade percebida pelo usuário/regulado | ausente — possível | Pesquisa ou dados da Ouvidoria |
| Peças restritas | ausente — limitado | Upload pelo gabinete (o relator já aceita PDF) ou acesso interno |
