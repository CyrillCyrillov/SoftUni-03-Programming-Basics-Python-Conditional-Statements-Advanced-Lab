day_of_week = input()
if day_of_week == "Sunday" or day_of_week == "Saturday":
    print("Weekend")
elif day_of_week == "Monday" or  \
        day_of_week == "Tuesday" or  \
        day_of_week == "Wednesday" or  \
        day_of_week == "Thursday" or \
        day_of_week == "Friday":
    print("Working day")
else:
    print("Error")
