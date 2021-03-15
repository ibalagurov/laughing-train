import re
from src.calendar import date_to_gregorian


if __name__ == "__main__":
    print(
        "Welcome to Gregorian calendar date checker!\n"
        "Enter a date in format 'day.month.year' to check it "
        "(years from 1 to 9999 are supported).\n"
        "To exit type 'exit'.\n"
    )
    while True:
        string = input().strip().lower().replace(" ", "").replace("_", "")
        if string == "exit":
            print("Bye!")
            break

        match = re.match(r"^(\d+)\.(\d+)\.(-?\d+)$", string=string)

        if not match:
            print("Invalid format, try one more time\n")
            continue

        day, month, year = map(int, match.groups())
        result = date_to_gregorian(day=day, month=month, year=year)

        if not result.supported:
            print("Unsupported year. Enter year from 1 to 9999\n")
            continue

        print("Yes" if result.correct else "No", "\n")
