import re
from src.calendar import date_to_gregorian


if __name__ == "__main__":
    print(
        "Enter date in format 'day.month.year', to check is it correct gregorian date.\n"
        "To exit type 'exit'\n"
    )
    while True:
        string = input().strip().lower()
        if string == "exit":
            print("Bye!")
            break

        match = re.match(r"(-?\d+)\.(-?\d+)\.(-?\d+)", string=string)

        if not match:
            print("Invalid format, try one more time\n")
            continue

        day, month, year = map(int, match.groups())
        result = date_to_gregorian(year=year, month=month, day=day)

        if not result.supported:
            print("Unsupported year. Enter year from 1 to 9999\n")
            continue

        print("Yes" if result.correct else "No", "\n")
