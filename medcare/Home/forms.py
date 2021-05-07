from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registrationform(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "username" )
    
    def save(self,commit= True):
    
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user