

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users import models
from django.forms import models


class registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

