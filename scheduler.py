from flask import Flask
import json
import os
from database import *
import datetime

now = datetime.datetime.now()


def daily_event_updates(event_lst):
    for event in event_lst:
        if event.end_date < now.date:
            Event.delete(event)
