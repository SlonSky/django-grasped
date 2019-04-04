"""
Test (staging) settings
Using PostgreSQL, CORS support, but debug mode off
"""

from split_settings.tools import include

from core.settings import TEST_MODE

include(

    # Base settings + environment variables, REQUIRED
    # Insert these components first
    'components/base.py',
    'components/env.py',

    # DB and static files managements, REQUIRED
    'components/postgresql.py',
    'components/static.py',

    # Rest modules, OPTIONAL
    'components/templates.py',
    'components/password.py',
    'components/internationalization.py',

    'components/cors.py'
)

DEBUG = False

ALLOWED_HOSTS = ['*']

MODE = TEST_MODE