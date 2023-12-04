from dataclasses import dataclass
from enum import Enum


class AttendanceType(Enum):
    ABSENCE = 1
    PERSONAL = 2
    SICK = 3
    BEREAVEMENT = 4
    PUBLIC = 5
    LATE = 7


@dataclass
class Absences:
    lessons: [AttendanceType]
