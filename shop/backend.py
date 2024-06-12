from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            # Filter users by email address
            users = User.objects.filter(email=email)
            # Ensure only one user is found
            if users.count() == 1:
                user = users.first()
                if user.check_password(password):
                    return user
            elif users.count() > 1:
                # Handle case where multiple users have the same email address
                # You may want to log this occurrence or handle it based on your application's logic
                pass
        except User.DoesNotExist:
            return None