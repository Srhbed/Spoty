from django.contrib.auth.forms import UserCreationForm



class UserCreationFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "password1", "password2")