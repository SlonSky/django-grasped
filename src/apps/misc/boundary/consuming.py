from django.contrib.auth.models import User


class SuperUserManager:

    @staticmethod
    def create_super_user(login, password):

        if User.objects.filter(username=login).count() > 0:
            return

        user = User.objects.create_superuser(
            username=login, password=password, email=''
        )

        return user