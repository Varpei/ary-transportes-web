# Estado da Arquitetura

## Estado atual

- Projeto: `ary-transportes-web`
- Tipo: protótipo web estático
- Arquitetura: HTML5 semântico, Tailwind CSS via CDN com configuração inline segura e Vanilla JS ES6+
- Backend: inexistente
- Banco de dados exposto: inexistente
- Servidor local: `python3 app_codespaces.py`
- Ambiente de desenvolvimento: GitHub Codespaces via `.devcontainer/devcontainer.json`
- Dependência prevista: Pillow para otimização de imagens

## Estrutura base

- `src/assets/css`: folhas de estilo
- `src/assets/js`: scripts do navegador
- `src/assets/img/raw`: imagens originais
- `src/assets/img/optimized`: imagens processadas
- `scripts`: automações auxiliares

## Governança

As decisões devem permanecer compatíveis com HTML5 semântico, Tailwind CSS via CDN e JavaScript nativo. Não adicionar bibliotecas externas sem ordem explícita. Todo input de usuário deve passar pelas funções de sanitização em `src/assets/js/security.js`.

## Dados imutáveis do cliente

- Nome: ARY Transportes e Viagens
- Abrangência oficial: Todo o Território do Tocantins e Maranhão (TO / MA)
- WhatsApp 1: `(63) 99293-5934` — `https://wa.me/5563992935934`
- WhatsApp 2: `(63) 99293-0031` — `https://wa.me/5563992930031`
- Instagram: `@_arytransporte` — `https://www.instagram.com/_arytransporte/`
- Paleta: azul petróleo escuro `#1B4956` e verde lima vibrante `#8CC63F`

### Pilares de serviço

1. Fretamento de vans: viagens, turismo, pousadas, excursões e transporte intermunicipal/interestadual.
2. Transporte escolar com segurança e pontualidade em todo o território do Tocantins e Maranhão.
3. Transporte executivo e receptivo de aeroportos em todo o território do Tocantins e Maranhão.

### Frota real mapeada

- Van Executiva Iveco Daily 50-180 Branca: 5 estrelas, ar-condicionado, DVD, som, tomadas e poltronas reclináveis.
- Van Executiva Mercedes-Benz Sprinter Prata: teto alto e rodado duplo.
- Van Executiva Fiat Ducato Minibus Branca: interior em couro cinza/preto e tapete vermelho.
- Sedan Executivo Toyota Corolla Prata: transfer VIP e aeroporto.

## Status de Issues

- ISSUE-01: CONCLUÍDO — setup, governança e blindagem base.
- ISSUE-02: CONCLUÍDO — pipeline de mídia, conversão WebP e placeholders.
- ISSUE-03: CONCLUÍDO — governança e blindagem base.
- ISSUE-04: CONCLUÍDO — protótipo completo, estilos, frota, filtros e lightbox.
- ISSUE-05: CONCLUÍDO — motor WhatsApp, rastreamento de conversões e formulário.
- ISSUE-06: CONCLUÍDO — servidor blindado Codespaces e sincronização GitHub.
- ISSUE-07: CONCLUÍDO — servidor híbrido, blueprint Render, base RAG unificada e pipeline zero-touch.
- ISSUE-08: CONCLUÍDO — auditoria zero-trust, checklist de arquivos, mídia, segurança, Git e servidor.
- ISSUE-09: CONCLUÍDO — mapeamento semântico determinístico, crop de logos e blur de regiões sensíveis.
- ISSUE-10: CONCLUÍDO — processamento dos slots reais e preparação do acesso público via servidor configurável.
- ISSUE-11: CONCLUÍDO — classificação visual inteligente das 14 fotos 20.56, crop e blur de privacidade.
- ISSUE-12: CONCLUÍDO — preparação e verificação dos links públicos de apresentação.
- ISSUE-13: CONCLUÍDO — adequação da interface ao posicionamento estadual TO/MA.
- ISSUE-14: CONCLUÍDO — atualização automática da governança e base RAG.
- ISSUE-15: CONCLUÍDO — simplificação do H1, remoção do subtítulo repetido e limpeza da navbar.
- ISSUE-16: CONCLUÍDO — atualização do estado, auditoria e base RAG do Épico 9.

## Última auditoria

- Data: 2026-10-30
- Relatório: `docs/AUDITORIA_CHECKLIST.md`
- Resultado: posicionamento estadual TO/MA aplicado, auditoria zero-cidades aprovada e governança sincronizada.

## Épico 9 (30/10/2026) — Limpeza Cirúrgica do Hero e Navbar

- ISSUE-15: **CONCLUÍDO** — H1 sem localidade, subtítulo redundante removido e item `Diferenciais` retirado da navbar.
- ISSUE-16: **CONCLUÍDO** — estado da arquitetura, auditoria e base RAG atualizados.

## Épico 8 (30/10/2026) — Adequação ao Feedback do Sócio (Posicionamento Estadual TO/MA e Foco Executivo/Escolar)

- ISSUE-13: **CONCLUÍDO** — interface sem cidades específicas, com abrangência oficial **Todo o Território do Tocantins e Maranhão (TO / MA)**.
- ISSUE-14: **CONCLUÍDO** — governança e base RAG atualizadas automaticamente, com foco primário em **Transporte Executivo e Transporte Escolar** e Fretamento de Vans & Viagens.
- Domínio mantido em `varpei.github.io/ary-transportes-web/` até o fechamento comercial da proposta.
- Histórico unificado preservado para os projetos ContraGlosa e ARY Transportes.
