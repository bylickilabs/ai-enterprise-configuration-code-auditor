# SECURITY POLICY / SICHERHEITSRICHTLINIE

This project takes security seriously. Please follow the responsible disclosure process below.  
Dieses Projekt nimmt Sicherheit ernst. Bitte nutze den Responsible-Disclosure-Prozess unten.

---

### 1) Supported Versions (Unterstützte Versionen)

Wir empfehlen, stets die **neueste Release-Version** zu verwenden. Sicherheitsfixes werden priorisiert veröffentlicht.

| Version | Support-Status |
|--------:|----------------|
| Latest (aktuelles Release) | ✅ Supported |
| Older Releases | ⚠️ Best effort (nach Möglichkeit) |
| Unreleased / Forks | ❌ Not supported |

> Hinweis: Wenn du eine Schwachstelle in einer älteren Version meldest, gib bitte an, ob die Schwachstelle auch im aktuellen Release reproduzierbar ist.

---

### 2) Verantwortungsvolle Meldung (Responsible Disclosure)

Bitte **veröffentliche keine Sicherheitslücken öffentlich**, bevor wir reagiert und ggf. einen Fix bereitgestellt haben.

**Bevorzugter Kontaktweg**
- Erstelle **keinen öffentlichen GitHub-Issue** für Sicherheitslücken.
- Nutze stattdessen einen privaten Meldeweg (z. B. GitHub Security Advisories / private Kommunikation).

**Wenn GitHub Security Advisories aktiviert sind**
- Nutze: *Security → Advisories → “Report a vulnerability”*

**Wenn kein privater Kanal verfügbar ist**
- Sende eine vertrauliche Meldung an das zuständige Projekt-/Security-Team (sofern in der Projektbeschreibung angegeben).

---

### 3) Was wir benötigen (Meldungsinhalt)

Bitte liefere so viele Details wie möglich, damit wir reproduzieren und priorisieren können:

**Pflichtangaben**
- Betroffene Version(en) und Umgebung (OS, Python-Version, Deployment-Setup)
- Reproduzierbare Schritte (PoC/Minimalbeispiel)
- Erwartetes Verhalten vs. tatsächliches Verhalten
- Auswirkung / Impact (z. B. Datenabfluss, RCE, Auth-Bypass)
- Logs / Screenshots (falls hilfreich, bitte ohne sensible Daten)

**Optional (hilft sehr)**
- CVSS-Einschätzung (Base Score) oder eine grobe Schweregrad-Einordnung
- Vorschlag für Fix/Mitigation
- Hinweise zu Workarounds

---

### 4) Schweregrade & Priorisierung

Wir priorisieren nach **Impact** und **Ausnutzbarkeit**:

- **Kritisch (Critical):** RCE, Auth-Bypass mit Admin-Rechten, kompletter Datenabfluss
- **Hoch (High):** Privilege Escalation, Token/Session-Leak, SQLi mit Datenzugriff
- **Mittel (Medium):** DoS, Information Disclosure ohne direkte Ausnutzung
- **Niedrig (Low):** geringe Auswirkung, schwer ausnutzbar, Hardening-Themen

---

### 5) Reaktionszeiten (Ziel-SLAs)

Wir bemühen uns um folgende Zielzeiten (Best Effort):

- **Bestätigung des Eingangs:** innerhalb von 72 Stunden
- **Erste technische Einschätzung:** innerhalb von 7 Tagen
- **Fix/Release-Plan:** abhängig von Schweregrad und Reproduzierbarkeit

> Hinweis: Bei kritischen Lücken kann der Prozess deutlich beschleunigt werden.

---

### 6) Koordinierte Offenlegung

Wir streben eine **koordinierte Offenlegung** an:

1. Eingang bestätigen
2. Reproduktion & Analyse
3. Fix entwickeln + Tests
4. Release mit Security Notes
5. (Optional) CVE-Antrag/Advisory-Veröffentlichung

Wenn du eine Offenlegung planst, stimme bitte den Zeitpunkt mit uns ab.

---

### 7) Umgang mit sensiblen Daten

Bitte sende **keine echten Zugangsdaten**, Produktionsdaten oder personenbezogene Daten.  
Wenn du Logs teilst, anonymisiere/zensiere bitte Tokens, Session-IDs, E-Mails etc.

---

### 8) Sichere Entwicklungs- und Betriebspraktiken (Empfehlungen)

**Für Maintainer**
- Abhängigkeiten regelmäßig aktualisieren (Dependabot/renovate)
- SAST/DAST nach Möglichkeit in CI integrieren (z. B. CodeQL)
- Secrets niemals im Repo speichern (nutze Vault/CI Secrets)

**Für Betreiber**
- TLS/HTTPS erzwingen, Reverse Proxy sauber konfigurieren
- Minimalrechte für Service-Accounts / DB-Zugriff
- Regelmäßige Backups + Restore-Tests
- Logging/Monitoring aktivieren (Fehler, Auth, Rate-Limits)
- Updates zeitnah einspielen

---

### 9) Sicherheitsrelevante Konfiguration (Projekt-spezifisch)

Typische Risikofelder (je nach Projekt-Konfiguration):
- Auth/Rollenmodell (Admin/Auditor/Viewer): **Least Privilege** sicherstellen
- Upload/ZIP-Handling: Limits (Größe/Typ), Pfad-Traversal-Schutz, sichere Extraktion
- Reporting/Export (JSON/PDF): Output Encoding, Template-Hardening
- Datenhaltung (SQLite/SQLAlchemy): sichere Queries, Migrations, Backup-Strategie

---

### 10) Anerkennung (Credits)

Wenn du möchtest, nennen wir dich im Advisory/Release Notes als Finder (Name/Handle).  
Bitte gib in deiner Meldung an, wie du genannt werden möchtest.

<br>

---

<br>

### 1) Supported Versions

We recommend using the **latest released version**. Security fixes are prioritized.

| Version | Support Status |
|--------:|----------------|
| Latest Release | ✅ Supported |
| Older Releases | ⚠️ Best effort |
| Unreleased / Forks | ❌ Not supported |

> Note: If you report an issue in an older version, please indicate whether it is reproducible on the latest release.

---

### 2) Responsible Disclosure

Please **do not publicly disclose vulnerabilities** before we have responded and, where possible, provided a fix.

**Preferred reporting**
- Do **not** open a public GitHub issue for security reports.
- Use a private reporting channel (e.g., GitHub Security Advisories / private communication).

**If GitHub Security Advisories are enabled**
- Use: *Security → Advisories → “Report a vulnerability”*

**If no private channel is available**
- Send a confidential report to the project/security contact (if provided in the repository/project description).

---

### 3) What to Include in Your Report

Please provide enough information to reproduce and prioritize the issue:

**Required**
- Affected version(s) and environment (OS, Python version, deployment details)
- Repro steps (PoC/minimal example)
- Expected vs. actual behavior
- Impact (e.g., data exposure, RCE, auth bypass)
- Logs/screenshots (redacted; avoid sensitive data)

**Optional (very helpful)**
- CVSS estimate (base score) or severity suggestion
- Proposed fix/mitigation ideas
- Workarounds

---

### 4) Severity & Prioritization

We prioritize based on **impact** and **exploitability**:

- **Critical:** RCE, admin-level auth bypass, full data exfiltration
- **High:** privilege escalation, token/session leakage, SQLi with data access
- **Medium:** DoS, limited info disclosure
- **Low:** low impact, hard to exploit, hardening recommendations

---

### 5) Response Targets (Best Effort SLAs)

We aim for the following targets:

- **Acknowledgement:** within 72 hours
- **Initial assessment:** within 7 days
- **Fix/release plan:** depends on severity and reproducibility

> Note: Critical issues may be handled on an accelerated timeline.

---

### 6) Coordinated Disclosure

We aim for **coordinated disclosure**:

1. Acknowledge receipt
2. Reproduce & analyze
3. Develop fix + tests
4. Release with security notes
5. (Optional) Publish advisory / request CVE

If you plan to disclose, please coordinate timing with us.

---

### 7) Handling Sensitive Data

Please do **not** send real credentials, production data, or personal data.  
Redact tokens, session IDs, emails, and any secrets from logs.

---

### 8) Secure Development & Operations Recommendations

**For maintainers**
- Keep dependencies updated (Dependabot/Renovate)
- Integrate SAST/DAST where feasible (e.g., CodeQL)
- Never commit secrets (use vaults/CI secrets)

**For operators**
- Enforce TLS/HTTPS; configure reverse proxy securely
- Apply least privilege for service accounts and DB access
- Regular backups + restore tests
- Enable logging/monitoring (errors, auth, rate limits)
- Patch/upgrade promptly

---

### 9) Security-Relevant Configuration (Project-Specific)

Common risk areas depending on configuration:
- Auth/role model (Admin/Auditor/Viewer): ensure **least privilege**
- Upload/ZIP handling: size/type limits, path traversal protections, safe extraction
- Reporting/exports (JSON/PDF): output encoding, template hardening
- Persistence (SQLite/SQLAlchemy): secure queries, migrations, backup strategy

---

### 10) Credits

If you want, we can credit you in advisories/release notes (name/handle).  
Please include your preferred attribution in your report.
