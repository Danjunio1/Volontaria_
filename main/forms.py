from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "name",
                "placeholder": "Votre Nom",
                "required": "required",
                "data-validation-required-message": "Please enter your name",
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "Votre E-mail",
                "required": "required",
                "data-validation-required-message": "Please enter your email",
            }
        ),
    )
    objet = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "subject",
                "placeholder": "Objet",
                "required": "required",
                "data-validation-required-message": "Please enter a subject",
            }
        ),
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "message",
                "placeholder": "Message",
                "required": "required",
                "data-validation-required-message": "Please enter your message",
            }
        ),
    )
    
