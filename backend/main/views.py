from django.shortcuts import render
from main.forms import *
from .services import services

def index(request):
    

    email_object_list = services.get_email_list()
    form = EmailListForm()
    if email_object_list:
        form.fields['recipient_email_list'].initial = services.convert_email_list_to_str(email_object_list)
    return render(request, 'main/index.html', context={'form': form})
