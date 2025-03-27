# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
EDGE_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'


def make_egdge_browser(*options: str) -> webdriver.Edge:
  edge_options = webdriver.EdgeOptions()

  # chrome_options.add_argument('--headless')
  if options is not None:
    for option in options:
      edge_options.add_argument(option)  # type: ignore

  edge_service = Service(
      executable_path=str(EDGE_DRIVER_PATH),
  )

  _browser = webdriver.Edge(
      service=edge_service,
      options=edge_options,
  )

  return _browser


if __name__ == '__main__':
  # Example
  # options = '--headless', '--disable-gpu',
  _options = ()
  browser = make_egdge_browser(*_options)

  # Como antes
  browser.get('https://www.google.com')

  # Dorme por 10 segundos
  sleep(10)
