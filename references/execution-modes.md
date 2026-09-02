# Modos de execução

Escolha o modo pelas capacidades reais do ambiente. Não anuncie paralelismo, isolamento ou persistência sem verificá-los.

## 1. Workspace persistente com múltiplos agentes

Use quando o ambiente permite criar agentes independentes e gravar arquivos no projeto.

Estrutura recomendada:

```text
research/
├── brief.md
├── source-pack.md
├── personas/
│   ├── 01-[slug].md
│   ├── 02-[slug].md
│   └── ...
├── evidence-map.md
├── convergence-matrix.md
└── final-report.md
```

Execute pareceres independentes em paralelo quando houver capacidade. Cada agente recebe o brief completo, seu mandato, o contrato de saída e apenas o contexto privado necessário.

**Qualidade esperada:** maior independência entre lentes, rastreabilidade e retomada do trabalho.

## 2. Sandbox com múltiplos agentes ou tarefas

Use quando a plataforma oferece execução de código e arquivos temporários, mas não acesso livre às pastas locais do usuário.

- Crie a estrutura de pesquisa no sandbox.
- Exporte o relatório final e, se possível, os pareceres.
- Não descreva os arquivos do sandbox como persistentes sem confirmação.
- Não pressuponha acesso a URLs, conectores ou arquivos não anexados.

**Qualidade esperada:** independência semelhante ao modo persistente durante a sessão, com persistência limitada pelo produto.

## 3. Sessão única sequencial

Use quando não há subagentes ou execução paralela.

1. Congele o brief.
2. Defina todas as personas antes do primeiro parecer.
3. Produza cada parecer em um bloco isolado, sem revisar os anteriores.
4. Só depois do último parecer, construa o mapa de evidências e a síntese.
5. Declare no relatório que as lentes foram simuladas sequencialmente pelo mesmo agente.

**Qualidade esperada:** disciplina analítica preservada, mas menor independência entre lentes e maior risco de contaminação pelo contexto acumulado.

## 4. Pesquisa sem acesso externo

Use apenas fontes fornecidas pelo usuário e conhecimento que possa ser tratado explicitamente como contexto não verificado.

- Não fabrique referências.
- Marque fatos atuais não verificáveis como lacunas.
- Reduza o grau de confiança.
- Diferencie ausência de evidência de evidência de ausência.

## Declaração obrigatória no relatório

Registre:

- modo usado;
- quantidade de personas planejadas e concluídas;
- acesso a fontes externas: disponível, parcial ou indisponível;
- persistência dos artefatos: local, sandbox ou somente conversa;
- limitações que afetaram independência, cobertura ou confiança.
