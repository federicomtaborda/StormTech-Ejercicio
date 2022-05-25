from django import forms

class PantillaFrom (forms.Form):
    ID = forms.ChoiceField(required=True) 

