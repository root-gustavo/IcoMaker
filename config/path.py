import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Caminho base: exe ou script Python
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS)  # pasta temporária do PyInstaller
else:
    BASE_DIR = Path(__file__).resolve().parent.parent  # dois níveis acima de run.py

# Carrega .env (somente no script Python, não no exe)
env_path = BASE_DIR / "path.env"
if env_path.exists() and not getattr(sys, 'frozen', False):
    load_dotenv(dotenv_path=env_path)

# USER: pega variável de ambiente ou fallback
user_env = os.getenv("USER")
USER = Path(os.path.expandvars(user_env)) if user_env else Path.home() / "Downloads"