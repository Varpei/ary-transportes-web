# Base RAG Unificada — ARY Transportes e Viagens

## Identidade

- Nome: ARY Transportes e Viagens
- Base: Araguaína - Tocantins - Brasil
- Área de atuação: Aeroporto de Imperatriz - MA e região
- Instagram: `@_arytransporte`
- WhatsApp principal: `(63) 99293-5934` — `https://wa.me/5563992935934`
- WhatsApp secundário: `(63) 99293-0031` — `https://wa.me/5563992930031`

## Arquitetura

- Front-end estático em HTML5 semântico, Tailwind CSS via CDN e Vanilla JS ES6+.
- Servidor Python em `app_codespaces.py`.
- Health checks: `/healthz` e `/api/status`.
- Porta: variável `PORT`, com padrão `8080`.
- Não há backend de negócio nem banco de dados exposto.

## Serviços

1. Fretamento de vans para viagens, turismo, pousadas, excursões e trajetos intermunicipais ou interestaduais.
2. Transporte escolar em Araguaína - TO.
3. Transporte executivo e receptivo no Aeroporto de Imperatriz - MA e região.

## Frota

- Iveco Daily 50-180 branca: 5 estrelas, ar-condicionado, DVD, som, tomadas e poltronas reclináveis.
- Mercedes-Benz Sprinter prata: teto alto e rodado duplo.
- Fiat Ducato Minibus branca: interior em couro cinza/preto e tapete vermelho.
- Toyota Corolla prata: transfer VIP e aeroporto.

## Segurança e operação

- Inputs devem passar por `window.ARYSecurity`.
- URLs de WhatsApp e Instagram são allowlisted.
- O servidor injeta CSP, HSTS, X-Frame-Options, NoSniff, Referrer-Policy e Permissions-Policy.
- Não inventar preços, horários, endereços, capacidade ou promessas comerciais ausentes nesta base.
