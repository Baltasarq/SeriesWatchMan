#!/usr/bin/env python
# MIT License
# (c) baltasar 2015

from google.appengine.api import users

import os
import webapp2
import jinja2

from error import ErrorHandler
from mainMenu import MainMenuHandler
from add import AddHandler
from modify import ModifyHandler
from delete import DeleteHandler
from next_season import NextSeasonHandler
from next_episode import NextEpisodeHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user_name = "Please login"
        user = users.get_current_user()
        if user != None:
                self.redirect("/main")
		return
        else:
                access_link = users.create_login_url("/main")

        template_values = {
                "user_name": user_name,
                "access_link": access_link,
        }

	template = JINJA_ENVIRONMENT.get_template( "index.html" )
	self.response.write(template.render(template_values));

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/main", MainMenuHandler),
    ("/add", AddHandler),
    ("/modify", ModifyHandler),
    ("/delete", DeleteHandler),
    ("/error", ErrorHandler),
    ("/nextEpisode", NextEpisodeHandler),
    ("/nextSeason", NextSeasonHandler),
], debug=True)
