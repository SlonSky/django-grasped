# Allow CORS, e.g. for accessing API via client

INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
] + MIDDLEWARE

# Allow adding CORS origin to OPTION headers
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True