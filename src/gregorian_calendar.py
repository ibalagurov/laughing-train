from datetime import datetime


def is_correct_date(year: int, month: int, day: int) -> bool:
    """
    Check is date correct in terms of gregorian calendar.

    It supports years from 1 to 9999
    """
    if 0 > year > 9999:
        raise ValueError(
            f"Unsupported year value: '{year}'. It should be in a range from 1 to 9999"
        )

    try:
        datetime.strptime(f"{year:04d}-{month}-{day}", "%Y-%m-%d")
    except ValueError:
        # ValeError raises for wrong dates:
        # - 0 or less or 32 and more days value and etc.
        # - 0 or less or 13 and more month value and etc.
        # - nonexistent dates like 31th April
        # - 29th February if year isn't leap
        return False
    return True
