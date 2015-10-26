#!/usr/bin/env python
# MIT License
# (c) baltasar 2015

from google.appengine.api import users
from google.appengine.ext import ndb

from serie import Serie

import time
import webapp2

class NextEpisodeHandler(webapp2.RequestHandler):
    def get(self):
	id = self.request.GET['id']
        user = users.get_current_user()

	if (user != None
	and id != None):
		user_name = user.nickname()
		access_link = users.create_logout_url("/")

		try:
			serie = ndb.Key(urlsafe = id).get()
		except:
			self.redirect("/main")
			return

		serie.lastEpisode += 1
		serie.put()
		time.sleep(1)
		self.redirect("/main?id=" + serie.key.urlsafe())
	else:
		self.redirect("/")
