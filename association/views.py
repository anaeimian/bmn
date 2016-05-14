from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, get_object_or_404
from application.models import CoopApplication
from django.http import HttpResponseRedirect
from django.template.defaulttags import register


# Create your views here.
def home(request):
    if request.method == 'GET':
        if not request.user.is_authenticated():
            return render(request, 'manager/manager-login.html', {

            })
        else:
            return render(request, 'association/association-dashboard-home.html', {
            })
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if (user is not None) and user.is_active and user.is_superuser:
            login(request, user)
            return render(request, 'association/association-dashboard-home.html', {

            })
        else:
            alerts = "اطلاعات وارد شده معتبر نمی باشد."
            return render(request, 'users/login.html', {
                'alerts': alerts,
            })

def requests(request):
    apps = CoopApplication.objects.all().filter(status=1).exclude(is_deleted = True)
    receivedRequests = CoopApplication.objects.all().exclude(status =1).exclude(status=5).exclude(status=6).exclude(status=7).exclude(is_deleted = True)
    reviewedRequests = CoopApplication.objects.all().exclude(status=1).exclude(status=2).exclude(status=3).exclude(status=4).exclude(
        status=7).exclude(is_deleted=True)
    deletedRequest = CoopApplication.objects.all().filter(is_deleted = True)
    return render(request, 'association/association-dashboard-requests.html', {
        'apps': apps,
        'receivedApps' : receivedRequests,
        'reviewedApps' : reviewedRequests,
        'deletedApps' : deletedRequest
    })
def delete_request(request):
    if request.method == "POST":
        print("true")
        list_of_delete = request.POST.getlist('new_del_inputs')
        for del_id in list_of_delete:
            CoopApplication.objects.all().filter(id=del_id).update(is_deleted=True)
        list_of_delete = request.POST.getlist('rec_del_inputs')
        for del_id in list_of_delete:
            CoopApplication.objects.all().filter(id=del_id).update(is_deleted=True)
        list_of_delete = request.POST.getlist('rev_del_inputs')
        for del_id in list_of_delete:
            CoopApplication.objects.all().filter(id=del_id).update(is_deleted=True)
        list_of_delete = request.POST.getlist('del_rest_inputs')
        for del_id in list_of_delete:
            CoopApplication.objects.all().filter(id=del_id).update(is_deleted=False)
    return HttpResponseRedirect('/association/requests/')

@register.filter(name='lookup')
def cut(value, arg):
    return value[arg]