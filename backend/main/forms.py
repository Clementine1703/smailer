from django import forms


class EmailListForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    recipient_email_list = forms.CharField( widget=forms.Textarea )

