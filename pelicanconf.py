#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Matthew Grossman"
SITENAME = "Matthew Grossman's website"
SITURL = "https://matthewgrossman.me"
SITELOGO = "images/profile.png"
FAVICON = SITELOGO
GITHUB_URL = "https://github.com/matthewgrossman"

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
THEME = '/Users/mgrossman/src/pelican-themes/Flex'

LINKS = (("test", "google.com"),)
DEFAULT_LANG = 'en'

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/matthewryangrossman/'),
          ('github', 'https://github.com/matthewgrossman'))


COPYRIGHT_YEAR = "$CURRENT_YEAR"
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
HOME_HIDE_TAGS = True
