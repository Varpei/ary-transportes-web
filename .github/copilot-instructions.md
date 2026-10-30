# Instruções do Copilot

- Trate o projeto como um protótipo web estático.
- Use HTML5 semântico, Tailwind CSS via CDN com configuração inline segura e Vanilla JS ES6+.
- Não há backend ou banco de dados exposto.
- Não instale React, Next.js, Vue, Angular, WordPress ou pacotes npm desnecessários.
- Nunca adicione bibliotecas externas sem ordem explícita.
- Não faça alterações criativas em regras de negócio.
- Leia `docs/ESTADO_ARQUITETURA.md` antes de qualquer modificação.
- Ao concluir uma Issue, atualize seu status em `docs/ESTADO_ARQUITETURA.md`.
- Todo input de usuário deve passar pelas funções de sanitização em `src/assets/js/security.js`.
- Preserve compatibilidade com o servidor HTTP Python na porta 8080.
- Faça alterações cirúrgicas e valide a sintaxe dos arquivos modificados.
- Não exponha segredos, credenciais ou dados sensíveis.

## Dados imutáveis do cliente

- Nome: ARY Transportes e Viagens
- Abrangência oficial: Todo o Território do Tocantins e Maranhão (TO / MA).
- WhatsApps: `(63) 99293-5934` e `(63) 99293-0031`
- Instagram: `@_arytransporte`
- Cores: `#1B4956` e `#8CC63F`

## Épico 8 (30/10/2026) — Adequação ao Feedback do Sócio (Posicionamento Estadual TO/MA e Foco Executivo/Escolar)

- ISSUE-13: **CONCLUÍDO** — interface sem cidades específicas, com abrangência oficial **Todo o Território do Tocantins e Maranhão (TO / MA)**.
- ISSUE-14: **CONCLUÍDO** — governança e base RAG atualizadas automaticamente, com foco primário em **Transporte Executivo e Transporte Escolar** e Fretamento de Vans & Viagens.
- Domínio mantido em `varpei.github.io/ary-transportes-web/` até o fechamento comercial da proposta.
- Histórico unificado preservado para os projetos ContraGlosa e ARY Transportes.
