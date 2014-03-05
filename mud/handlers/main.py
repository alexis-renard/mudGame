# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from mud.handlers.base import BaseHandler
from mud.models.player import Player

import tornado.web
import tornado.escape

#==============================================================================
# home page of the mud and also play page when the user is logged in.
#==============================================================================

class MainHandler(BaseHandler):

    def get(self):
        if self.get_current_user():
            self.render("play.html", **self.extras())
        else:
            self.render("index.html")

    def extras(self):
        player = self.get_player()
        return {
            "items": player.transcript
        }

    @tornado.web.authenticated
    def post(self):
        player = self.get_player()
        # at the moment there is nothing beyond echoing back the input
        text = self.get_argument("text")
        html = tornado.escape.xhtml_escape(text)
        player.transcript.append(html)
        self.render("play.html", **self.extras())
