from dateutil.relativedelta import relativedelta
from datetime import datetime

date1=datetime.strptime('1990-01-01','%Y-%m-%d')
date2=datetime.strptime('2024-09-16','%Y-%m-%d')

age_difference=relativedelta(date2,date1)
print(f"age_difference:{age_difference.years} Years ,{age_difference.months} Months ,{age_difference.days} Days.")