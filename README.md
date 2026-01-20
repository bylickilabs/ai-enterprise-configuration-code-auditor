# AI Enterprise Configuration & Code Auditor
**Author:** ©Thorsten  Bylicki
**Company:** ©BYLICKILABS  
**App ID / Name:** `ai-enterprise-configuration-code-auditor`  
**Version:** `1.0.0`  
**Date:** `01/20/2026` <br>
**Language:** `DE / EN` <br>
**README:** `DE / EN` <br>

<br>

| ![](assets/logo.png) |
|---|

---

### 1) Zweck & Mehrwert
Der **AI Enterprise Configuration & Code Auditor** ist eine **serverseitige** Analyse-Anwendung zur **Sicherheits-, Risiko- und Konfigurationsprüfung** von Software-Projekten, die als **ZIP-Archiv** hochgeladen werden.

Die Anwendung ist darauf ausgelegt, in einem **Enterprise-Workflow** zu funktionieren:
- nachvollziehbare Ergebnisse (Findings + Score)
- persistente Historie (SQLite via SQLAlchemy)
- klare Trennung der Schichten (UI / Scanner / Storage)
- Mehrsprachigkeit (DE/EN)

---

### 2) Features (Ist-Stand)
- **ZIP-Projekt-Scan** (Upload über Web-UI)
- **Risk Score** + **Risk Level** (LOW/MEDIUM/HIGH/CRITICAL)
- **Detailed Findings** (Datei, Severity, Message)
- **Scan-Historie** in SQLite (persistente Speicherung)
- **Mehrsprachigkeit** (DE/EN) über i18n
- **Server-Side Rendering** (FastAPI + Jinja2) – keine fragile SPA-HTML-Parsing-Logik

---

### 3) Architektur (High-Level)
**Server Side App (SSR):**
- **FastAPI**: Webserver + API-Endpunkte  
- **Jinja2**: UI-Templates (serverseitig gerendert)  
- **SQLAlchemy**: ORM für SQLite (später optional Postgres)  
- **Scanner-Modul**: Entpackt ZIP, analysiert Dateien, erzeugt strukturierte Findings  
- **Repository-Layer**: einzige Stelle für DB-Zugriffe (Write/Read)  

**Wichtig:** Die UI wird vom Server gerendert. JavaScript ergänzt nur UI-Interaktionen (Sprache, Modal etc.).

---

### 4) Projektstruktur
Beispielhafte Struktur (Soll-/Zielstruktur, kompatibel zu deinem Setup):

```text
ai-enterprise-auditor/
├─ app/
│  ├─ __init__.py
│  ├─ main.py              # FastAPI-Einstiegspunkt
│  ├─ config.py            # Anwendungs-Metadaten & Standardkonfiguration
│  └─ i18n.py              # Serverseitiger Übersetzungs-Helper (DE/EN)
│
├─ analysis/
│  ├─ __init__.py
│  └─ scanner.py           # Logik für ZIP-Analyse und Sicherheits-Scans
│
├─ storage/
│  ├─ __init__.py
│  ├─ db.py                # SQLAlchemy Engine, Session & Base
│  ├─ models.py            # ORM-Modelle (Benutzer, Scans, Findings, Audits)
│  └─ repository.py        # Persistenzschicht (save_scan, list_scans, …)
│
├─ ui/
│  ├─ templates/
│  │  └─ index.html        # Haupt-Dashboard (Server-Side Rendering)
│  └─ static/
│     ├─ css/style.css     # Zentrales Stylesheet
│     └─ js/
│        ├─ i18n.js        # Client-seitige Übersetzungen
│        └─ app.js         # Frontend-Logik & API-Anbindung
│
├─ data/
│  ├─ app.db               # SQLite-Datenbank (automatisch erzeugt)
│  └─ logs/                # Optionale Logdateien
│
├─ requirements.txt        # Python-Abhängigkeiten
└─ README.md               # Projektdokumentation
```

---

### 5) Requirements / Abhängigkeiten
Die Anwendung benötigt folgende Python-Pakete (siehe `requirements.txt`):
- `fastapi` – Web Framework
- `uvicorn[standard]` – ASGI Server
- `jinja2` – Template Engine
- `sqlalchemy` – ORM
- `python-multipart` – File Uploads via FormData (ZIP Upload)

---

### 6) Installation (Windows – empfohlen)
1. **Projektverzeichnis öffnen**
```powershell
cd C:\Users\ ... \Desktop\ai-enterprise-auditor
```

2. **Virtuelle Umgebung erstellen**
```powershell
python -m venv .venv
```

3. **VENV aktivieren**
```powershell
.venv\Scripts\activate
```

4. **Dependencies installieren**
```powershell
pip install -r requirements.txt
```

---

### 7) Installation (Linux/macOS)
```bash
cd ai-enterprise-auditor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### 8) Start / Ausführung
**Wichtig:** Immer aus dem Projekt-Root starten.

```powershell
python -m app.main
```

Du siehst dann typischerweise:
- `Uvicorn running on http://0.0.0.0:8000`

**Im Browser öffnen:**
```text
http://127.0.0.1:8000
```

---

### 9) Erster Scan (Web UI)
1. ZIP-Datei auswählen
2. Profil wählen (BASE / OWASP / CIS)
3. API Token (Dev-Mode):
```text
admin-dev-token
```
4. Scan starten → Ergebnis erscheint serverseitig gerendert

---

### 10) Datenbank (SQLite) – Erstellung / Reset
Die DB wird automatisch erzeugt, sobald `init_db()` beim App-Start ausgeführt wird.

**Pfad (Default):**
```text
data/app.db
```

**Reset (Dev-Phase):**
- App stoppen (`STRG + C`)
- DB löschen:
```powershell
Remove-Item data\app.db -ErrorAction SilentlyContinue
```
- App neu starten:
```powershell
python -m app.main
```

---

### 11) Konfiguration (env / Defaults)
Je nach `storage/db.py` kann die DB-URL über ENV gesetzt werden:

**Beispiel `.env` / Umgebungsvariable:**
```text
DB_URL=sqlite:///./data/app.db
```
Optional später:
```text
DB_URL=postgresql+psycopg2://user:pass@localhost:5432/auditor
```

---

### 12) Troubleshooting (häufige Probleme)
**A) `ModuleNotFoundError: fastapi`**
- VENV aktivieren
- Dependencies installieren:
```powershell
pip install -r requirements.txt
```

**B) `No module named 'app'`**
```powershell
python -m app.main
```

**C) JS/CSS wird nicht geladen**
- Prüfe Requests im Terminal (`GET /static/...`)
- Browser Cache hard reload:
  - `STRG + SHIFT + R`

**D) „File is not a zip file“**
- Stelle sicher, dass wirklich eine `.zip` hochgeladen wird

---

### 13) Roadmap (empfohlene nächste Schritte)
- Scan-Historie im UI (Liste + Detail)
- Severity Filter + Suche
- JSON Export + PDF Report
- Auth/Rollen-Model (Admin/Auditor/Viewer) produktiv aktivieren

---

### 14) Hinweis zur Hash-Stabilität bei GitHub-Repositories

Der für dieses Projekt angegebene Hashwert bleibt **ausschließlich dann identisch**, wenn das Repository **per `git clone`** bezogen wird.

Wird das Repository über die GitHub-Funktion **„Download ZIP“** heruntergeladen, erstellt GitHub automatisch ein neues Wurzelverzeichnis mit folgendem Schema:

```
<repository-name>-main
oder
<repository-name>_main
```

Der Zusatz `main` kennzeichnet den exportierten Standard-Branch und wird **automatisch durch GitHub** vergeben.  
Dabei ändert sich der ursprüngliche Name des Projekt-Root-Verzeichnisses.

### Technischer Hintergrund

- Der Root-Verzeichnisname ist Bestandteil des Dateipfads  
- Dateipfade fließen in rekursive Hash-Berechnungen ein  
- Eine Änderung des Root-Verzeichnisses führt zwangsläufig zu einem anderen Hashwert  
- Dieses Verhalten ist systembedingt und beabsichtigt  

### Empfehlung

Für eine reproduzierbare und verlässliche Hash-Verifikation:

- Repository per `git clone` beziehen, oder  
- Hashes ausschließlich über definierte Datei-Inhalte bzw. Manifeste prüfen  

ZIP-Downloads sollten nicht als Grundlage für Integritätsvergleiche verwendet werden.

<br>

---

<br>

### 1) Purpose & Business Value
The **AI Enterprise Configuration & Code Auditor** is a **server-side** application for **security, risk and configuration analysis** of software projects uploaded as **ZIP archives**.

Designed for **enterprise workflows**:
- traceable results (findings + score)
- persistent scan history (SQLite via SQLAlchemy)
- clean separation of layers (UI / scanner / storage)
- bilingual support (DE/EN)

---

### 2) Features (Current)
- **ZIP project scan** (web upload)
- **Risk score** + **risk level** (LOW/MEDIUM/HIGH/CRITICAL)
- **Detailed findings** (file, severity, message)
- **Scan history** stored in SQLite
- **Multi-language** (DE/EN)
- **Server-side rendering** (FastAPI + Jinja2) – no fragile HTML parsing SPA logic

---

### 3) Architecture (High-Level)
**Server-side rendering approach (SSR):**
- **FastAPI**: web server + endpoints
- **Jinja2**: templates rendered by server
- **SQLAlchemy**: ORM for SQLite (Postgres-ready later)
- **Scanner module**: unzip, analyze, produce structured findings
- **Repository layer**: single point of DB access (write/read)

---

### 4) Project Structure
```
ai-enterprise-auditor/
├─ app/
│  ├─ __init__.py
│  ├─ main.py              # FastAPI Entry Point
│  ├─ config.py            # App-Metadaten & Defaults
│  └─ i18n.py              # Server-side translations helper
│
├─ analysis/
│  ├─ __init__.py
│  └─ scanner.py           # ZIP scan logic
│
├─ storage/
│  ├─ __init__.py
│  ├─ db.py                # SQLAlchemy engine/session/base
│  ├─ models.py            # ORM models (users, scans, findings, audit)
│  └─ repository.py        # persistence layer (save_scan, list_scans, ...)
│
├─ ui/
│  ├─ templates/
│  │  └─ index.html         # main dashboard template (SSR)
│  └─ static/
│     ├─ css/style.css
│     └─ js/
│        ├─ i18n.js
│        └─ app.js
│
├─ data/
│  ├─ app.db               # SQLite DB (auto-generated)
│  └─ logs/                # optional logs
│
├─ requirements.txt
└─ README.md
```

---

### 5) Requirements / Dependencies
See `requirements.txt`:
- `fastapi`
- `uvicorn[standard]`
- `jinja2`
- `sqlalchemy`
- `python-multipart`

---

### 6) Install (Windows)
```powershell
cd C:\Users\ ... \Desktop\ai-enterprise-auditor
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

### 7) Install (Linux/macOS)
```bash
cd ai-enterprise-auditor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### 8) Run
Always start from project root:
```bash
python -m app.main
```

Open:
```text
http://127.0.0.1:8000
```

---

### 9) First Scan
1. Select ZIP file
2. Choose profile (BASE / OWASP / CIS)
3. Dev token:
```text
admin-dev-token
```
4. Start scan

---

### 10) Database (SQLite) – Create / Reset
DB is auto-created at:
```text
data/app.db
```

Reset (dev phase):
```bash
# stop server first (CTRL + C)
rm -f data/app.db
python -m app.main
```

---

### 11) Configuration (env / defaults)
Example env var:
```text
DB_URL=sqlite:///./data/app.db
```

---

### 12) Troubleshooting
**A) `ModuleNotFoundError: fastapi`**
```bash
pip install -r requirements.txt
```

**B) `No module named 'app'`**
```bash
python -m app.main
```

**C) Static files not loading**
Hard reload browser: `CTRL + SHIFT + R`

---

### 13) Roadmap (Recommended Next Steps)

- Scan history in the UI (list view + detail view)
- Severity filtering and search
- JSON export and PDF reporting
- Production activation of the authentication and role model (Admin / Auditor / Viewer)

---

### 14) Hash Stability for GitHub Repositories

The hash value documented for this project remains **identical only when the repository is obtained via `git clone`**.

When using GitHub’s **“Download ZIP”** function, GitHub automatically extracts the project into a new root directory following this pattern:

```
<repository-name>-main
or
<repository-name>_main
```

The `main` suffix represents the exported default branch and is **assigned automatically by GitHub**.  
As a result, the original root directory name is modified.

### Technical Background

- The root directory name is part of the file path  
- File paths are included in recursive hash calculations  
- Changing the root directory inevitably results in a different hash value  
- This behavior is intentional and expected  

### Recommendation

For reliable and reproducible hash verification:

- Obtain the repository via `git clone`, or  
- Validate hashes based solely on defined file contents or manifest files  

ZIP downloads should not be used as a basis for integrity validation.

---

## License
BYLICKILABS – Internal / Enterprise Usage
[LICENSE](LICENSE)
