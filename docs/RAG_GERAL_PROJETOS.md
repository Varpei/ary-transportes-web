# RAG Geral de Projetos — ARY Transportes e Viagens

## Identidade e operação

- Nome: ARY Transportes e Viagens
- Abrangência oficial: Todo o Território do Tocantins e Maranhão (TO / MA)
- WhatsApp: `(63) 99293-5934` e `(63) 99234-2641`
- E-mail: `arytransporteseviagens@gmail.com`
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
- ISSUE-15: limpeza cirúrgica do Hero e navbar.
- ISSUE-16: atualização do estado, auditoria e base RAG.
- ISSUE-29: live-reload local por `/__mtime`, com headers de segurança preservados.
- ISSUE-30: processamento do kit oficial de design e da foto memorial do Sr. Ary.
- ISSUE-31: whitelist do novo WhatsApp/e-mail e motor dinâmico de excursões com ocultação de pacotes expirados.
- ISSUE-32: revisão integral da interface, apresentação institucional, oito serviços, homenagem, frota e rodapé comercial.
- ISSUE-36: refinamento do lightbox sem quadro branco.
- ISSUE-37: remoção do cursor de edição em textos visuais, com formulários preservados.
- ISSUE-38: remoção do filtro azul e correção do estado oculto do lightbox.

## Épico 18 — Publicação Oficial / Go-Live

- ISSUE-36 a ISSUE-38: **CONCLUÍDAS** e aprovadas visualmente em `http://localhost:8080`.
- ISSUE-39: auditoria final de segurança e estrutura concluída.
- ISSUE-40: publicação oficial pendente de `git add`, `git commit` e `git push` pelo responsável fora desta sessão.
- ISSUE-41: menu hambúrguer mobile-first com navegação sem encavalamento.
- ISSUE-42: homenagem ao Sr. Ary movida fisicamente para depois do Hero.
- ISSUE-43: documentação e validação local do Épico 19 concluídas.

## Épico 19 — Correção Mobile-First e Reposicionamento da Homenagem

- ISSUE-41 a ISSUE-43: **CONCLUÍDAS** — menu responsivo e memorial do Sr. Ary no topo da página.

## Regras de continuidade

Leia `CLAUDE.md`, `.github/copilot-instructions.md` e `docs/ESTADO_ARQUITETURA.md` antes de modificar o projeto. Preserve os dados imutáveis, não adicione frameworks ou bibliotecas sem autorização e encaminhe inputs por `window.ARYSecurity`.

## Épico 8 (30/10/2026) — Adequação ao Feedback do Sócio (Posicionamento Estadual TO/MA e Foco Executivo/Escolar)

- ISSUE-13: **CONCLUÍDO** — interface sem cidades específicas, com abrangência oficial **Todo o Território do Tocantins e Maranhão (TO / MA)**.
- ISSUE-14: **CONCLUÍDO** — governança e base RAG atualizadas automaticamente, com foco primário em **Transporte Executivo e Transporte Escolar** e Fretamento de Vans & Viagens.
- Domínio mantido em `varpei.github.io/ary-transportes-web/` até o fechamento comercial da proposta.
- Histórico unificado preservado para os projetos ContraGlosa e ARY Transportes.

## Épico 9 (30/10/2026) — Limpeza Cirúrgica do Hero e Navbar

- ISSUE-15: **CONCLUÍDO** — H1 sem localidade, subtítulo repetido removido e link `Diferenciais` excluído da navbar.
- ISSUE-16: **CONCLUÍDO** — documentação de estado, auditoria e RAG atualizada.
