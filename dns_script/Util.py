#!/usr/bin/python3

import datetime
import time

def get_current_time():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

def time_elapsed(startTime, endTime):
    return endTime - startTime