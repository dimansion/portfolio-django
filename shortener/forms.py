from django import forms


from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(
            label='', 
            validators=[validate_url, validate_dot_com],
            widget = forms.TextInput(
                    attrs ={
                        "placeholder": "Your long URL goes here",
                        "class": "form-control"
                        }
                )
            )