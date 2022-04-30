from audioop import reverse
from sqlalchemy import text
import json
import dateutil.parser
import babel, datetime, dateutil.parser, pytz
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from sqlalchemy import String
import sqlalchemy
from forms import *
from flask_migrate import Migrate
from sqlalchemy.dialects import postgresql
from app import *

venues = Venue.query.all()
# shows = show_info.query.all()
# venuesList_upcomingShowCount = []

for i in Venue.query.all():
  # venuesList_upcomingShowCount.append([i.id, 0])
  i.upcoming_shows = 0

data = []
for show in show_info.query.all():
  # venuesList_upcomingShowCount.append([venue.id, show_info.query.filter_by(venue_id = venue.id).count()])
  # print(show_info.query.filter_by(venue.id < 1).count())
  if pytz.utc.localize(show.start_time) > pytz.utc.localize(datetime.utcnow()):
    # venuesList_upcomingShowCount[show.venue_id-1][1] += 1
    Venue.query.get(show.venue_id).upcoming_shows += 1
    # pass
# print(venuesList_upcomingShowCount)
# for i in Venue.query.all():
#   print(type(i))

# def takeSecond(elem):
#     return elem[1]
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# random.sort(key=takeSecond)
# print(random)

def abc(abc):
  return abc.upcoming_shows
a = Venue.query.all()
a.sort(key= abc, reverse=True)
for i in a:
  # print(i.id)
  find = False
  for j in data:
    if j['city'] == i.city:
      find = True
      j['venues'].append({"id": i.id, "name": i.name, "num_upcoming_shows": i.upcoming_shows})
      break
  if not find:
    data.append({"city": i.city, "state": i.state, "venues": [{"id": i.id, "name": i.name, "num_upcoming_shows": i.upcoming_shows}]})

for i in data:
  print(i)