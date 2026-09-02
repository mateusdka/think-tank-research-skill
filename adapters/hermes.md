# Adapter para Hermes Agent

## Instalação assistida

Envie o endereço do repositório ao Hermes e peça:

> Instale a skill `think-tank-research` no perfil ativo, revise todos os arquivos antes da cópia e valide a descoberta da skill sem executar uma pesquisa real.

O agente deve resolver o diretório pelo perfil ativo. Não presuma que o destino é sempre `~/.hermes`; use o `HERMES_HOME` efetivo quando configurado.

## Execução

- Use o mecanismo de delegação para pareceres independentes.
- O limite simultâneo pode ser menor que o número de personas. Nesse caso, execute em lotes sem mudar os mandatos.
- Use ferramentas de pesquisa e extração para fatos externos.
- Grave os artefatos no workspace quando o usuário pedir uma pesquisa durável.
- Passe a cada subagente um briefing autossuficiente. Ele não conhece a conversa principal.

## Verificação

1. Confirme que `think-tank-research` aparece no catálogo do perfil ativo depois do recarregamento necessário.
2. Faça um teste de descoberta com uma pergunta que peça múltiplas perspectivas.
3. Não rode a pesquisa completa no teste de instalação.
4. Confirme que nenhuma skill, memória ou configuração de outro perfil foi alterada.

Documentação oficial: https://hermes-agent.nousresearch.com/docs/
