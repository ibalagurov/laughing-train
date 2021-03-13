import pytest

from src import gregorian_calendar


@pytest.mark.parametrize("string_date", ["01-01-1900"])
def test_correct_date_format(string_date):
    result = gregorian_calendar.correct(string=string_date)
    assert result, f"Correct date '{string_date}' was recognized as incorrect"
