from datetime import date
import seasons

def test_calculate_age_in_mins():
    user_date = date(2000, 1, 1)
    expected_age_in_mins = (date.today() - user_date).days * 24 * 60
    assert seasons.calculate_age_in_mins(user_date) == expected_age_in_mins

