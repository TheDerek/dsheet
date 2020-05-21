#!/usr/bin/env python3.8

import json
import sys
from importlib import import_module
import dsheet


def validate(row, cols):
    passed = True

    for name, column in cols.items():
        # Validate the row has the column
        if name not in row:
            print(f"Error row is missing the column '{name}'")
            passed = False
            continue

        # Validate that the data type is correct
        parsed = column.data_type(row[name])
        print(parsed)



if __name__ == "__main__":
    sheet = import_module(sys.argv[1])
    data = json.loads(open(sys.argv[2]).read())

    # Fetch the columns the user specified
    cols = {
        attr: getattr(sheet, attr)
        for attr in dir(sheet)
        if isinstance(getattr(sheet, attr), dsheet.Col)
    }

    # Validate the data against those columns
    for row in data:
        validate(row, cols)
