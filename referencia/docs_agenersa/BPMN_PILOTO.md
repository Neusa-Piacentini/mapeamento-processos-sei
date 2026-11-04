# BPMN AS-IS dos processos-piloto

30/10/2026 · arquivos BPMN 2.0 em `saida/bpmn/<código>.bpmn` (abrem no Camunda Modeler, bpmn.io e Bizagi) ·
visualizador com os 8 diagramas em `docs/bpmn/index.html`.

## Como os modelos foram feitos

1. **Evidências por código** (`scripts/evidencias_bpmn.py` → `saida/bpmn/evidencias_<código>.md`): participação
   das unidades e transições em todos os processos SEI do código, mais as tarefas em ordem dos casos típico e
   crítico, com dias úteis, faixa de horas (piso–teto), sinais de perda e espera dominante.
2. **Modelo canônico** (`saida/bpmn/modelo_<código>.json`, formato em `saida/bpmn/ESPECIFICACAO_MODELO.md`):
   consolida típico e crítico num fluxo de no máximo 25 elementos. Encaminhamentos puros da Secretaria não viram
   tarefa; a fila que geram vai para a nota da tarefa seguinte. Variações observadas viram decisões com laço; o
   que só aparece num caso tem frequência "1/2". Nada fora das evidências.
3. **Gerador** (`scripts/gerar_bpmn.py`): layout automático com raias horizontais, colunas por camada
   topológica e roteamento ortogonal. Cores: vermelho para espera dominante, âmbar para sinal de perda. Os 8
   arquivos importam no bpmn-js sem avisos. Regras de roteamento:
   - cada vão entre colunas tem trilhos verticais próprios, um por seta, em ordem escolhida para minimizar
     cruzamentos; o vão se alarga conforme o número de trilhos;
   - trechos horizontais só atravessam colunas por linhas livres; se não houver, correm pela margem inferior
     da raia;
   - decisões soltam os ramos alternativos pelos vértices de cima ou de baixo, em pente (tronco único e um
     braço por destino); junções recebem quem vem de cima pelo vértice de cima e quem vem de baixo pelo de
     baixo;
   - laços (voltas a etapas anteriores) correm num corredor sob a piscina, os mais curtos mais perto dela;
   - entradas e saídas das tarefas são espalhadas ao longo da lateral;
   - a ordem das raias é a que dá o menor custo visual medido no desenho (atravessar elemento, sobreposição,
     cruzamento), com a raia do início no alto.

   `scripts/checar_bpmn.py` mede esses defeitos em qualquer `.bpmn`. Antes e depois da revisão de
   roteamento (soma dos 8 diagramas): setas atravessando elementos 6 → 0; trechos sobrepostos 5 → 2 (fusões na
   entrada de junções); cruzamentos 26 → 27, a maioria inerente aos laços do modelo.

Cada tarefa traz no nome `[casos · dias úteis · horas]`, e a documentação do elemento repete esses dados e a
nota de evidência.

## Os 8 fluxos

| Código | Fluxo principal | Laços e variações |
|---|---|---|
| P01 Reajuste tarifário | pleito → recebimento e sorteio → cálculo paramétrico (CAPET) → parecer (PROC) → razões finais → relatoria e deliberação → publicação → encerramento | diligência à FIPE, ao Município ou à concessionária com reiteração quando o prazo vence; conciliação entre as partes; verificação das tarifas nas faturas (só no crítico) |
| P06 Fiscalização | vistoria, relatório e notificação → defesa → parecer técnico → parecer jurídico → sorteio → razões finais → relatoria e deliberação → publicação e ofícios → registro de providências | requisição de documentos à concessionária e ao INEA; devolução do relator à PROC ou à câmara técnica |
| P21 Ocorrência de usuário | relato da Ouvidoria → notificação da concessionária → parecer sobre sanção → sorteio → razões finais → relatoria e deliberação → publicação → encerramento | apuração técnica pela câmara (1/2); vista ao usuário e ciência da Ouvidoria; embargos |
| P35 Crises de abastecimento | ofício e vistoria → justificativa ou plano → parecer técnico → parecer jurídico → distribuição → razões finais → relatoria e deliberação → publicação → cumprimento e encerramento | ouvir a concessionária; complementação técnica com a CAPET (crítico); reiteração sem resposta; embargos |
| P36 Grandes usuários | pleito → enquadramento (REG) → parecer jurídico → razões finais → relatoria e deliberação → publicação e ofícios → encerramento | minuta ajustada pela concessionária volta à PROC |
| P08 Metas contratuais | recebimento → atestado de KPIs (CASAN) → notificação com prazo → PROC → parecer final da CASAN → proposta de padronização → distribuição | nenhum (um só caso, sem laço) |
| P03 Reequilíbrio | pleito → análise da CAPET → vista → sorteio → diligências do relator → recálculo da TIR (CAPET) → CASAN → PROC → razões finais → relatoria e deliberação → publicação → encerramento | pedidos de dados às partes; PROC devolve sem parecer após 180 du; complementação de cenários e nova rodada de razões finais |
| P22 Órgãos de controle e MP | ofício do MPRJ → Ouvidoria → ofício da CASAN → apuração → parecer jurídico → razões finais → relatoria e penalidade → publicação → encerramento | reiteração e prorrogação de prazo à concessionária |

## Pontos a validar com as unidades

Decisões de modelagem que a trilha sustenta, mas que precisam do olhar de quem executa:

- **P01:** a conciliação volta à PROC, o que simplifica uma decisão intermediária do Conselho-Diretor no caso
  típico. A pergunta "Verificar aplicação das novas tarifas?" é inferida: as peças não trazem o critério que
  leva a CAPET a conferir as faturas.
- **P06:** o laço de devolução do relator não ocorre nos dois casos-piloto. Ele vem das trilhas dos 32
  processos do código: o gabinete mandou o processo à PROC 23 vezes e às câmaras técnicas 22 vezes. A raia
  técnica é "CAENE ou CASAN".
- **P21 e P35:** os casos críticos tiveram vista concedida depois do encerramento, o que não está modelado.
  No P21 crítico, quem retirou os autos da PROC foi a Secretaria; o modelo representa isso como decisão da PROC.
- **P35:** os dois casos têm naturezas diferentes (plano de contingência de gás e rompimento de adutora). Vale
  confirmar se são um só processo ou duas variantes.
- **P22:** o caso típico é uma apuração de denúncia do MPRJ que termina em penalidade, sem ofício de resposta
  ao MP. Convém confirmar se representa o código ou se P22 deve ser só a resposta ao órgão de controle.
- **P08 e P03:** só há um caso elegível; os fluxos são uma trilha, não um padrão.
- **Razões finais** foram modeladas como etapa normal (devido processo), não como perda, mesmo concedendo prazo.
  Os prazos que a deliberação fixa à concessionária também contam como resultado da decisão, não como perda.
- Alguns intervalos das notas (marcados com "~") foram calculados das datas, em dias úteis sem feriados.
