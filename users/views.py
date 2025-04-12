from django.shortcuts import render
from users import forms


def register(request):
    msg = None
    if request.method == 'POST':
        subm = forms.registerform(request.POST)
        if subm.is_valid():
            subm.save()
        msg = f"Success! Your account name is {subm.cleaned_data.get('username')}"
    subm = forms.registerform()
    context = {'title': 'Register', 'msg': msg, 'subm': subm}
    return render(request, 'users/register.html', context)