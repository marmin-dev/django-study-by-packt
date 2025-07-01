from django.contrib.auth.models import User


class EmailAuthBackend:
    def authenticate(self, request):
        try:
            user = User.objects.get(email=request.user.email)
            if user.check_password(user.password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None