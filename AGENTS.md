# AGENTS.md — think-tank-research-skill

Este repositório empacota uma skill pública para o Hermes Agent.

## Escopo

- Mantenha `SKILL.md` como a definição canônica da skill.
- Mantenha estruturas reutilizáveis de relatório em `templates/`.
- Não inclua relatórios privados de pesquisa, material de clientes, credenciais, configurações locais do Hermes ou exportações de memória específicas de usuário.
- Trate este repositório como candidato a publicação pública: toda mudança deve ser segura para publicar.

## Verificação antes de publicar

1. Procure caminhos privados, segredos, nomes de clientes, tokens, referências a `.env` com valores reais e relatórios privados.
2. Confirme que `README.md`, `LICENSE`, `SKILL.md` e os templates estão presentes.
3. Não crie remoto no GitHub, não faça push e não publique sem autorização explícita.
