# Documentation Language Parity Policy

🌐 **Language:** [Português](DOCUMENTATION_LANGUAGE_POLICY.md) | [English](DOCUMENTATION_LANGUAGE_POLICY.en.md)

## Principle

MagicGate public documentation treats **Brazilian Portuguese and English as first-class languages**.

No public Markdown document should exist in only one language.

> **No language parity, no publication.**

## File convention

- `FILE.md` is the PT-BR version.
- `FILE.en.md` is the English version.
- Both must contain a language selector at the top linking to the corresponding pair.

Example:

`README.md` ↔ `README.en.md`

## Semantic parity

PT-BR and EN versions must preserve the same material meaning, including:

- product version;
- price and currency;
- trial duration;
- completed capabilities;
- features under development;
- metrics and evidence classification;
- roadmap status;
- security and disclosure rules;
- boundaries between public and private content.

The English version should use natural technical English rather than mechanical word-for-word translation.

## Current commercial rule

Until a later approved commercial decision is made, documentation must preserve:

- **10 dias grátis** / **10 days free**;
- **US$ 19/mês** / **US$ 19/month**.

Any commercial change must update both languages in the same pull request.

## Change rule

When a document is created, changed, corrected, or removed:

1. its language pair must be created, changed, corrected, or removed in the same pull request;
2. both documents must preserve material equivalence;
3. neither version may disclose restricted information that the other version is not authorized to disclose;
4. technical terminology must remain consistent;
5. any material divergence blocks publication until corrected.

## Terminology

Technical terms that operate as product names, engineering concepts, or industry-standard terminology may remain in English in both versions when that improves precision. Examples include:

- Control Plane;
- Device ID;
- API Key;
- fail-closed;
- quality gates;
- first-pass success;
- MGPI;
- VS Code Control Center.

## Security

The existence of a translation never expands disclosure authorization.

If there is uncertainty about whether a detail may be published, the fail-closed default applies: the content remains unpublished until reviewed.

## Automation

Repository CI structurally verifies that every Markdown file has its PT-BR/EN pair and that both documents expose language-navigation links.

Semantic equivalence still requires human review.
