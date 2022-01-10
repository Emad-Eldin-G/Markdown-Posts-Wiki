from django import forms

class create_new(forms.Form):
    title = forms.CharField(label="Title", max_length=30)
    body = forms.CharField(label="Body", max_length=500)
