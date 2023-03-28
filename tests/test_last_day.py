import datetime

import pytest
from freezegun import freeze_time
from pytz import timezone

from faking_time_demo.main import get_text_for_day, is_last_day_of_month
import time
import time_machine

start_date = datetime.datetime(2023, 1, 1)

test_dates = [start_date + datetime.timedelta(days=no_days) for no_days in range(365)]

test_scenario_message = [
    (
        date_,
        "is last day of the month"
        if date_
        in [
            datetime.datetime(2023, 1, 31),
            datetime.datetime(2023, 2, 28),
            datetime.datetime(2023, 3, 31),
            datetime.datetime(2023, 4, 30),
            datetime.datetime(2023, 5, 31),
            datetime.datetime(2023, 6, 30),
            datetime.datetime(2023, 7, 31),
            datetime.datetime(2023, 8, 31),
            datetime.datetime(2023, 9, 30),
            datetime.datetime(2023, 10, 31),
            datetime.datetime(2023, 11, 30),
            datetime.datetime(2023, 12, 31),
        ]
        else "is NOT last day of the month",
    )
    for date_ in test_dates
]
test_scenario_message.append((datetime.datetime(2024, 2, 29), "is last day of the month"))


test_scenario_bool = [
    (
        date_,
        True
        if date_
        in [
            datetime.datetime(2023, 1, 31),
            datetime.datetime(2023, 2, 28),
            datetime.datetime(2023, 3, 31),
            datetime.datetime(2023, 4, 30),
            datetime.datetime(2023, 5, 31),
            datetime.datetime(2023, 6, 30),
            datetime.datetime(2023, 7, 31),
            datetime.datetime(2023, 8, 31),
            datetime.datetime(2023, 9, 30),
            datetime.datetime(2023, 10, 31),
            datetime.datetime(2023, 11, 30),
            datetime.datetime(2023, 12, 31),
        ]
        else False,
    )
    for date_ in test_dates
]
test_scenario_bool.append((datetime.datetime(2024, 2, 29), True))


def get_offset(tzname):
    match tzname:
        case "UTC":
            return 0
        case "EST":
            return 5
        case "CET":
            return -1
        case "EET":
            return -2
        case _:
            raise Exception("Unknown timezone")


@pytest.mark.parametrize(("input_datetime", "expected_result"), test_scenario_message)
def test_get_text_for_day_freeze_gun(input_datetime, expected_result):
    with freeze_time(input_datetime, tz_offset=get_offset(time.tzname[0])):
        message = get_text_for_day()
        assert expected_result in message


@pytest.mark.parametrize(("input_datetime", "expected_result"), test_scenario_message)
def test_get_text_for_day_time_machine(input_datetime, expected_result):
    input_datetime = input_datetime.replace(tzinfo=timezone(time.tzname[0]))
    with time_machine.travel(input_datetime):
        message = get_text_for_day()
        assert expected_result in message


@pytest.mark.parametrize(("input_datetime", "expected_result"), test_scenario_bool)
def test_is_last_day_of_month(input_datetime, expected_result):
    with freeze_time(input_datetime):
        assert is_last_day_of_month(input_datetime=input_datetime) is expected_result
