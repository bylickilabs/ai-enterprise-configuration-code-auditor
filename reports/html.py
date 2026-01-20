from datetime import datetime
from app.config import APP_TITLE, APP_VERSION, APP_COMPANY
from app.i18n import t
from reports.signer import sign_report

def generate_html(scan_result: dict, lang: str) -> str:
    payload = {
        "risk": scan_result["risk_level"],
        "score": scan_result["score"],
        "findings": scan_result["findings"]
    }
    signature = sign_report(payload)

    rows = ""
    for f in scan_result["findings"]:
        rows += f"""
        <tr>
            <td>{f['category']}</td>
            <td>{f['severity']}</td>
            <td>{f['file']}</td>
            <td>{f['message']}</td>
        </tr>
        """

    return f"""
<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{APP_TITLE[lang]}</title>
<style>
body {{
  background:#0b0f1a;
  color:#d8faff;
  font-family:Segoe UI, sans-serif;
}}
table {{
  width:100%;
  border-collapse:collapse;
}}
th, td {{
  border:1px solid #1f2a3a;
  padding:8px;
}}
th {{
  background:#142033;
}}
</style>
</head>
<body>

<h1>{APP_TITLE[lang]}</h1>
<p>{APP_COMPANY} · v{APP_VERSION}</p>
<p>{t(lang,'risk_score')}: <strong>{scan_result['score']}</strong> ({t(lang,'risk_'+scan_result['risk_level'].lower())})</p>
<p>{datetime.utcnow().isoformat()} UTC</p>

<h2>Findings</h2>
<table>
<tr>
  <th>Category</th>
  <th>Severity</th>
  <th>File</th>
  <th>Description</th>
</tr>
{rows}
</table>

<hr>
<p>{t(lang,'report_signed')}</p>
<code>{signature}</code>

</body>
</html>
"""
