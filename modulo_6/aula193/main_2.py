# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# edge Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o edgedriver está
EDGE_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'


def make_edge_browser(*options: str) -> webdriver.Edge:
  edge_options = webdriver.EdgeOptions()

  # edge_options.add_argument('--headless')
  if options is not None:
    for option in options:
      edge_options.add_argument(option)

  edge_service = Service(
      executable_path=str(EDGE_DRIVER_PATH),
  )

  _browser = webdriver.Edge(
      service=edge_service,
      options=edge_options
  )

  return _browser


if __name__ == '__main__':
  TIME_TO_WAIT = 10

  # Example
  # options = '--headless', '--disable-gpu',
  _options = ()
  browser = make_edge_browser(*_options)

  # Como antes
  browser.get('https://www.google.com')

  # Espere para encontrar o input
  search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
      EC.presence_of_element_located(
          (By.NAME, 'q')
      )
  )
  search_input.send_keys('Hello World!')

  # Dorme por 10 segundos
  sleep(TIME_TO_WAIT)
