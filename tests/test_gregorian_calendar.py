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
    "year, month, day",
    [
        pytest.param(1, 1, 1, id="Minimum supported date"),
        pytest.param(9999, 12, 31, id="Maximum supported date"),
        pytest.param(4, 2, 29, id="First supported usual 4th leap year"),
        pytest.param(2020, 2, 29, id="Usual 4th leap year"),
        pytest.param(9996, 2, 29, id="Last supported usual 4th leap year"),
        pytest.param(400, 2, 29, id="First supported round leap year"),
        pytest.param(2000, 2, 29, id="Usual round leap year"),
        pytest.param(9600, 2, 29, id="Last supported round leap year"),
    ],
)
def test_correct_date_format(year, month, day):
    """Check correct date"""
    result: GregorianDate = date_to_gregorian(year=year, month=month, day=day)
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
    "year, month, day",
    [
        # 29th february for not leap years
        pytest.param(1, 2, 29, id="First supported usual year"),
        pytest.param(2021, 2, 29, id="Usual year"),
        pytest.param(9999, 2, 29, id="Last supported usual year"),
        pytest.param(100, 2, 29, id="First supported round usual year"),
        pytest.param(2100, 2, 29, id="Usual round year"),
        pytest.param(9900, 2, 29, id="Last supported round usual year"),
        # day format
        pytest.param(1900, 1, 32, id="Nonexistent 32th day"),
        pytest.param(1900, 4, 31, id="Nonexistent 31th day"),
        pytest.param(1900, 1, 0, id="Nonexistent 0th day"),
        pytest.param(1900, 1, -1, id="Negative day"),
        # month format
        pytest.param(1900, 0, 1, id="Nonexistent 0th day"),
        pytest.param(1900, 13, 1, id="Nonexistent 13th month"),
        pytest.param(1900, -1, 1, id="Negative month"),
    ],
)
def test_incorrect_date_format(year, month, day):
    """Check incorrect date"""
    result: GregorianDate = date_to_gregorian(year=year, month=month, day=day)
    assert (
        not result.correct
    ), f"Incorrect date '{day}-{month}-{year}'(day-month-year) is recognized as correct"


@pytest.mark.parametrize(
    "year, month, day",
    [
        pytest.param(0, 1, 31, id="Unsupported bottom boundary year"),
        pytest.param(10_000, 1, 1, id="Unsupported top boundary year"),
        pytest.param(-1, 1, 31, id="Negative year"),
    ],
)
def test_unsupported_date_format(year, month, day):
    """Check unsupported date"""
    result: GregorianDate = date_to_gregorian(year=year, month=month, day=day)
    assert (
        not result.supported
    ), f"Unsupported date '{day}-{month}-{year}'(day-month-year) is recognized as supported"
