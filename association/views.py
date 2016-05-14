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
        temp = request.POST.getlist('which-button')
        for value in temp:
            if value == '1':
                list_of_changes= request.POST.getlist('status')
                print(list_of_changes)
                list_of_ids = request.POST.getlist('app-id')
                print(list_of_ids)
                counter =0
                for id in list_of_ids:
                    CoopApplication.objects.all().filter(id=id).update(status = list_of_changes[counter])
                    counter+=1
            else:
                list_of_delete = request.POST.getlist('new_del_inputs')
                for del_id in list_of_delete:
                    if del_id != "":
                        CoopApplication.objects.all().filter(id=del_id).update(is_deleted=True)
                list_of_delete = request.POST.getlist('rec_del_inputs')
                for del_id in list_of_delete:
                    if del_id != "":
                        CoopApplication.objects.all().filter(id=del_id).update(is_deleted=True)
                list_of_delete = request.POST.getlist('rev_del_inputs')
                for del_id in list_of_delete:
                    if del_id != "":
                        CoopApplication.objects.all().filter(id=del_id).update(is_deleted=True)
                list_of_delete = request.POST.getlist('del_rest_inputs')
                for del_id in list_of_delete:
                    if del_id != "":
                        CoopApplication.objects.all().filter(id=del_id).update(is_deleted=False)
    return HttpResponseRedirect('/association/requests/')

def save_changes(request):
    print('ye baby')
    if request.method == "POST":
        temp = request.POST.getlist('which-button')
        print(temp)
