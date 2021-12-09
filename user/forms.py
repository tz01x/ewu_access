
from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Row, Field, HTML, Column


class MyUserCreationForm(UserCreationForm):
    ewu_mail = forms.EmailField()
    role_in_ewu = forms.ChoiceField(choices=(
        ('student', 'student'), ('ex-student', 'ex-student'), ('facalty', 'facalty')))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                
                "User info",  # legend of the form set string/none. ex : 'Basic Info'
        
                Field("username", css_class="px-2"),
                'role_in_ewu',

                css_class="mk"
                

            ),
            Fieldset(
                'Auth',  # legend of the form set string/none
                Field("email", css_class="px-2"),
                'ewu_mail',


                'password1',
                'password2',
                css_class="px-2"

            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-indigo mx-2')
            )
        )


    class Meta:
        model=User
        fields=['username','email','ewu_mail','password1','password2',]

    
    