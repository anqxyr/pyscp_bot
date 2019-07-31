#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

from . import core, lex, parser, db

###############################################################################

db.init('jarvis.db')

###############################################################################
# Commands
###############################################################################

@core.command
@core.require(channel=core.config.irc.sssc)
@parser.ignore
def ignore(inp, *, user):
    inst = db.Ignored.find_one(user=user)
    if inst:
        db.Ignored.purge(user=user)
        return lex.ignore.unignoring(user=user)
    else:
        db.Ignored.create(user=user)
        return lex.ignore.ignoring(user=user)
