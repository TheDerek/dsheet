#!/usr/bin/env python3.8

from dataclasses import dataclass
import datetime


class Col:
    pass


class UserEntryCol(Col):
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type


class Date:
    def __init__(self, raw: str):
        args = [int(a) for a in raw.split("-")]
        self._data: datetime.date = datetime.date(*args)

    def __str__(self):
        return str(self._data)
