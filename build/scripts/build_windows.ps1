python -m venv .venv
. .venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

pyinstaller build\spec\auditor.spec --clean

Write-Host "✔ Windows Binary erstellt"
