# RAG Geral de Projetos — ARY Transportes e Viagens

## Identidade e operação

- Nome: ARY Transportes e Viagens
- Abrangência oficial: Todo o Território do Tocantins e Maranhão (TO / MA)
- WhatsApp: `(63) 99293-5934` e `(63) 99293-0031`
- Instagram: `@_arytransporte`

## Arquitetura consolidada

- Protótipo estático em HTML5 semântico, Tailwind CSS via CDN e Vanilla JS ES6+.
- Servidor: `app_codespaces.py`, com porta configurável por `PORT` e padrão `8080`.
- Health checks: `/healthz` e `/api/status`.
- Deploy: `render.yaml`, GitHub Codespaces e `scripts/auto_deploy_pipeline.py`.
- Não há backend de negócio nem banco de dados exposto.

## Issues concluídas

- ISSUE-01: governança e ambiente.
- ISSUE-02: pipeline de mídia e slots WebP.
- ISSUE-03: headers e sanitização zero-trust.
- ISSUE-04: protótipo front-end e frota.
- ISSUE-05: WhatsApp, tracking e JSON-LD.
- ISSUE-06: servidor Codespaces/cloud e sincronização.
- ISSUE-07: RAG, blueprint cloud e automação de deploy.
- ISSUE-11: classificação visual determinística e mapa semântico das fotos.
- ISSUE-12: preview público e sincronização da apresentação.

## Regras de continuidade

Leia `CLAUDE.md`, `.github/copilot-instructions.md` e `docs/ESTADO_ARQUITETURA.md` antes de modificar o projeto. Preserve os dados imutáveis, não adicione frameworks ou bibliotecas sem autorização e encaminhe inputs por `window.ARYSecurity`.

## Épico 8 (30/10/2026) — Adequação ao Feedback do Sócio (Posicionamento Estadual TO/MA e Foco Executivo/Escolar)

- ISSUE-13: **CONCLUÍDO** — interface sem cidades específicas, com abrangência oficial **Todo o Território do Tocantins e Maranhão (TO / MA)**.
- ISSUE-14: **CONCLUÍDO** — governança e base RAG atualizadas automaticamente, com foco primário em **Transporte Executivo e Transporte Escolar** e Fretamento de Vans & Viagens.
- Domínio mantido em `varpei.github.io/ary-transportes-web/` até o fechamento comercial da proposta.
- Histórico unificado preservado para os projetos ContraGlosa e ARY Transportes.
