const translations = {
  de: {
    "app.title": "AI Enterprise Konfigurations- & Code Auditor",

    "api.title": "API Zugriff",
    "api.desc": "Aktiver Development Token",

    "scan.title": "Projekt scannen",
    "scan.zip": "Projekt (ZIP)",
    "scan.profile": "Compliance-Profil",
    "scan.token": "API-Token",
    "scan.start": "Scan starten",

    "result.title": "Scan-Ergebnisse",
    "result.profile": "Profil",
    "result.level": "Risikostufe",
    "result.score": "Risiko-Score",
    "result.files": "Gescannt Dateien",
    "result.findings": "Detaillierte Findings",
    "result.none": "Keine Findings erkannt",

    "table.severity": "Schweregrad",
    "table.file": "Datei",
    "table.desc": "Beschreibung",

    "error.title": "Fehler",

    "info.title": "Über diese Anwendung",
    "info.text":
      "Dieses Tool dient der lokalen Analyse von Softwareprojekten im Hinblick auf Sicherheit, Konfiguration und Compliance.",
    "info.close": "Schließen",

    "lang.de": "DE",
    "lang.en": "EN",
    "github": "GitHub"
  },

  en: {
    "app.title": "AI Enterprise Configuration & Code Auditor",

    "api.title": "API Access",
    "api.desc": "Active development token",

    "scan.title": "Project scan",
    "scan.zip": "Project (ZIP)",
    "scan.profile": "Compliance profile",
    "scan.token": "API token",
    "scan.start": "Start scan",

    "result.title": "Scan results",
    "result.profile": "Profile",
    "result.level": "Risk level",
    "result.score": "Risk score",
    "result.files": "Files scanned",
    "result.findings": "Detailed findings",
    "result.none": "No findings detected",

    "table.severity": "Severity",
    "table.file": "File",
    "table.desc": "Description",

    "error.title": "Error",

    "info.title": "About this application",
    "info.text":
      "This tool performs local analysis of software projects with regard to security, configuration and compliance.",
    "info.close": "Close",

    "lang.de": "DE",
    "lang.en": "EN",
    "github": "GitHub"
  }
};

let currentLang = "en";

function setLanguage(lang) {
  currentLang = lang;
  document.documentElement.lang = lang;

  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (translations[lang][key]) {
      el.textContent = translations[lang][key];
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  setLanguage(currentLang);

  document.querySelectorAll(".lang-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      setLanguage(btn.dataset.lang);
    });
  });
});
