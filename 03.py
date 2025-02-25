import re

def normalize_phone(phone_number):
  input_pattern = r"[^\d\+]"
  pattern = ""
  nums_extraction = re.sub(input_pattern, pattern, phone_number)

  if re.search(r'\+380', nums_extraction):
    return nums_extraction
  elif re.search(r'.{12}', nums_extraction):
    if re.search(r'38', re.findall(r'38' ,nums_extraction)[0]):
      return f"+{nums_extraction}"
  elif re.search(r'.{10}', nums_extraction):
    if re.search(r'0', re.findall(r'0' ,nums_extraction)[0]):
      return f"+38{nums_extraction}"
  else:
    return f"+380{nums_extraction}"



raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

correct_nums = ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']

normalized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Normalized numbers: \n", normalized_numbers)

print("SUCCESS") if normalized_numbers == correct_nums else print("INCORRECT")