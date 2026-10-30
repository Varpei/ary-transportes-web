# ARY Transportes — Contexto do Projeto

## Escopo

Este repositório contém o protótipo web estático da ARY Transportes e Viagens. A arquitetura obrigatória é HTML5 semântico, Tailwind CSS via CDN com configuração inline segura e Vanilla JS ES6+. Não há backend nem banco de dados exposto.

## Regras de execução

- Mantenha a estrutura de diretórios existente.
- Use HTML5 semântico, Tailwind CSS via CDN e JavaScript nativo ES6+.
- Não adicione bibliotecas externas sem ordem explícita.
- Não altere regras de negócio sem instrução explícita.
- Todo input de usuário deve passar pelas funções de sanitização de `src/assets/js/security.js`.
- Faça mudanças pequenas, rastreáveis e compatíveis com o protótipo.
- Valide arquivos e comandos antes de concluir.

## Dados imutáveis

Nome: ARY Transportes e Viagens. Abrangência oficial: Todo o Território do Tocantins e Maranhão (TO / MA). WhatsApps oficiais: `(63) 99293-5934` (`https://wa.me/5563992935934`) e `(63) 99293-0031` (`https://wa.me/5563992930031`). Instagram: `@_arytransporte` (`https://www.instagram.com/_arytransporte/`). Paleta: `#1B4956` e `#8CC63F`.

## Prompt de contexto para comunicação entre IAs

Você é um agente executor sob supervisão de arquitetura. Antes de alterar o projeto, leia este arquivo, `.github/copilot-instructions.md` e `docs/ESTADO_ARQUITETURA.md`. Implemente somente o escopo solicitado, preserve decisões existentes, não instale frameworks pesados e registre claramente arquivos alterados, validações executadas e bloqueios.

## Épico 8 (30/10/2026) — Adequação ao Feedback do Sócio (Posicionamento Estadual TO/MA e Foco Executivo/Escolar)

- ISSUE-13: **CONCLUÍDO** — interface sem cidades específicas, com abrangência oficial **Todo o Território do Tocantins e Maranhão (TO / MA)**.
- ISSUE-14: **CONCLUÍDO** — governança e base RAG atualizadas automaticamente, com foco primário em **Transporte Executivo e Transporte Escolar** e Fretamento de Vans & Viagens.
- Domínio mantido em `varpei.github.io/ary-transportes-web/` até o fechamento comercial da proposta.
- Histórico unificado preservado para os projetos ContraGlosa e ARY Transportes.
