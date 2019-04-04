"""
Settings core module.
Keep it clear.

Possibly, you can put some IoC tools here,
which are applicable for entire project and
help you to organize code.

Settings are splitted to:
- dev - for running locally during development
- prod - for running dockerized app in production environment
- test - for running dockerized app in staging environment

We also user split-settings module to organize
setting more atomic and decomposed, so all
settings aspects are pluggable.

You can create your own "settings plugins":
just create file in settings/components and
include it with corresponding function.

Thus, you can manage your setting and compose
such combinations, as you like.

"""
