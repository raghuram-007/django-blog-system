from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from blog.models import Category, Media

class ContactForm(forms.Form):
    name=forms.CharField(label='name',max_length=100, required=True)
    email=forms.EmailField(label='email', required=True)
    message=forms.CharField(label='message', required=True)
class Meta:
  model=User
  fields=['name','email']
    
  
class RegisterForm(forms.ModelForm):
  username=forms.CharField(label="username", max_length=100, required=True)
  email=forms.CharField(label='email', max_length=100, required=True)
  password=forms.CharField(label="password", max_length=100, required=True)
  confirm_password=forms.CharField(label="confirm_password", max_length=100, required=True)
  
  class Meta:
       model=User
       fields=['username','email','password']
    
    
  def clean(self):
        cleaned_data= super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
          raise forms.ValidationError("password are not match")
    
        return cleaned_data
      
      
class loginform(forms.Form):
  username=forms.CharField(label='username',max_length=100, required=True)
  password=forms.CharField(label='password',max_length=100,required=True)
  
  def clean(self):
      cleaned_data=super().clean()
      username=cleaned_data.get('username')
      password=cleaned_data.get('password')
      if username and password:
        user=authenticate(username=username,password=password)
        if user is None:
          raise forms.ValidationError("User doesn't Exists...!")
        
        
      
class Postform(forms.ModelForm):
    title = forms.CharField(label='title', max_length=100, required=True)
    content = forms.CharField(label='content', required=True)
    categer = forms.ModelChoiceField(label='category', required=True, queryset=Category.objects.all())
    

    class Meta:
        model = Media
        fields = ['title', 'content', 'categer','img']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        categer = cleaned_data.get('categer')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content and len(content) < 8:
            raise forms.ValidationError("Content must be at least 8 characters long.")
        return content
 
 
 
class ForgetPassword(forms.Form):
   email=forms.EmailField(label="email",max_length=40)
   
   def clean(self):
      cleaned_data=super().clean()
      email=cleaned_data.get("email")
      
      if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("user email doesn;t exist")
   
   

class ResetForm(forms.Form):
    password = forms.CharField(label="New Password", widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data