from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, get_object_or_404
from application.models import CoopApplication
from django.http import HttpResponseRedirect
from association.forms import FilterRequestsForm
import math


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
    if request.method == 'POST':
        requests = CoopApplication.objects.all()
        print("size", requests.__len__())
        form = FilterRequestsForm(request.POST)
        if form.is_valid():
            if (form.cleaned_data['first_name'] != ""):
                first_name = form.cleaned_data['first_name']
                requests = requests.filter(application__user__user__first_name=first_name)
                print("first")
            if (form.cleaned_data['last_name'] != ""):
                last_name = form.cleaned_data['last_name']
                requests = requests.filter(application__user__user__last_name=last_name)
                print("last")
            print(requests.__len__())
            # if(form.cleaned_data['email']!= None):
            #     email = form.cleaned_data['email']
            if (form.cleaned_data['field'] != None):
                field = form.cleaned_data['field']
                requests = requests.filter(field=field)
                print("field")
            if (form.cleaned_data['facility'] != None):
                facility = form.cleaned_data['facility']
                requests = requests.filter(facility__title=facility)
                print("fac")
            print(requests.__len__())

            if (form.cleaned_data['status'] != None):
                status = form.cleaned_data['status']
                print(requests.__len__())
                status = int(status) - 1
                if (status != -1):
                    requests = requests.filter(status=status)
                    print("stat")
                print(status)
                print(requests.__len__())
            if (form.cleaned_data['start_date'] != None):
                start_date = form.cleaned_data['start_date']
            if (form.cleaned_data['end_date'] != None):
                end_date = form.cleaned_data['end_date']
                requests = CoopApplication.objects.all().filter(facility = facility)
        apps = requests.filter(status=1).exclude(is_deleted=True)
        receivedRequests = requests.exclude(status=1).exclude(status=5).exclude(status=6).exclude(
            status=7).exclude(status=8).exclude(is_deleted=True)
        reviewedRequests = requests.exclude(status=1).exclude(status=2).exclude(status=3).exclude(
            status=4).exclude(is_deleted=True)
        deletedRequest = requests.filter(is_deleted=True)
        return render(request, 'association/association-dashboard-requests.html', {
            'apps': apps,
            'receivedApps': receivedRequests,
            'reviewedApps': reviewedRequests,
            'deletedApps': deletedRequest,
            'form': form
        })

    else:
        # apps = CoopApplication.objects.all().filter(status=1).exclude(is_deleted=True)[0:5]
        # receivedRequests = CoopApplication.objects.all().exclude(status=1).exclude(status=5).exclude(status=6).exclude(
        #     status=7).exclude(status=8).exclude(is_deleted=True)[0:5]
        # reviewedRequests = CoopApplication.objects.all().exclude(status=1).exclude(status=2).exclude(status=3).exclude(
        #     status=4).exclude(is_deleted=True)[0:5]
        # deletedRequest = CoopApplication.objects.all().filter(is_deleted=True)[0:5]
        # form = FilterRequestsForm()
        # appsPagesNumber = math.ceil(CoopApplication.objects.all().__len__() / 5)
        # return render(request, 'association/association-dashboard-requests.html', {
        #     'apps': apps,
        #     'receivedApps': receivedRequests,
        #     'reviewedApps': reviewedRequests,
        #     'deletedApps': deletedRequest,
        #     'form': form,
        #     'appsPagesNumberRange': range(1, appsPagesNumber + 1),
        #     'appsPagesNumber': appsPagesNumber
        # })
        return HttpResponseRedirect('/association/requests/1')


def delete_request(request):
    if request.method == "POST":
        temp = request.POST.getlist('which-button')
        print(temp)
        if temp == []:
            temp = ['0']
        for value in temp:
            if value == '1':
                list_of_changes = request.POST.getlist('status')
                list_of_ids = request.POST.getlist('app-id')
                counter = 0
                if list_of_changes != []:
                    for id in list_of_ids:
                        CoopApplication.objects.all().filter(id=id).update(status=int(list_of_changes[counter]) + 1)
                        counter += 1
                list_of_changes = request.POST.getlist('rec-status')
                list_of_ids = request.POST.getlist('rec-app-id')
                counter1 = 0
                if list_of_changes != []:
                    print('true')
                    for id in list_of_ids:
                        print(int(list_of_changes[counter1]) + 1)
                        CoopApplication.objects.all().filter(id=id).update(status=int(list_of_changes[counter1]) + 1)
                        counter1 += 1
                list_of_changes = request.POST.getlist('rev-status')
                list_of_ids = request.POST.getlist('rev-app-id')
                counter2 = 0
                if list_of_changes != []:
                    for id in list_of_ids:
                        CoopApplication.objects.all().filter(id=id).update(status=int(list_of_changes[counter2]) + 1)
                        counter2 += 1
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


def paged_requests(request, page_id):
    apps = CoopApplication.objects.all().filter(status=1).exclude(is_deleted=True)[
           int(page_id) * 5 - 5:int(page_id) * 5]
    receivedRequests = CoopApplication.objects.all().exclude(status=1).exclude(status=5).exclude(status=6).exclude(
        status=7).exclude(status=8).exclude(is_deleted=True)[int(page_id) * 5 - 5:int(page_id) * 5]
    reviewedRequests = CoopApplication.objects.all().exclude(status=1).exclude(status=2).exclude(status=3).exclude(
        status=4).exclude(is_deleted=True)[int(page_id) * 5 - 5:int(page_id) * 5]
    deletedRequest = CoopApplication.objects.all().filter(is_deleted=True)[int(page_id) * 5 - 5:int(page_id) * 5]
    form = FilterRequestsForm()
    appsPagesNumber = math.ceil(CoopApplication.objects.all().__len__() / 5)
    return render(request, 'association/association-dashboard-requests.html', {
        'apps': apps,
        'receivedApps': receivedRequests,
        'reviewedApps': reviewedRequests,
        'deletedApps': deletedRequest,
        'form': form,
        'appsPagesNumber': appsPagesNumber,
        'appsPagesNumberRange': range(1, appsPagesNumber + 1)
    })


def details(request, app_id):
    app = CoopApplication.objects.get(id=app_id)
    return render(request, 'association/association-dashboard-request-detail.html', {'app': app})


def all_requests(request):
    return HttpResponseRedirect('/association/requests')
