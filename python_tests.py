from datetime import datetime
import sys

def getdayofweek(date=None):
    return date.weekday()

if __name__ == "__main__":
    day= getdayofweek(datetime.now())
    print(day)
    days_of_week = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday")
    )

    Actual_day = (days_of_week[day][1])

    if Actual_day == "Friday":
        print ("Today is a Friday do not make code changes even in dev")
        sys.exit(1)
    else:
        print("Not a Fridy go ahead and merge")
        sys.exit(0)

