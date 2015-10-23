#!/usr/bin/env python
# MIT License
# (c) baltasar 2015

from google.appengine.api import users
from google.appengine.ext import ndb

from serie import Serie

import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

class MainMenuHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

	if user != None:
		user_name = user.nickname()
		access_link = users.create_logout_url("/")
		series = Serie.query( Serie.user == user.user_id() ).order(Serie.added)

		template_values = {
			"user_name": user_name,
			"access_link": access_link,
			"series": series,
		}

		template = JINJA_ENVIRONMENT.get_template( "mainMenu.html" )
		self.response.write(template.render(template_values));
	else:
		self.redirect("/")
