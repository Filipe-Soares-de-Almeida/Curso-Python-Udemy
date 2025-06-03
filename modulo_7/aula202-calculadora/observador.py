import time
import subprocess
from pathlib import Path

WATCHED_FILES = [
  "buttons.py",
  "display.py",
  "environment_constants.py",
  "info.py",
  "main.py",
  "main_window.py",
  "styles.py"
]
WATCHED_FILES = [Path(__file__).parent / f for f in WATCHED_FILES]
CHECK_INTERVAL = 1  # segundos
VENV_PATH = 'D:\\_Filipe\\Cursos\\Curso-Python-Udemy\\venv\\Scripts\\python.exe'

def get_all_mod_times(files):
  return {f: f.stat().st_mtime for f in files if f.exists()}

def main():
  for f in WATCHED_FILES:
    if not f.exists(): # type: ignore
      print(f"💥 Arquivo não encontrado: {f}")
      return

  print("👁️ Observando alterações nos arquivos...")
  mod_times = get_all_mod_times(WATCHED_FILES)
  main_file = [f for f in WATCHED_FILES if f.name == "main.py"][0] # type: ignore
  main_proc = subprocess.Popen([str(VENV_PATH), str(main_file)])
  print(f"🚀 main.py started! PID = {main_proc.pid}")

  while True:
    time.sleep(CHECK_INTERVAL)
    new_mod_times = get_all_mod_times(WATCHED_FILES)

    if new_mod_times != mod_times:
      print("🔁 Um arquivo python foi alterado! RELOADING!!! 💥")
      mod_times = new_mod_times

      if main_proc and main_proc.poll() is None:
        print(f"💣 finalizando main.py (PID {main_proc.pid})")
        main_proc.terminate()
        try:
          main_proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
          print("💀 main.py não respondeu a tempo, forçando finalização!")
          main_proc.kill()

        print("🔥 Iniciando!")
        main_proc = subprocess.Popen([str(VENV_PATH), str(main_file)])
        print(f"⚙️ Novo PID: {main_proc.pid}")

if __name__ == "__main__":
  main()
