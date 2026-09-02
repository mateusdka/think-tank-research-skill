---
name: think-tank-research
description: Use quando uma pesquisa exigir múltiplas lentes. Sintetiza evidências e divergências.
version: 0.2.0
author: Mateus Fardin
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [pesquisa, multiagente, personas, sintese, evidencias]
    related_skills: []
---

# Think Tank Research

Conduz pesquisas por lentes metodológicas independentes e produz uma síntese que distingue consenso, divergência, evidência e incerteza. A skill se adapta a ambientes com múltiplos agentes, sandboxes ou apenas uma sessão sequencial.

## Quando usar

Use para:

- decisões que envolvem critérios diferentes, como mercado, público, viabilidade, risco e implementação;
- pesquisa estratégica, tecnológica, editorial, de produto ou política pública;
- revisão simulada por comitê ou painel de especialistas;
- comparação de perspectivas antes de uma recomendação;
- relatórios que precisam preservar discordâncias e lacunas.

Não use para:

- consulta factual simples;
- tarefa com um método único e autoritativo já definido;
- multiplicar opiniões sem pesquisa ou critérios diferentes;
- substituir aconselhamento profissional em decisões médicas, jurídicas, financeiras ou de segurança de alto risco.

## Pré-requisitos

Antes de iniciar, identifique:

- fontes e arquivos disponíveis;
- acesso ou não a pesquisa externa;
- possibilidade de criar tarefas ou agentes independentes;
- possibilidade de gravar arquivos e sua persistência;
- restrições de privacidade, prazo e formato.

Leia [os modos de execução](references/execution-modes.md) e escolha o modo pelas capacidades confirmadas. Consulte [a matriz de plataformas](references/platform-capabilities.md) quando estiver instalando ou adaptando a skill.

## Conceitos

### Persona metodológica

Uma persona não é um personagem nem uma voz fictícia. Ela possui:

1. **Mandato:** aspecto do problema pelo qual responde.
2. **Lente:** critérios e trade-offs que orientam a análise.
3. **Contrato de saída:** seções que deve entregar.
4. **Limites:** questões fora de seu papel.

### Think tank

É a etapa coordenadora que compara os pareceres. Não calcula uma média de opiniões. Ela pesa evidências, explicita pressupostos, preserva objeções e só recomenda quando houver sustentação suficiente.

## Procedimento

### 1. Estruture o brief

Use [o template de brief](templates/research-brief.md). Torne explícitos:

- tema e pergunta central;
- decisão ou resultado que a pesquisa deve apoiar;
- público do relatório;
- escopo geográfico e temporal;
- profundidade;
- fontes aceitáveis e disponíveis;
- riscos, dados sensíveis e restrições;
- formato final.

Pergunte apenas quando uma lacuna mudar materialmente a pesquisa. Nos demais casos, registre a premissa adotada.

**Conclusão:** pergunta, objetivo, público, escopo, modo e formato estão definidos.

### 2. Escolha o modo de execução

Selecione um dos modos:

1. workspace persistente com múltiplos agentes;
2. sandbox com agentes ou tarefas;
3. sessão única sequencial;
4. pesquisa limitada às fontes fornecidas.

Registre o modo no brief. Não presuma paralelismo, acesso externo ou persistência.

**Conclusão:** capacidades e limitações do ambiente estão documentadas.

### 3. Selecione as personas

Escolha de três a sete personas. Cinco é um ponto de partida, não uma regra.

Papéis possíveis:

- estrategista de mercado;
- analista técnico;
- pesquisador de usuários ou audiência;
- especialista do domínio;
- analista de risco;
- revisor de literatura;
- consultor de implementação;
- lente regulatória ou de impacto social.

Defina o elenco pelo problema. Una papéis que fariam as mesmas perguntas e usariam os mesmos critérios.

**Conclusão:** cada persona tem mandato, lente e limites distinguíveis.

### 4. Prepare o contrato de cada parecer

Use [o template de persona](templates/persona-report.md). Todos recebem o mesmo brief e pacote de fontes, além de seu mandato específico.

Regras para cada parecer:

- não sintetizar o comitê;
- não buscar consenso;
- não suavizar objeções do próprio mandato;
- separar evidência, inferência, hipótese e opinião estratégica;
- citar apenas fontes realmente inspecionadas;
- declarar perguntas em aberto e grau de confiança.

**Conclusão:** cada tarefa é autossuficiente e pode ser executada sem a conversa principal.

### 5. Execute os pareceres

Quando houver agentes independentes, execute em paralelo ou em lotes. Quando houver apenas uma sessão, congele todas as personas antes do primeiro parecer e não inicie a síntese até concluir a última.

Se uma persona falhar, registre a ausência. Não a substitua silenciosamente nem apresente o elenco planejado como concluído.

**Conclusão:** toda persona planejada tem parecer ou status de indisponibilidade.

### 6. Construa o mapa de evidências

Para cada afirmação relevante, registre:

| Afirmação | Fonte | Tipo | Personas | Força | Limitações |
|---|---|---|---|---|---|

Não conte a mesma fonte como múltiplas confirmações porque apareceu em pareceres diferentes.

**Conclusão:** evidências fortes, inferências, hipóteses e lacunas são distinguíveis.

### 7. Compare convergências e divergências

Construa uma matriz:

| Tema | Persona A | Persona B | Persona C | Síntese provisória |
|---|---|---|---|---|

Inclua consensos, conflitos, pressupostos, dependências e implicações para a decisão. Preserve uma objeção minoritária quando ela puder invalidar a recomendação sob certas condições.

**Conclusão:** nenhuma divergência material foi achatada.

### 8. Produza a síntese

Use [o template de relatório final](templates/final-report.md). A recomendação deve decorrer do mapa de evidências e indicar condições, limites e próximos passos.

Não confunda:

- repetição com confirmação;
- síntese com consenso;
- ausência de dado com resultado negativo;
- cenário plausível com previsão.

**Conclusão:** o relatório permite rastrear a recomendação até os pareceres e fontes.

### 9. Execute os dois gates de qualidade

Primeiro aplique [a revisão de evidências](references/evidence-review.md). Um resultado `EVIDENCE_REVIEW: FAIL` bloqueia a entrega como relatório validado.

Depois aplique [a revisão editorial anti-slop](references/editorial-review.md). Ela melhora clareza, precisão e ritmo sem editar dados, apagar divergências ou criar especificidade inexistente.

Por fim, compare a versão editada à versão aprovada no gate de evidências.

**Conclusão:** os dois resultados estão registrados e a integridade factual foi preservada.

## Guardrails

- Não fabrique fontes, citações ou dados.
- Passe a agentes apenas o contexto privado necessário.
- Não apresente personas simuladas como especialistas humanos consultados.
- Não use o processo para criar aparência de certeza.
- Não esconda limitações do ambiente de execução.
- Em temas de alto risco, priorize fontes primárias e validação profissional adequada.

## Recursos

- [Modos de execução](references/execution-modes.md)
- [Revisão de evidências](references/evidence-review.md)
- [Revisão editorial](references/editorial-review.md)
- [Capacidades por plataforma](references/platform-capabilities.md)
- [Exemplo de pergunta simples](examples/simple-question.md)
- [Exemplo de relatório estratégico](examples/strategic-report.md)

## Verificação final

- [ ] Brief, modo e limitações estão explícitos.
- [ ] Personas têm mandatos diferentes.
- [ ] Pareceres concluídos e ausentes estão identificados.
- [ ] Afirmações decisivas têm fonte ou rótulo epistemológico.
- [ ] Fontes repetidas não foram contadas como confirmações independentes.
- [ ] Divergências materiais permanecem visíveis.
- [ ] Recomendação indica confiança, condições e lacunas.
- [ ] `EVIDENCE_REVIEW` está registrado.
- [ ] `EDITORIAL_REVIEW` está registrado.
- [ ] A edição final preservou dados, citações e conclusões aprovadas.