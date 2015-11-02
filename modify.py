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

class ModifyHandler(webapp2.RequestHandler):
    def get(self):
        try:
    	    id = self.request.GET['id']
        except:
            id = None

        if id == None:
            self.redirect("/error?msg=serie was not found")
            return

        user = users.get_current_user()

    	if user != None:
    		user_name = user.nickname()
    		access_link = users.create_logout_url("/")

    		try:
    			serie = ndb.Key(urlsafe = id).get()
    		except:
    			self.redirect("/error?msg=key does not exist")
    			return

    		template_values = {
    			"user_name": user_name,
    			"access_link": access_link,
    			"serie": serie,
    		}

    		template = JINJA_ENVIRONMENT.get_template( "modify.html" )
    		self.response.write(template.render(template_values));
    	else:
    		self.redirect("/")

    def post(self):
        try:
            id = self.request.GET['id']
        except:
            id = None

        if id == None:
            self.redirect("/error?msg=missing id for modification")
            return

    	user = users.get_current_user()

    	if user != None:
    		try:
    			serie = ndb.Key(urlsafe = id).get()
    		except:
    			self.redirect("/error?msg=key does not exist")
    			return


    		episode = 1
    		season = 1
    		try:
    			episode = int(self.request.get("episode"))
    			season = int(self.request.get("season"))
    		except:
    			pass

    		serie.name = self.request.get("name")
    		serie.picture = self.request.get("picture")
    		serie.web = self.request.get("web")
    		serie.comments = self.request.get("comments")
    		serie.lastEpisode = (season * 1000) + episode
    		serie.put()
    		time.sleep(1)
    		self.redirect("/main")
    	else:
    		self.redirect("/")
