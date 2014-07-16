#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Amy Hanlon'
SITENAME = u'Amy Hanlon'
SITEURL = 'http://amygdalama.github.io'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%B %d %Y')

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'

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

DISQUS_SITENAME = "mathamy"

PAGE_PATHS = ['pages', 'tutorials']

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'toc']

