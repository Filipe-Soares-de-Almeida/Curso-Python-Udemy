import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(string: str) -> bool:
  return bool(NUM_OR_DOT_REGEX.search(string))


def isEmpty(string: str) -> bool:
  return len(string) == 0

def isValidNumber(string: str) -> bool:
  valid = False
  try:
    float(string)
    valid = True
  except ValueError:
    ...
  return valid

def convertToNumber(string: str) -> float | int: 
  number = float(string) 

  if number.is_integer():
    number = int(number)

  return number