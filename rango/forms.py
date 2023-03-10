
from django import forms
from rango.models import *
from django.contrib.auth.models import User
char_field_max_length = 128
url_field_max_length = 200
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=char_field_max_length, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required= False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=char_field_max_length, help_text = "Please enter the title of the page.")
    url = forms.URLField(max_length=url_field_max_length, help_text="Please enter the URL of the page.")
    views  = forms.IntegerField(widget=forms.HiddenInput(),initial=0, required=False)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture',)