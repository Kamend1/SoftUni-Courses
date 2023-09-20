number_pages = int(input())
pages_hour = int(input())
number_days = int(input())

hours_read = number_pages // pages_hour
hours_day = hours_read // number_days

print(round(hours_day))
print(hours_day)
print(int(hours_day))
#различни опции, като съм сложил целочислено деление в редове 5 и 6