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
@parser.ignore
def ignore(inp, *, user):
    if not user:
        return lex.ignore.no_user
    inst = db.Ignored.find_one(user=user)
    if inst:
        db.Ignored.purge(user=user)
        return lex.ignore.unignored(user=user)
    else:
        db.Ignored.create(user=user)
        return lex.ignore.ignored(user=user)
