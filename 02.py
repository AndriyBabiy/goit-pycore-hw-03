import random

def get_numbers_ticket(min, max, quantity):
  if (min < 1 or max > 1000 or (min > quantity > max)):
    print("""Error: Please enter valid inputs.
get_numbers_ticket(min, max, quantity)
  min > 1
  max < 1000
  min < quanitiy < max
    """)
    return []

  set = list(range(min, max))
  result = random.sample(set, k=quantity)

  result.sort()
  return result

def promptInput(field):
  return input(f"Value for {field}: ")

while True:
  try:
    min = int(promptInput("min"))
    max = int(promptInput("max"))
    quantity = int(promptInput("quantity"))
    
    print(get_numbers_ticket(min, max, quantity))
    break
  except Exception as e:
    print(e)
    print()