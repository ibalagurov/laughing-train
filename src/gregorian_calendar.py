from typing import NamedTuple, Optional

from datetime import datetime


class Result(NamedTuple):
    supported: bool
    correct: Optional[bool] = None


def is_correct_date(year: int, month: int, day: int) -> Result:
    """
    Check is date correct in terms of gregorian calendar.

    It supports years from 1 to 9999
    """
    if 1 > year or year > 9999:
        return Result(supported=False)

    try:
        datetime.strptime(f"{year:04d}-{month}-{day}", "%Y-%m-%d")
    except ValueError:
        # ValeError raises for wrong dates:
        # - 0 or less or 32 and more days value and etc.
        # - 0 or less or 13 and more month value and etc.
        # - nonexistent dates like 31th April
        # - 29th February if year isn't leap
        return Result(supported=True, correct=False)
    return Result(supported=True, correct=True)
