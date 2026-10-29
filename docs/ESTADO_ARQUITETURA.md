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
- Cidade base: Araguaína - Tocantins - Brasil
- Atuação: Aeroporto de Imperatriz - MA e região
- WhatsApp 1: `(63) 99293-5934` — `https://wa.me/5563992935934`
- WhatsApp 2: `(63) 99293-0031` — `https://wa.me/5563992930031`
- Instagram: `@_arytransporte` — `https://www.instagram.com/_arytransporte/`
- Paleta: azul petróleo escuro `#1B4956` e verde lima vibrante `#8CC63F`

### Pilares de serviço

1. Fretamento de vans: viagens, turismo, pousadas, excursões e transporte intermunicipal/interestadual.
2. Transporte escolar em Araguaína - TO.
3. Transporte executivo e receptivo de aeroporto em Imperatriz - MA e região.

### Frota real mapeada

- Van Executiva Iveco Daily 50-180 Branca: 5 estrelas, ar-condicionado, DVD, som, tomadas e poltronas reclináveis.
- Van Executiva Mercedes-Benz Sprinter Prata: teto alto e rodado duplo.
- Van Executiva Fiat Ducato Minibus Branca: interior em couro cinza/preto e tapete vermelho.
- Sedan Executivo Toyota Corolla Prata: transfer VIP e aeroporto.

## Status de Issues

- ISSUE-01: Setup, governança e blindagem base concluídos.
- ISSUE-02: CONCLUÍDO — pipeline de mídia, conversão WebP e placeholders.
- ISSUE-03: Setup, governança e blindagem base concluídos.
- ISSUE-04: CONCLUÍDO — protótipo completo, estilos, frota, filtros e lightbox.
- ISSUE-05: CONCLUÍDO — motor WhatsApp, rastreamento de conversões e formulário.
- ISSUE-06: CONCLUÍDO — servidor blindado Codespaces e sincronização GitHub.
