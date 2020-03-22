from django.shortcuts import render
from django.contrib.auth.models import User


def profiles(request):
    user = User.objects.first()
    profile = user.userprofile

    return render(request, 'index.html', {
        'user': user,
        'profile': profile,
    })
