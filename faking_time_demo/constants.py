from enum import Enum


class AvailableTimeZone(str, Enum):
    UTC = "UTC"
    NETHERLANDS = "Europe/Amsterdam"
    ROMANIA = "Europe/Bucharest"
    NEW_YORK = "US/Eastern"
