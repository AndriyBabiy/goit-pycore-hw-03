from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

def get_upcoming_birthdays(users): 
  today = datetime.now().date()
  one_week_after_today = today + timedelta(days=7)
  print(today, one_week_after_today)

  users_w_birthdays_soon = []

  def get_celebration_date_datetime(date):
    return datetime.strptime(date, "%Y.%m.%d")

  for user in users:
    user_temp = {
      'name': user["name"]
    }

    if one_week_after_today.year == today.year:
      user_temp["congratulation_date"] = get_celebration_date_datetime(user['birthday']).replace(year=today.year).date()
    else:
      user_temp["congratulation_date"] = get_celebration_date_datetime(user['birthday']).replace(year=today.year + 1).date()
    
    birthday_weekday = user_temp["congratulation_date"].weekday()

    if birthday_weekday == 5:
      user_temp["congratulation_date"] + timedelta(days=2)
    elif birthday_weekday == 6:
      user_temp["congratulation_date"] + timedelta(days=1)
    

    if user_temp["congratulation_date"] >= today and user_temp["congratulation_date"] < one_week_after_today:
      user_temp["congratulation_date"] = datetime.strftime(user_temp["congratulation_date"], "%Y.%m.%d")
      users_w_birthdays_soon.append(user_temp)

  return users_w_birthdays_soon

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": fake.name(), "birthday": "1990.02.27"},
    {"name": fake.name(), "birthday": "1990.03.02"},
    {"name": fake.name(), "birthday": "1990.03.09"},
    {"name": fake.name(), "birthday": "1990.03.27"},
    {"name": fake.name(), "birthday": "1990.01.03"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)