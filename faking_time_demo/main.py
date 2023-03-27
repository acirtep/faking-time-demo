import sys
import time
from datetime import datetime, timezone, date

import pytz
import typer

from faking_time_demo.constants import AvailableTimeZone


def is_last_day_of_month(input_datetime: date) -> bool:
    """

    :param input_datetime: date object
    :return:
        True, if datetime is last day of month
        False, otherwise
    """
    date_year = input_datetime.year
    date_month = input_datetime.month
    date_day = input_datetime.day

    match date_month:
        case odd_month if odd_month in [1, 3, 5, 7, 8, 10, 12]:
            match date_day:
                case 31:
                    return True
                case _:
                    return False
        case even_month if even_month in [4, 6, 9, 11]:
            match date_day:
                case 30:
                    return True
                case _:
                    return False
        case 2:
            match date_year % 4:
                case 0:
                    match date_day:
                        case 29:
                            return True
                        case _:
                            return False
                case _:
                    match date_day:
                        case 28:
                            return True
                        case _:
                            return False
        case _:
            raise ValueError(
                f"Unexpected values for {input_datetime} {date_year} {date_month} {date_day}"
            )


def get_text_for_day(input_timezone: AvailableTimeZone = None):
    timezone_to_set = input_timezone or time.tzname[0]
    current_datetime = datetime.now(tz=pytz.timezone(timezone_to_set))

    is_last_day = is_last_day_of_month(current_datetime)
    typer.echo(typer.style(f"{current_datetime} is expressed in {timezone_to_set}"))

    if is_last_day:
        message = f"{current_datetime} is last day of the month"
        typer.echo(typer.style(message, fg=typer.colors.GREEN))
    else:
        message = f"{current_datetime} is NOT last day of the month"
        typer.echo(typer.style(message, fg=typer.colors.RED))
    return message


if __name__ == "__main__":
    typer.run(get_text_for_day)
