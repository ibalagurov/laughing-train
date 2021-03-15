from typing import NamedTuple, Optional

from datetime import datetime


class GregorianDate(NamedTuple):
    supported: bool
    correct: Optional[bool] = None


def date_to_gregorian(day: int, month: int, year: int) -> GregorianDate:
    """
    Check is date correct in terms of gregorian calendar.

    It supports years from 1 to 9999
    """
    if 1 > year or year > 9999:
        return GregorianDate(supported=False)

    try:
        datetime.strptime(f"{year:04d}-{month}-{day}", "%Y-%m-%d")
    except ValueError:
        # ValeError raises for wrong dates:
        # - 0 or less or 32 and more days value and etc.
        # - 0 or less or 13 and more month value and etc.
        # - nonexistent dates like 31th April
        # - 29th February if year isn't leap
        return GregorianDate(supported=True, correct=False)
    return GregorianDate(supported=True, correct=True)
