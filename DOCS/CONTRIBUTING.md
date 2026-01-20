# CONTRIBUTING / BEITRAGEN

Thank you for considering contributing to this project.  
Danke, dass du zu diesem Projekt beitragen möchtest.

This document defines how to propose changes, report issues, and submit pull requests in a reliable and reviewable way.  
Dieses Dokument beschreibt, wie du Änderungen vorschlägst, Issues meldest und Pull Requests sauber einreichst.

---

## 🇩🇪 Deutsch

### 1) Grundprinzipien

Wir legen Wert auf:
- **Nachvollziehbarkeit** (klare Commits, klare Beschreibungen)
- **Sicherheit** (keine Secrets, keine unsicheren Defaults)
- **Qualität** (Tests, Linting, saubere Architektur)
- **Respekt** (professionelle Kommunikation)

Beiträge sind willkommen – unabhängig davon, ob es sich um Bugfixes, Dokumentation, Security-Hardening oder Features handelt.

---

### 2) Kommunikations- und Ticket-Regeln

#### Issues
Bitte erstelle ein Issue für:
- Bugs / Fehlerbilder
- Feature Requests
- Verbesserungen an Dokumentation/UX
- Security-Hardening (nicht vertraulich)

**Nicht als öffentliches Issue melden:**
- Sicherheitslücken mit potenzieller Ausnutzung → siehe [SECURITY](SECURITY.md)

**Issue-Qualität (erwartet):**
- klare Problem-/Zielbeschreibung
- reproduzierbare Schritte (wenn Bug)
- Umgebung: OS, Python, Browser (falls UI), Deployment
- Logs/Screenshots (ohne sensible Daten)

---

### 3) Entwicklungsumgebung (empfohlen)

**Voraussetzungen**
- Python 3.11+ (oder projektabhängig)
- pip / venv
- Optional: Docker (für reproduzierbare Builds/Deployments)

**Setup (Beispiel)**
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

**Start (Beispiel)**
```bash
uvicorn app.main:app --reload
```

> Hinweis: Passe den Startbefehl an die Projekt-README und die tatsächlichen Entry-Points an.

---

### 4) Branching-Strategie

Empfohlen:
- `main`: stabil, releasefähig
- `feature/<kurzbeschreibung>`: neue Features
- `fix/<kurzbeschreibung>`: Bugfixes
- `docs/<kurzbeschreibung>`: Dokumentationsänderungen
- `chore/<kurzbeschreibung>`: Wartung/Refactor ohne Feature

Bitte erstelle Pull Requests **gegen `main`**, sofern nicht anders angegeben.

---

### 5) Commit-Konvention (empfohlen)

Bitte verwende aussagekräftige Commit Messages. Optional nach Conventional Commits:

- `feat:` neue Funktion
- `fix:` Bugfix
- `docs:` Dokumentation
- `refactor:` Refactoring ohne Feature
- `test:` Tests
- `chore:` Maintenance

**Beispiele**
- `feat: add severity filter to findings view`
- `fix: prevent zip-slip in extractor`
- `docs: update deployment instructions`

---

### 6) Code Style & Qualitätsregeln

**Allgemein**
- keine Secrets, Keys, Passwörter committen
- keine unsicheren Defaults in Produktivpfaden
- Fehlerbehandlung: klare Exceptions, saubere HTTP-Responses
- Logging: keine sensiblen Daten loggen

**Python**
- konsistente Typen/Signaturen
- klare Modulgrenzen (API / analysis / storage / ui)
- bevorzugt: `black`/`ruff`/`isort` (falls im Projekt verwendet)

**Frontend**
- keine Inline-Secrets
- I18N: neue Strings in DE/EN ergänzen
- saubere Fehlerbehandlung in API-Calls

---

### 7) Tests & Qualitätssicherung

Beiträge sollten:
- bestehende Tests nicht brechen
- neue Tests enthalten, wenn sinnvoll/erforderlich
- reproduzierbar laufen (lokal und CI)

Empfohlen:
- Unit Tests für Scanner-/Analyse-Logik
- Integration Tests für API-Endpunkte
- Regression Tests für behobene Bugs

Wenn dein PR bewusst ohne Tests kommt (z. B. reine Doku), erwähne das kurz im PR-Text.

---

### 8) Security & Privacy Regeln

- Keine echten Produktionsdaten in Repro-Dumps/Issues
- Tokens/Session-IDs/Keys immer redakten
- ZIP/Upload-Features: immer Pfad-Traversal-Schutz, Größenlimits, sichere Extraktion
- SQLAlchemy: sichere Queries, keine String-Konkatenation

Wenn du einen Security-Fix einreichst:
- beschreibe Impact + Mitigation
- liefere Tests/Regression (wenn möglich)
- verweise auf `SECURITY.md` (falls relevant)

---

### 9) Pull Request Checkliste

Bitte stelle sicher, dass dein PR:
- [ ] ein Issue referenziert (oder das Problem klar beschreibt)
- [ ] fokussiert ist (kein „alles in einem“-PR)
- [ ] Code style einhält
- [ ] Tests enthält bzw. begründet, warum nicht
- [ ] keine Secrets oder sensiblen Daten enthält
- [ ] Dokumentation aktualisiert, wenn nötig
- [ ] UI/I18N Änderungen in DE/EN berücksichtigt

---

### 10) Review-Prozess

Wir prüfen u. a.:
- Korrektheit und Reproduzierbarkeit
- Sicherheit (Input Validation, Auth, Data Handling)
- Performance (keine unnötigen Scans/Loops)
- Wartbarkeit (saubere Modulgrenzen)
- Dokumentation (wenn Feature-Impact)

Wir können um Änderungen bitten. Bitte fasse Feedback sauber in Folgeveränderungen zusammen.

---

### 11) Lizenz & Rechte

Mit deinem Beitrag erklärst du dich einverstanden, dass dein Code unter der Projektlizenz veröffentlicht werden kann.  
Wenn du Code aus anderen Quellen nutzt, stelle sicher, dass die Lizenz kompatibel ist und die Quelle korrekt angegeben wird.

<br>

---

<br>

### 1) Principles

We value:
- **Traceability** (clear commits, clear descriptions)
- **Security** (no secrets, no unsafe defaults)
- **Quality** (tests, linting, clean architecture)
- **Respect** (professional communication)

Contributions are welcome—bug fixes, documentation, security hardening, and features alike.

---

### 2) Communication & Issue Rules

#### Issues
Please open an issue for:
- Bugs
- Feature requests
- Documentation/UX improvements
- Non-confidential hardening topics

**Do NOT report publicly:**
- Security vulnerabilities with potential exploitation → see [SECURITY](SECURITY.md)

**Issue quality (expected):**
- clear problem/goal statement
- reproducible steps (for bugs)
- environment: OS, Python, browser (UI), deployment details
- logs/screenshots (redacted; no sensitive data)

---

### 3) Development Setup (recommended)

**Requirements**
- Python 3.11+ (or project-specific)
- pip / venv
- Optional: Docker (reproducible builds/deployments)

**Setup (example)**
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

**Run (example)**
```bash
uvicorn app.main:app --reload
```

> Note: Adjust the command to the repository README and the actual entry points.

---

### 4) Branching Strategy

Recommended:
- `main`: stable, release-ready
- `feature/<short-description>`: new features
- `fix/<short-description>`: bug fixes
- `docs/<short-description>`: documentation changes
- `chore/<short-description>`: maintenance/refactor

Please open pull requests **against `main`**, unless stated otherwise.

---

### 5) Commit Convention (recommended)

Use meaningful commit messages. Optionally follow Conventional Commits:

- `feat:` new functionality
- `fix:` bug fix
- `docs:` documentation
- `refactor:` refactor without feature change
- `test:` tests
- `chore:` maintenance

**Examples**
- `feat: add severity filter to findings view`
- `fix: prevent zip-slip in extractor`
- `docs: update deployment instructions`

---

### 6) Code Style & Quality Rules

**General**
- never commit secrets (keys/passwords/tokens)
- no unsafe defaults in production paths
- clear error handling (exceptions, HTTP responses)
- never log sensitive data

**Python**
- consistent types/signatures
- clear module boundaries (API / analysis / storage / ui)
- prefer `black`/`ruff`/`isort` if used in the project

**Frontend**
- no inline secrets
- I18N: add new strings in both DE/EN
- robust error handling for API calls

---

### 7) Tests & Quality Assurance

Contributions should:
- not break existing tests
- include new tests where appropriate
- run reproducibly (locally and in CI)

Recommended:
- unit tests for scanner/analysis logic
- integration tests for API endpoints
- regression tests for fixed bugs

If your PR intentionally has no tests (e.g., docs-only), mention it in the PR description.

---

### 8) Security & Privacy Rules

- Do not include real production data in repro dumps/issues
- Always redact tokens/session IDs/keys
- For ZIP/uploads: enforce traversal protections, size limits, safe extraction
- With SQLAlchemy: use safe queries; avoid string concatenation

If you submit a security fix:
- describe impact + mitigation
- add regression tests where possible
- reference `SECURITY.md` if relevant

---

### 9) Pull Request Checklist

Please ensure your PR:
- [ ] references an issue (or clearly explains the problem)
- [ ] is focused (avoid “mega PRs”)
- [ ] follows the code style
- [ ] includes tests or explains why not
- [ ] contains no secrets or sensitive data
- [ ] updates documentation when needed
- [ ] includes DE/EN updates for UI/I18N where applicable

---

### 10) Review Process

We review:
- correctness and reproducibility
- security (validation, auth, data handling)
- performance (avoid unnecessary loops/scans)
- maintainability (clear module boundaries)
- documentation (if feature impact)

We may request changes. Please apply feedback in follow-up commits.

---

### 11) License & Rights

By contributing, you agree that your contribution can be published under the project license.  
If you reuse third-party code, ensure license compatibility and proper attribution.
