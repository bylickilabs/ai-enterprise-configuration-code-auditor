document.addEventListener("DOMContentLoaded", () => {

  const $ = (id) => document.getElementById(id);
  const $$ = (sel) => document.querySelectorAll(sel);

  const langButtons = $$(".lang-btn");

  if (langButtons.length > 0) {
    langButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        const lang = btn.dataset.lang;
        if (!lang) return;

        document.documentElement.lang = lang;

        try {
          localStorage.setItem("lang", lang);
        } catch {}

        if (window.setLanguage) {
          window.setLanguage(lang);
        }
      });
    });
  }

  try {
    const storedLang = localStorage.getItem("lang");
    if (storedLang && window.setLanguage) {
      document.documentElement.lang = storedLang;
      window.setLanguage(storedLang);
    }
  } catch {}

  const infoBtn   = $("infoBtn");
  const infoModal = $("infoModal");
  const closeInfo = $("closeInfo");

  if (infoBtn && infoModal) {
    infoBtn.addEventListener("click", () => {
      infoModal.classList.remove("hidden");
    });
  }

  if (closeInfo && infoModal) {
    closeInfo.addEventListener("click", () => {
      infoModal.classList.add("hidden");
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && infoModal) {
      infoModal.classList.add("hidden");
    }
  });

  const navButtons = $$(".nav");

  if (navButtons.length > 0) {
    navButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        const view = btn.dataset.view;
        if (!view) return;

        navButtons.forEach(n => n.classList.remove("active"));
        btn.classList.add("active");

        $$(".view").forEach(v => v.classList.remove("active"));
        const target = $("view-" + view);
        if (target) target.classList.add("active");
      });
    });
  }

  const scanForm = $("scanForm");
  const zipInput = $("zipFile");

  if (scanForm) {
    scanForm.addEventListener("submit", (e) => {
      if (!zipInput || !zipInput.files || zipInput.files.length === 0) {
        e.preventDefault();
        alert("Bitte eine ZIP-Datei auswählen.");
        return;
      }

      scanForm.classList.add("loading");
    });
  }

  const searchInput = $("search");
  const findingsTable = document.querySelector("table");

  if (searchInput && findingsTable) {
    searchInput.addEventListener("input", () => {
      const query = searchInput.value.toLowerCase();

      findingsTable.querySelectorAll("tbody tr").forEach(row => {
        row.style.display = row.textContent.toLowerCase().includes(query)
          ? ""
          : "none";
      });
    });
  }

  const severityFilter = $("severityFilter");

  if (severityFilter && findingsTable) {
    severityFilter.addEventListener("change", () => {
      const level = severityFilter.value;

      findingsTable.querySelectorAll("tbody tr").forEach(row => {
        const severityCell = row.querySelector("td");
        if (!severityCell) return;

        row.style.display =
          level === "ALL" || severityCell.textContent === level
            ? ""
            : "none";
      });
    });
  }

});