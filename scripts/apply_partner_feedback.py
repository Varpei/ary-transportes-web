#!/usr/bin/env python3
"""Apply the partner's statewide TO/MA positioning feedback deterministically."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_all(path: Path, replacements: list[tuple[str, str]]) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = original
    for old, new in replacements:
        updated = updated.replace(old, new)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def update_site() -> None:
    site_replacements = [
        ("Aeroporto de Imperatriz - MA (CCR Aeroportos)", "Receptivo em Aeroportos (Tocantins e Maranhão)"),
        ("Aeroporto de Imperatriz - MA", "Receptivo em Aeroportos (Tocantins e Maranhão)"),
        ("Aeroporto de Imperatriz", "Receptivo em Aeroportos (Tocantins e Maranhão)"),
        ("Araguaína - TO, Imperatriz - MA e Região", "Todo o Território do Tocantins e Maranhão"),
        ("Araguaína - TO e Imperatriz - MA", "Todo o Território do Tocantins e Maranhão"),
        ("Transporte Escolar em Araguaína - TO", "Transporte Escolar com Segurança e Pontualidade"),
        ("Transporte Escolar em Araguaína", "Transporte Escolar com Segurança e Pontualidade"),
        ("Araguaína - Tocantins - Brasil", "Região do Tocantins e Maranhão - Brasil"),
        ("Araguaína - TO", "Tocantins e Maranhão (TO / MA)"),
        ("Araguaína", "Tocantins"),
        ("Imperatriz", "Maranhão"),
    ]
    target_files = [
        ROOT / "src/index.html",
        ROOT / "src/assets/js/security.js",
        ROOT / "src/assets/js/whatsapp-tracking.js",
        ROOT / "src/assets/js/app.js",
        ROOT / "app_codespaces.py",
    ]
    for path in target_files:
        replace_all(path, site_replacements)

    index = ROOT / "src/index.html"
    replace_all(
        index,
        [
            (
                'content="ARY Transportes e Viagens: fretamento de vans, transporte escolar em Tocantins e transporte executivo no Receptivo em Aeroportos (Tocantins e Maranhão).">',
                'content="Transporte Executivo, Transporte Escolar e Fretamento de Vans em Todo o Território do Tocantins e Maranhão">',
            ),
            (
                'content="fretamento de vans Tocantins, transporte escolar Tocantins, transfer Receptivo em Aeroportos (Tocantins e Maranhão), ARY Transportes">',
                'content="transporte executivo, transporte escolar e fretamento de vans no Tocantins e Maranhão, ARY Transportes">',
            ),
            (
                "<title>ARY Transportes e Viagens | Fretamento, Escolar e Executivo</title>",
                "<title>ARY Transportes e Viagens | Transporte Executivo, Escolar e Fretamento no Tocantins e Maranhão</title>",
            ),
            (
                '"address": {"@type": "PostalAddress", "addressLocality": "Tocantins", "addressRegion": "TO", "addressCountry": "BR"},\n    "areaServed": ["Tocantins e Maranhão (TO / MA)", "Maranhão e Região"]',
                '"address": {"@type": "PostalAddress", "addressLocality": "Tocantins e Maranhão", "addressRegion": "TO / MA", "addressCountry": "BR"},\n    "areaServed": [{"@type": "State", "name": "Tocantins"}, {"@type": "State", "name": "Maranhão"}]',
            ),
            (
                "Sua viagem começa com a ARY em Tocantins e Maranhão (TO / MA) e\n            região.",
                "Transporte Executivo, Transporte Escolar e Fretamento de Vans em Todo o Território do Tocantins e Maranhão.",
            ),
            (
                "Fretamento de vans para viagens e turismo, transporte escolar em\n            Tocantins e transporte executivo ou receptivo no Receptivo em Aeroportos (Tocantins e Maranhão).",
                "Transporte Executivo, Transporte Escolar e Fretamento de Vans em Todo o Território do Tocantins e Maranhão.",
            ),
            (
                '<h3 class="mb-3 text-2xl font-bold text-ary-primary">Fretamento de Vans & Viagens</h3>',
                '<h3 class="mb-3 text-2xl font-bold text-ary-primary">Transporte Executivo & Receptivo de Aeroportos</h3>',
            ),
            (
                'data-select-service="Fretamento de Van"',
                'data-select-service="Transporte Executivo & Receptivo de Aeroportos"',
            ),
            (
                '<h3 class="mb-3 text-2xl font-bold text-ary-primary">Transporte Escolar com Segurança e Pontualidade</h3>',
                '<h3 class="mb-3 text-2xl font-bold text-ary-primary">Transporte Escolar</h3>',
            ),
            (
                'data-select-service="Transporte Escolar com Segurança e Pontualidade"',
                'data-select-service="Transporte Escolar"',
            ),
            (
                '<h3 class="mb-3 text-2xl font-bold text-ary-primary">Executivo & Receptivo de Aeroporto</h3>',
                '<h3 class="mb-3 text-2xl font-bold text-ary-primary">Fretamento de Vans & Viagens</h3>',
            ),
            (
                '<p class="mb-6">Atendimento VIP com Toyota Corolla e vans executivas, incluindo traslado direto no Receptivo em Aeroportos (Tocantins e Maranhão).</p><button data-select-service="Transporte Executivo / Transfer Aeroporto"',
                '<p class="mb-6">Turismo, excursões, viagens intermunicipais e interestaduais com frota executiva confortável.</p><button data-select-service="Fretamento de Vans & Viagens (TO e MA)"',
            ),
            (
                '<option>Fretamento de Van</option>\n            <option>Transporte Escolar com Segurança e Pontualidade</option>\n            <option>Transporte Executivo / Transfer Aeroporto</option>',
                '<option>Transporte Executivo &amp; Receptivo de Aeroportos</option>\n            <option>Transporte Escolar</option>\n            <option>Fretamento de Vans &amp; Viagens (TO e MA)</option>',
            ),
            (
                "<p>Transfer VIP corporativo e receptivo no Receptivo em Aeroportos (Tocantins e Maranhão).</p>",
                "<p>Transfer VIP corporativo e receptivo em aeroportos de Tocantins e Maranhão.</p>",
            ),
            ("<p>Região do Tocantins e Maranhão - Brasil</p>", "<p>Região do Tocantins e Maranhão - Brasil</p>"),
        ],
    )
    replace_all(
        index,
        [
            (
                '"address": {"@type": "PostalAddress", "addressLocality": "Tocantins", "addressRegion": "TO", "addressCountry": "BR"},\n    "areaServed": ["Tocantins e Maranhão (TO / MA)", "Maranhão - MA"]',
                '"address": {"@type": "PostalAddress", "addressLocality": "Tocantins e Maranhão", "addressRegion": "TO / MA", "addressCountry": "BR"},\n    "areaServed": [{"@type": "State", "name": "Tocantins"}, {"@type": "State", "name": "Maranhão"}]',
            ),
            (
                '<p class="mb-6">Turismo, excursões, Pousada Pipes, viagens intermunicipais e interestaduais com Iveco Daily,\n            Sprinter e Ducato.</p><button data-select-service="Transporte Executivo & Receptivo de Aeroportos"',
                '<p class="mb-6">Atendimento VIP com Toyota Corolla e vans executivas para compromissos corporativos e receptivos.</p><button data-select-service="Transporte Executivo & Receptivo de Aeroportos"',
            ),
            (
                '<p class="mb-6">Atendimento VIP com Toyota Corolla e vans executivas, incluindo traslado direto no Aeroporto\n            de Maranhão - MA.</p><button data-select-service="Transporte Executivo / Transfer Aeroporto"',
                '<p class="mb-6">Turismo, excursões, viagens intermunicipais e interestaduais com frota executiva confortável.</p><button data-select-service="Fretamento de Vans & Viagens (TO e MA)"',
            ),
            (
                'data-select-service="Transporte Executivo / Transfer Aeroporto"',
                'data-select-service="Fretamento de Vans & Viagens (TO e MA)"',
            ),
            (
                '<h3 class="mb-3 text-2xl font-bold text-ary-primary">Transporte Executivo & Receptivo de Aeroportos</h3>\n          <p class="mb-6">Turismo, excursões, viagens intermunicipais e interestaduais com frota executiva confortável.</p><button data-select-service="Fretamento de Vans & Viagens (TO e MA)"',
                '<h3 class="mb-3 text-2xl font-bold text-ary-primary">Fretamento de Vans & Viagens</h3>\n          <p class="mb-6">Turismo, excursões, viagens intermunicipais e interestaduais com frota executiva confortável.</p><button data-select-service="Fretamento de Vans & Viagens (TO e MA)"',
            ),
            (
                'de Maranhão - MA.</p><button data-select-service="Fretamento de Vans & Viagens (TO e MA)"',
                'de vans em todo o território do Tocantins e Maranhão.</p><button data-select-service="Fretamento de Vans & Viagens (TO e MA)"',
            ),
        ],
    )
    replace_all(
        ROOT / "app_codespaces.py",
        [
            (
                "ARY Transportes e Viagens (Araguaina-TO / Maranhão-MA)",
                "ARY Transportes e Viagens (Todo o Território do Tocantins e Maranhão)",
            ),
            (
                "ARY Transportes e Viagens (Araguaina-TO / Imperatriz-MA)",
                "ARY Transportes e Viagens (Todo o Território do Tocantins e Maranhão)",
            ),
        ],
    )


def update_governance() -> None:
    official_scope = "Todo o Território do Tocantins e Maranhão (TO / MA)"
    focus = "Transporte Executivo e Transporte Escolar"
    governance_replacements = [
        ("Base: Araguaína - Tocantins - Brasil; atuação forte no Aeroporto de Imperatriz - MA e região.", f"Abrangência oficial: {official_scope}."),
        ("Base: Araguaína - Tocantins - Brasil", f"Abrangência oficial: {official_scope}"),
        ("Atuação: Aeroporto de Imperatriz - MA e região", f"Abrangência oficial: {official_scope}"),
        ("Cidade base: Araguaína - Tocantins - Brasil", f"Abrangência oficial: {official_scope}"),
        ("Base: Araguaína - Tocantins - Brasil; atuação forte no Aeroporto de Imperatriz - MA e região.", f"Abrangência oficial: {official_scope}."),
        (
            "Nome: ARY Transportes e Viagens. Abrangência oficial: Todo o Território do Tocantins e Maranhão (TO / MA), com atuação forte no Aeroporto de Imperatriz - MA e região.",
            f"Nome: ARY Transportes e Viagens. Abrangência oficial: {official_scope}.",
        ),
    ]
    for relative in ("CLAUDE.md", ".github/copilot-instructions.md", "docs/ESTADO_ARQUITETURA.md", "docs/RAG_GERAL_PROJETOS.md"):
        replace_all(ROOT / relative, governance_replacements)
    for relative in ("docs/ESTADO_ARQUITETURA.md", "docs/RAG_GERAL_PROJETOS.md"):
        path = ROOT / relative
        lines = path.read_text(encoding="utf-8").splitlines()
        deduplicated: list[str] = []
        seen_lines: set[str] = set()
        for line in lines:
            if line in {
                "- Abrangência oficial: Todo o Território do Tocantins e Maranhão (TO / MA)",
                "- ISSUE-13: CONCLUÍDO — adequação da interface ao posicionamento estadual TO/MA.",
                "- ISSUE-14: CONCLUÍDO — atualização automática da governança e base RAG.",
            }:
                if line in seen_lines:
                    continue
                seen_lines.add(line)
            deduplicated.append(line)
        path.write_text("\n".join(deduplicated) + "\n", encoding="utf-8")

    estado = ROOT / "docs/ESTADO_ARQUITETURA.md"
    estado_replacements = [
        ("2. Transporte escolar em Araguaína - TO.", "2. Transporte escolar com segurança e pontualidade em todo o território do Tocantins e Maranhão."),
        ("3. Transporte executivo e receptivo de aeroporto em Imperatriz - MA e região.", "3. Transporte executivo e receptivo de aeroportos em todo o território do Tocantins e Maranhão."),
        ("- ISSUE-12: CONCLUÍDO — preparação e verificação dos links públicos de apresentação.", "- ISSUE-12: CONCLUÍDO — preparação e verificação dos links públicos de apresentação.\n- ISSUE-13: CONCLUÍDO — adequação da interface ao posicionamento estadual TO/MA.\n- ISSUE-14: CONCLUÍDO — atualização automática da governança e base RAG."),
        ("- Data: 2026-10-29", "- Data: 2026-10-30"),
        ("- Resultado: working tree limpo, `main` sincronizada com `origin/main`, health check aprovado.", "- Resultado: posicionamento estadual TO/MA aplicado, auditoria zero-cidades aprovada e governança sincronizada."),
    ]
    replace_all(estado, estado_replacements)

    for relative in ("CLAUDE.md", ".github/copilot-instructions.md", "docs/ESTADO_ARQUITETURA.md", "docs/RAG_GERAL_PROJETOS.md"):
        path = ROOT / relative
        content = path.read_text(encoding="utf-8")
        marker = "## Épico 8 (30/10/2026) — Adequação ao Feedback do Sócio (Posicionamento Estadual TO/MA e Foco Executivo/Escolar)"
        if marker not in content:
            content = content.rstrip() + (
                "\n\n"
                + marker
                + "\n\n"
                f"- ISSUE-13: **CONCLUÍDO** — interface sem cidades específicas, com abrangência oficial **{official_scope}**.\n"
                f"- ISSUE-14: **CONCLUÍDO** — governança e base RAG atualizadas automaticamente, com foco primário em **{focus}** e Fretamento de Vans & Viagens.\n"
                "- Domínio mantido em `varpei.github.io/ary-transportes-web/` até o fechamento comercial da proposta.\n"
                "- Histórico unificado preservado para os projetos ContraGlosa e ARY Transportes.\n"
            )
            path.write_text(content, encoding="utf-8")


def audit_zero_cities() -> None:
    forbidden = re.compile(r"araguaína|araguaina|imperatriz", re.IGNORECASE)
    violations: list[str] = []
    for path in (ROOT / "src").rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8", errors="ignore")
            count = len(forbidden.findall(text))
            if count:
                violations.append(f"{path.relative_to(ROOT)}: {count}")
    if violations:
        raise RuntimeError("Auditoria zero-cidades falhou: " + ", ".join(violations))
    print("Auditoria zero-cidades: 0 ocorrências em src/")


def main() -> None:
    update_site()
    update_governance()
    audit_zero_cities()
    print("Feedback do sócio aplicado com sucesso.")


if __name__ == "__main__":
    main()
