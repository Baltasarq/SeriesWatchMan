#!/usr/bin/env python
# MIT License
# (c) baltasar 2015

from google.appengine.api import users
from google.appengine.ext import ndb

from serie import Serie

import time
import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

class AddHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

	if user != None:
		user_name = user.nickname()
		access_link = users.create_logout_url("/")

		template_values = {
			"user_name": user_name,
			"access_link": access_link,
		}

		template = JINJA_ENVIRONMENT.get_template( "add.html" )
		self.response.write(template.render(template_values));
	else:
		self.redirect("/")

    def post(self):
	user = users.get_current_user()

	if user != None:
		user_name = user.nickname()
		serie = Serie()
		serie.user = user.user_id()
		serie.name = self.request.get("name")
		serie.web = self.request.get("web")
		serie.picture = self.request.get("picture")
		serie.comments = self.request.get("comments")
		serie.lastEpisode = 1001
		serie.put()
		time.sleep(1)
		self.redirect("/main")
	else:
		self.redirect("/")
