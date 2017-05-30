#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Synergie'
SITENAME = 'Les Journées Synergiques'
SITEURL = ''
DESCRIPTION = 'Ateliers d\'initiation aux métiers de l\'informatique'

PATH = 'content'
THEME = 'themes/synergie-twenty'

LOCALE = ("fr_FR")
TIMEZONE = 'Europe/Paris'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 3
RELATIVE_URLS = True

# Content
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['files']

# Theme-related
def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'

JINJA_FILTERS = {'sidebar': sidebar}
SOCIAL = (('github', 'http://github.com/synergie-asso'),
        ('facebook', 'http://facebook.com/synergie.io'),
        ('twitter', 'http://twitter.com/synergieio')
        )
MAIL_CONTACT = "contact@synergie.epita.fr"
