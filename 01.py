from datetime import datetime

def get_days_from_today(date):
  today = datetime.today().date()
  difference = date.toordinal() - today.toordinal()
  print(f"{difference} days")
  return(f"{difference} days")

def dateInput(): 
  return input("Please insert a date in the format (YYYY-MM-DD) >>> ")
dateFormat = "%Y-%m-%d"

while True:
  try:
    date = datetime.strptime(dateInput(), dateFormat).date()
    get_days_from_today(date)
    break
  except Exception as e:
    print("Error: Please input date in the format YYYY-MM-DD")