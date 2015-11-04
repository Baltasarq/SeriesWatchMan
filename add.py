#!/usr/bin/env python
# MIT License
# (c) baltasar 2015

from google.appengine.api import users
from google.appengine.ext import ndb

from serie import Serie

import webapp2


class AddHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

	if user != None:
		serie = Serie()
		serie.name = "Name"
		serie.web = "http://en.wikipedia.org/wiki/Serial_(radio_and_television)";
		serie.comments = "Serial comments.";
		serie.picture =  "https://upload.wikimedia.org/wikipedia/commons/6/66/SMPTE_Color_Bars.svg";
		serie.user = user.user_id()
		serie.lastEpisode = 1001
		serie.put()
		self.redirect("/modify?id=" + serie.key.urlsafe())

	else:
		self.redirect("/")
