from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()
    class Meta :  # ene Meta gedeg ni special shit genee. ""configure""
        # form create hiihed l ene ni dagaldaad yvj l baidiin baina.
        # Ug ni eniig bol ajilluugui baigaaz, ghde Meta gdg ner ni l bhd hangalttai uuru uriigu shaadaf ed baina.
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm) :
    email = forms.EmailField()
    class Meta :
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm) :
    class Meta :
        model = Profile
        fields = ['image']
            
