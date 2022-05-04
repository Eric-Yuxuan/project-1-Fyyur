import json, sys
import dateutil.parser
import babel, datetime, dateutil.parser, pytz
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from sqlalchemy import String
from forms import *
from flask_migrate import Migrate
from sqlalchemy.dialects import postgresql
from app import *

venues = Venue.query.all()
for venue in Venue.query.all():
  venue.upcoming_shows = 0
data = []
for show in show_info.query.all():
  if pytz.utc.localize(show.start_time) > pytz.utc.localize(datetime.utcnow()):
    Venue.query.get(show.venue_id).upcoming_shows += 1
def venueUpcomingShows(venues):
  return venues.upcoming_shows
venues.sort(key= venueUpcomingShows, reverse=True)
for venue in venues:
  find = False
  for i in data:
    if i['city'] == venue.city:
      find = True
      i['venues'].append({"id": venue.id, "name": venue.name, "num_upcoming_shows": venue.upcoming_shows})
      break
  if not find:
    data.append({"city": venue.city, "state": venue.state, "venues": [{"id": venue.id, "name": venue.name, "num_upcoming_shows": venue.upcoming_shows}]})

for i in data:
  print(i)