#!/bin/bash
# ATP Intelligence – magyar privát labor indítása macOS/Linux alatt.
# A GitHub fájl alaphelyzetben lehet nem futtatható: egyszeri "chmod +x START_ATP_LAB.command".
set -e
cd "$(dirname "$0")"

if ! command -v python3 >/dev/null 2>&1; then
  echo "HIBA: Python 3 nincs telepítve. Python 3.10 vagy újabb szükséges."
  read -r -p "Enter a bezáráshoz..." _
  exit 1
fi

if ! python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)"; then
  echo "HIBA: A Python legalább 3.10-es verziója szükséges."
  read -r -p "Enter a bezáráshoz..." _
  exit 1
fi

if [ ! -f ".venv/bin/python" ]; then
  echo "Első indítás: helyi Python-környezet létrehozása..."
  python3 -m venv .venv
fi

if ! .venv/bin/python -c "import streamlit" >/dev/null 2>&1; then
  echo "Első indítás: szükséges Python-csomagok telepítése..."
  .venv/bin/python -m pip install -r requirements.txt
fi

echo ""
echo "=============================================="
echo " ATP INTELLIGENCE – MAGYAR PRIVÁT LAB"
echo "=============================================="
echo "Helyi labor indul. Az API-kulcs nélkül is működik a játékosprofil és B0."
echo "Leállítás: a Terminálban CTRL+C."
echo ""
exec .venv/bin/python -m streamlit run atp_lab.py
