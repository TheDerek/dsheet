#!/usr/bin/env python3.8

import dsheet

Name = dsheet.UserEntryCol("Employee Name", str)
JoinDate = dsheet.UserEntryCol("Join Date", dsheet.Date)
Salary = dsheet.UserEntryCol("Salary", float)
