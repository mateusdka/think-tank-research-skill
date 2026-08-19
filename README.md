# Skill de Pesquisa Think Tank

Uma skill reutilizável que executa pesquisas estruturadas com múltiplas personas: as lentes especialistas investigam um tema de forma independente, enquanto uma camada de síntese preserva divergências, avalia a qualidade das evidências e produz um relatório consolidado.

![Cinco robôs em uma sala de reunião debatendo uma pesquisa](assets/think-tank-research-robots-meeting.png)



## O que é

Esta skill transforma pesquisas no formato de “think tank” em um fluxo operacional. Ela foi pensada para relatórios estratégicos, análises de mercado e comunicação, decisões de produto, pesquisa tecnológica, planejamento editorial e outras perguntas em que uma resposta linear apagaria trade-offs importantes.

Não é um prompt de interpretação de papéis. As personas funcionam como lentes metodológicas, com mandatos, padrões de evidência, limites e contratos de saída explícitos.



## Principais recursos

- Estrutura um briefing de pesquisa antes da delegação;
- Seleciona de 3 a 7 personas de pesquisa distintas;
- Executa investigações independentes por persona;
- Exige separação entre evidência, inferência, hipótese e opinião estratégica;
- Constrói uma matriz de convergência e divergência;
- Preserva objeções minoritárias em vez de forçar falso consenso;
- Produz um relatório consolidado com recomendações, grau de confiança e apêndice de fontes.

## Conteúdo do repositório

```text
.
├── SKILL.md
├── assets/
│   └── think-tank-research-robots-meeting.png
├── templates/
│   ├── research-brief.md
│   ├── persona-report.md
│   └── final-report.md
├── LICENSE
├── .gitignore
└── README.md
```

## Instalação no Hermes Agent

Copie esta pasta para o diretório de skills do Hermes, por exemplo:

```bash
mkdir -p ~/.hermes/skills/research
cp -R think-tank-research-skill ~/.hermes/skills/research/think-tank-research
```

Depois, reinicie ou recarregue o Hermes para que o índice de skills seja atualizado.

## Uso básico

Peça um relatório de pesquisa com múltiplas perspectivas, por exemplo:

> Use um processo de think tank para avaliar se uma pequena consultoria deveria oferecer workshops de IA para equipes de marketing no Brasil.

Uma boa tarefa inclui:

- pergunta central;
- público-alvo;
- escopo/geografia;
- profundidade desejada;
- fontes aceitáveis;
- formato de saída esperado;
- restrições ou sensibilidades conhecidas.

Se algum campo importante estiver faltando, a skill orienta o agente a fazer uma única pergunta de esclarecimento ou a prosseguir com premissas explícitas.



## Templates

A pasta `templates/` contém:

- `research-brief.md` — modelo para estruturar o brief inicial de pesquisa;
- `persona-report.md` — contrato de saída para cada persona especialista;
- `final-report.md` — estrutura do relatório consolidado do think tank.



## Guardrails de segurança e qualidade

A skill desencoraja explicitamente:

- citações falsas;
- consenso artificial;
- resultados superficiais com “cinco personas dizendo a mesma coisa”;
- tratar afirmações repetidas sem fonte como evidência forte;
- expor contexto privado desnecessariamente a subagentes;
- usar esse processo para decisões jurídicas, médicas, financeiras ou de segurança de alto risco sem verificação em fontes primárias e ressalvas adequadas.



## Licença

MIT. Consulte `LICENSE`.
