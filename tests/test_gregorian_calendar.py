"""
Tests for checking gregorian calendar date.

Astronomical year contains 365,2425 days:
365 for usual year and 366 for leap

Leap years:
0.2425 is 97 / 400 or 1/4 - 1/100 + 1/400

It means:
- each 4th year is leap, except 3 of 4 round dates
- 2004, 2008, 2012 and etc are leap
- 2000, 2400, 2800 and etc. is leap
- 2100, 2200, 2300, 2500, 2600, 2700, 2900 and etc. are NOT leap
- for 400 years 97 are leap
"""
import pytest

from src.calendar import date_to_gregorian, GregorianDate


@pytest.mark.parametrize(
    "day, month, year",
    [
        pytest.param(1, 1, 1, id="Minimum supported date"),
        pytest.param(31, 12, 9999, id="Maximum supported date"),
        pytest.param(29, 2, 4, id="First supported usual 4th leap year"),
        pytest.param(29, 2, 2020, id="Usual 4th leap year"),
        pytest.param(29, 2, 9996, id="Last supported usual 4th leap year"),
        pytest.param(29, 2, 400, id="First supported round leap year"),
        pytest.param(29, 2, 2000, id="Usual round leap year"),
        pytest.param(29, 2, 9600, id="Last supported round leap year"),
    ],
)
def test_correct_date_format(day, month, year):
    """Check correct date"""
    result: GregorianDate = date_to_gregorian(day=day, month=month, year=year)
    assert (
        result.correct
    ), f"Correct date '{day}-{month}-{year}'(day-month-year) is recognized as incorrect"


def test_400_years_contain_97_leap_years():
    """Check property of count leap years for 400 consecutive years"""
    start_year = 2000
    leap_years = [
        year
        for year in range(start_year, start_year + 400)
        if date_to_gregorian(year=year, month=2, day=29).correct
    ]
    actual_count = len(leap_years)
    expected_count = 97
    assert actual_count == expected_count, (
        f"For 400 consecutive years '{expected_count}' should be leap. "
        f"But actual count: '{actual_count}'. "
        f"Years, recognized as leap:\n{leap_years}"
    )


@pytest.mark.parametrize(
    "day, month, year",
    [
        # 29th february for not leap years
        pytest.param(29, 2, 1, id="First supported usual year"),
        pytest.param(29, 2, 2021, id="Usual year"),
        pytest.param(29, 2, 9999, id="Last supported usual year"),
        pytest.param(29, 2, 100, id="First supported round usual year"),
        pytest.param(29, 2, 2100, id="Usual round year"),
        pytest.param(29, 2, 9900, id="Last supported round usual year"),
        # day format
        pytest.param(32, 1, 1900, id="Nonexistent 32th day"),
        pytest.param(31, 4, 1900, id="Nonexistent 31th day"),
        pytest.param(0, 1, 1900, id="Nonexistent 0th day"),
        pytest.param(-1, 1, 1900, id="Negative day"),
        # month format
        pytest.param(1, 0, 1900, id="Nonexistent 0th day"),
        pytest.param(1, 13, 1900, id="Nonexistent 13th month"),
        pytest.param(1, -1, 1900, id="Negative month"),
    ],
)
def test_incorrect_date_format(day, month, year):
    """Check incorrect date"""
    result: GregorianDate = date_to_gregorian(day=day, month=month, year=year)
    assert (
        not result.correct
    ), f"Incorrect date '{day}-{month}-{year}'(day-month-year) is recognized as correct"


@pytest.mark.parametrize(
    "day, month, year",
    [
        pytest.param(31, 1, 0, id="Unsupported bottom boundary year"),
        pytest.param(1, 1, 10_000, id="Unsupported top boundary year"),
        pytest.param(31, 1, -1, id="Negative year"),
    ],
)
def test_unsupported_date_format(day, month, year):
    """Check unsupported date"""
    result: GregorianDate = date_to_gregorian(day=day, month=month, year=year)
    assert (
        not result.supported
    ), f"Unsupported date '{day}-{month}-{year}'(day-month-year) is recognized as supported"
