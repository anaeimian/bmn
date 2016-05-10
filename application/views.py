from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    if request.method == 'GET':
        if not request.user:
            return render(request, 'association/association-login.html', {})
        else:
            return render(request, 'association/association-dashboard-home.html', {})
    else:
        return None


def logout(request):
    logout(request.user)
    return HttpResponseRedirect("/association/")


def messages(request):
    return render(request, 'association/association-dashboard-messages.html', {
        'new_messages': 0
     })


def requests(request):
    return render(request, 'association/association-dashboard-requests.html', {
        'new_messages': 0
    })

