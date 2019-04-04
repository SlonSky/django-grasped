from django.core.management import BaseCommand
from django.conf import settings

from apps.misc.boundary.consuming import SuperUserManager


class Command(BaseCommand):

    def handle(self, *args, **options):

        SuperUserManager.create_super_user(
            settings.SUPER_USER_LOGIN,
            settings.SUPER_USER_PASSWORD
        )