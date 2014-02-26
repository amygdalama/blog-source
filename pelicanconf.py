#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Amy Hanlon'
SITENAME = u'Amy Hanlon'
SITEURL = 'http://amygdalama.github.io'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = False

# Social widget
SOCIAL = False

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pelican-themes/subtle"

DISPLAY_CATEGORIES_ON_MENU = False

OUTPUT_PATH = 'output/'

GOOGLE_ANALYTICS = "UA-48330831-1"
