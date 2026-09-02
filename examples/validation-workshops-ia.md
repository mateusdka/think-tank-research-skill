# Caso de validação: workshops de IA para marketing no Brasil

Este caso foi usado para testar o Think Tank Research em ambientes diferentes com a mesma pergunta estratégica.

## Pergunta de teste

> Uma pequena consultoria deveria oferecer workshops de IA para equipes de marketing no Brasil? O relatório será lido pelos sócios e deve separar demanda, desenho da oferta, risco e teste de mercado.

A escolha de uma pergunta realista, com critérios conflitantes e lacunas de informação, permite observar mais do que a geração de texto: seleção do modo de execução, decomposição em lentes, disciplina de evidências, preservação de divergências e comportamento dos gates de qualidade.

## ChatGPT web

**Estado:** homologado ponta a ponta.

**Registro público da execução:** https://chatgpt.com/share/e/6a98753f-ff3c-8001-a3eb-4736b6b74bfb

Comportamentos observados durante a validação:

- descoberta e acionamento da skill a partir do pedido de pesquisa;
- cinco lentes com mandatos distintos: Mercado, Comprador, Oferta, Viabilidade da consultoria e Risco;
- separação entre evidência forte, evidência moderada e variáveis ainda desconhecidas;
- preservação de divergência entre uma leitura mais favorável ao lançamento e uma leitura de risco favorável a começar de forma estreita;
- disposição a pagar, preço, formato e ciclo comercial tratados como lacunas a resolver por piloto, não como números a inventar por desk research;
- recomendação condicionada em vez de promessa de ROI;
- `EVIDENCE_REVIEW: PASS_WITH_LIMITATIONS` e `EDITORIAL_REVIEW: PASS`.

## Claude.ai

**Estado:** homologado ponta a ponta no plano Free.

O Claude identificou o ambiente e selecionou o modo de **sessão única sequencial**, declarando que a independência entre lentes era simulada, não estrutural. O relatório final registrou cinco personas, pesquisa externa disponível e a limitação de não haver múltiplos agentes reais.

Comportamentos observados:

- cinco lentes concluídas com mandatos explícitos;
- mapa de evidências com força e limitações por afirmação;
- descarte explícito de números incompatíveis de tamanho de mercado, em vez de escolher arbitrariamente um deles;
- ausência de benchmark público de preço tratada como lacuna real;
- convergências e divergências apresentadas separadamente;
- recomendação final com confiança média e condições explícitas;
- `EVIDENCE_REVIEW: PASS_WITH_LIMITATIONS` e `EDITORIAL_REVIEW: PASS`;
- integridade factual declarada após a edição.

O relatório completo gerado no teste foi preservado separadamente durante a auditoria do projeto.

## O que este caso valida

Este teste não prova que duas plataformas produzem respostas idênticas, nem que as personas equivalem a especialistas humanos independentes.

Ele verifica algo mais específico: se o pacote consegue preservar os comportamentos centrais do método em runtimes diferentes.

| Comportamento | ChatGPT web | Claude.ai |
|---|---|---|
| Skill descoberta e acionada | Sim | Sim |
| Lentes com mandatos distintos | Sim | Sim |
| Limitações do ambiente declaradas | Sim | Sim |
| Evidência separada de inferência | Sim | Sim |
| Divergências preservadas | Sim | Sim |
| Lacunas mantidas como lacunas | Sim | Sim |
| Evidence review | PASS_WITH_LIMITATIONS | PASS_WITH_LIMITATIONS |
| Editorial review | PASS | PASS |
| Recomendação condicionada | Sim | Sim |

## Limites do teste

- O caso verifica comportamento metodológico, não equivalência textual entre modelos.
- Os dois ambientes web podem executar as lentes dentro de um único contexto; isso não oferece a mesma independência estrutural de subagentes separados.
- Resultados de pesquisa dependem das fontes acessíveis no momento da execução.
- A qualidade factual de um relatório específico continua dependendo da qualidade e cobertura das fontes encontradas.
- A homologação de um ambiente não implica homologação automática de outros runtimes.

Este caso deve ser lido como **evidência de portabilidade comportamental do método**, não como benchmark de qual modelo produz a melhor pesquisa.
