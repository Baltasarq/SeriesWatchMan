#!/usr/bin/env python
# MIT License
# (c) baltasar 2015

from google.appengine.api import users
from google.appengine.ext import ndb

from serie import Serie

import time
import webapp2

class NextSeasonHandler(webapp2.RequestHandler):
    def get(self):
	id = self.request.GET['id']
        user = users.get_current_user()

	if (user != None
	and id != None):
		user_name = user.nickname()

		try:
			serie = ndb.Key(urlsafe = id).get()
		except:
			self.redirect("/main")
			return

		season = serie.lastEpisode // 1000
		serie.lastEpisode = ( ( season + 1 ) * 1000 ) + 1
		serie.put()
		time.sleep(1)
		self.redirect("/main?id=" + serie.key.urlsafe())
	else:
		self.redirect("/")
