"""
Setting for development only.
Using local SQLite db, supporting CORS, debug mode on
"""

from split_settings.tools import include

from core.settings import DEV_MODE

include(

    # Base settings + environment variables, REQUIRED
    # Insert these components first
    'components/base.py',
    'components/env.py',

    # DB and static files managements, REQUIRED
    'components/sqlite.py',
    'components/static.py',

    # Rest modules, OPTIONAL
    'components/templates.py',
    'components/password.py',
    'components/internationalization.py',

    'components/cors.py'
)

DEBUG = True

MODE = DEV_MODE