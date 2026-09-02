# Adapter para Claude Code

## Instalação

Claude Code descobre Skills pessoais em `~/.claude/skills/` e Skills de projeto em `.claude/skills/`.

Instalação assistida:

> Instale a skill `think-tank-research` no escopo pessoal ou deste projeto, conforme eu indicar. Revise o conteúdo antes da cópia e valide a descoberta sem executar uma pesquisa real.

Escolha o escopo do projeto quando a metodologia só deve orientar um repositório. Use o escopo pessoal quando ela deve ficar disponível em trabalhos diferentes.

## Execução

- Use agentes ou tarefas independentes quando a sessão tiver esse recurso.
- Mantenha os pareceres em arquivos separados quando houver workspace.
- Se a sessão não oferecer isolamento suficiente, use o modo sequencial e declare a limitação.
- Só carregue referências necessárias à etapa atual.

## Verificação

1. Confirme a presença de `SKILL.md` na pasta escolhida.
2. Inicie ou recarregue a sessão conforme necessário para redescobrir Skills.
3. Faça um teste de acionamento sem iniciar a pesquisa completa.
4. Confirme o escopo instalado: pessoal ou projeto.

Referência oficial: https://code.claude.com/docs/en/skills
