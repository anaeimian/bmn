import pdb
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

import jdatetime
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import datetime
from django.contrib.auth import authenticate, login, logout

from application.models import FileExtraAttachment, TextExtraAttachment, CoopApplication, Association_Application
from users.forms import RegisterForm
from messaging.models import Message
from manager.models import News, Notice
from users.models import BMNUser, Field, Application
from users.forms import CoopApplicationForm
from association.models import Association, Facility


def user_login(request):
    if request.user.is_anonymous():
        if request.method == 'GET':
            success = False
            referrer = request.META.get('HTTP_REFERRER', None)
            # if referrer == ""
            if request.GET.get('msg', None):
                success = True
            return render(request, 'users/login.html', {
                'success': success
            })
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if (user is not None) and user.is_active:
                login(request, user)
                return get_user_dashboard(request)
            else:
                alerts = "اطلاعات وارد شده معتبر نمی باشد."
                return render(request, 'users/login.html', {
                    'alerts': alerts,
                })

    else:
        if request.method == 'GET':
            return get_user_dashboard(request)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/users/')


def get_user_dashboard(request):
    user = request.user
    notices = Notice.objects.filter(initiation_date__lte=timezone.now).filter(expiration_date__gte=timezone.now)
    news = News.objects.all().reverse()[0:3]
    messages = Message.objects.filter(reciever__id=request.user.id).filter(is_read=False)

    return render(request, 'users/user-dashboard-home.html', {
        'user': user,
        'news': news,
        'notices': notices,
        'new_messages': messages
    })


def user_register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'users/signup.html', {'form': form})
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            pdb.set_trace()
            auth_user = User.objects.create(username=form.cleaned_data['email'], password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])

            BMNUser.objects.create(user=auth_user,
                                   birth_date=jdate_to_date(form.cleaned_data['birthDate']),
                                   birth_country=form.cleaned_data['birth_country'],
                                   residence_country=form.cleaned_data['residence_country'],
                                   education=form.cleaned_data['education'],
                                   university=form.cleaned_data['university'],
                                   field=Field.objects.get(title=form.cleaned_data['field']),
                                   phone=form.cleaned_data['phone'],
                                   mobile=form.cleaned_data['mobile'])

            return HttpResponseRedirect('/users/?msg=success')
        return render(request, 'users/signup.html', {
            'form': form
        })


def user_requests(request):
    if request.method == "GET":
        user = BMNUser.objects.get(user=request.user)
        saved_apps = Application.objects.filter(user=user, is_finalized=False)
        saved_coops = []
        # saved_military = []
        complete_apps = Application.objects.filter(user=user, is_finalized=True)
        complete_coops = []
        # complete_military = []
        if len(saved_apps) > 0:
            for app in saved_apps:
                coop_application = None
                try:
                    coop_application = CoopApplication.objects.get(application=app)
                except ObjectDoesNotExist:
                    pass
                except MultipleObjectsReturned:
                    pass
                if coop_application:
                    saved_coops.append(coop_application)

            # for app in saved_apps:
            #     saved_military.append(MilitaryApplication.objects.filter(application=app))

        # pdb.set_trace()

        if len(complete_apps) > 0:
            for app in complete_apps:
                coop_application = None
                try:
                    coop_application = CoopApplication.objects.get(application=app)
                except ObjectDoesNotExist:
                    pass
                except MultipleObjectsReturned:
                    pass
                if coop_application:
                    complete_coops.append(coop_application)


            # for app in complete_apps:
            #     complete_military.append(MilitaryApplication.objects.filter(application=app))

        return render(request, 'users/user-dashboard-requests.html',
                      {'saved_coops': saved_coops, "complete_coops": complete_coops,})


def get_user_messages(request):
    return render(request, 'users/user-dashboard-messages.html', {

    })


def new_request(request):
    if request.method == "POST":
        type = request.POST['type-id']

        if type == '0':
            return HttpResponseRedirect('/users/requests/new/coop/')
        elif type == '1':
            return HttpResponseRedirect('/users/cons/')
        elif type == '2':
            return HttpResponseRedirect('/users/requests/new/contact/')
        else:
            return render(request, 'users/user-dashboard-requests-wrong.html', {
            })

    elif request.method == "GET":
        return HttpResponseRedirect("/users/requests/")


def getassocs(request):
    if request.method == "POST":
        field = Field.objects.get(title=request.POST['field'])
        facility = Facility.objects.get(title=request.POST['facility'])
        l1 = field.associations.all()
        l2 = facility.associations.all()

        associations = [i for i in l1 if i in l2]
        associations_names = [association.user.first_name for association in associations]
        return JsonResponse(associations_names, safe=False)


def new_coop_request(request):
    if request.method == "GET":
        form = CoopApplicationForm()
        return render(request, 'users/user-dashboard-requests-new-coop.html', {
            'form': form,
        })
    elif request.method == "POST":
        form = CoopApplicationForm(request.POST)

        if not (request.POST['association1'] and not (request.POST["association1"] == "none")) or not request.POST['association2'] or request.POST["association2"] == "none" or not request.POST['association3'] or request.POST["association3"] == "none":
            form = CoopApplicationForm()
            return render(request, 'users/user-dashboard-requests-new-coop.html', {
                'form': form, 'error': True,
            })

        if form.is_valid():
            application_user = BMNUser.objects.get(user=request.user)
            application = Application.objects.create(user=application_user)
            coop_application = CoopApplication.objects.create(application=application, field=form.cleaned_data['field'],
                                                              facility=form.cleaned_data['facility'])
            association1 = request.POST['association1']
            association2 = request.POST['association2']
            association3 = request.POST['association3']
            user1 = User.objects.get(first_name=association1)
            user2 = User.objects.get(first_name=association2)
            user3 = User.objects.get(first_name=association3)
            association11 = Association.objects.get(user=user1)
            association22 = Association.objects.get(user=user2)
            association33 = Association.objects.get(user=user3)
            # pdb.set_trace()
            priority1 = Association_Application.objects.create(
                association=association11,
                application=coop_application,
                priority='1'
            )
            priority2 = Association_Application.objects.create(association = association22, application = coop_application, priority = '2')
            priority3 = Association_Application.objects.create(association = association33, application = coop_application, priority = '3')

            facility = coop_application.facility
            requirements = facility.facility_requirements.all()

            text_requirments = [requirement for requirement in requirements if requirement.type == "0"]
            file_requirments = [requirement for requirement in requirements if requirement.type == "1"]

            for fr in file_requirments:
                FileExtraAttachment.objects.create(title=fr.title, application=coop_application)
            for tr in text_requirments:
                TextExtraAttachment.objects.create(title=tr.title, application=coop_application)
            return HttpResponseRedirect("/users/requests/edit/" + coop_application.id.__str__() + "/")
        else:
            form = CoopApplicationForm()
            return render(request, 'users/user-dashboard-requests-new-coop.html', {
                'form': form,
            })
            # TODO Handle form validation.


def edit_coop_request(request, application_id):
    coop_application = CoopApplication.objects.get(pk=application_id)
    text_attachments = coop_application.text_extra_attachments.all()
    file_attachments = coop_application.file_extra_attachments.all()
    priorities = Association_Application.objects.filter(application = coop_application)
    associations = [p.association for p in priorities]
    print(associations)

    if request.method == "GET":
        return render(request, 'users/user-dashboard-requests-coop-edit.html', {
            'text_attachments': text_attachments,
            'file_attachments': file_attachments,
            'application': coop_application,
            'associations': associations,
        })
    elif request.method == "POST":
        #pdb.set_trace()

        for ta in text_attachments:
            ta.text = request.POST["text-" + ta.id.__str__()]
            ta.save()
        for fa in file_attachments:
            if request.FILES.get("file-" + fa.id.__str__(), None):
                fa.file = request.FILES["file-" + fa.id.__str__()]
                fa.save()

        if request.POST['action'] == "save":
            return render(request, 'users/user-dashboard-requests-coop-edit.html', {
                'text_attachments': text_attachments,
                'file_attachments': file_attachments,
                'application': coop_application,
                'success': True,
            })

        elif request.POST['action'] == "preview":
            for ta in text_attachments:
                if request.POST["text-" + ta.id.__str__()] == '':
                 return render(request, 'users/user-dashboard-requests-coop-edit.html', {
                 'text_attachments': text_attachments,
                 'file_attachments': file_attachments,
                 'application': coop_application,
                 'error': True,
            })

            for fa in file_attachments:
                if request.POST["file-" + fa.id.__str__()] == '' and not fa:
                    return render(request, 'users/user-dashboard-requests-coop-edit.html', {
                    'text_attachments': text_attachments,
                    'file_attachments': file_attachments,
                    'application': coop_application,
                    'error': True,
            })
            return HttpResponseRedirect("/users/requests/preview/coop/" + coop_application.id.__str__() + "/")


def preview_coop_request(request, application_id):
    coop_application = CoopApplication.objects.get(pk=application_id)
    text_attachments = coop_application.text_extra_attachments.all()
    file_attachments = coop_application.file_extra_attachments.all()
    priorities = Association_Application.objects.filter(application=coop_application)

    if request.method == "GET":
        return render(request, 'users/user-dashboard-requests-preview-coop.html', {
            'application': coop_application,
            'text_requirements': text_attachments,
            'file_requirementes': file_attachments,
            'priorities': priorities,
        })
    elif request.method == 'POST':
        coop_application.application.is_finalized = True
        coop_application.application.finalization_date = datetime.datetime.now()
        coop_application.application.save()
        coop_application.save()
        return HttpResponseRedirect('/users/requests/')


def view_coop_request(request, application_id):
    coop_application = CoopApplication.objects.get(pk=application_id)
    text_attachments = coop_application.text_extra_attachments.all()
    file_attachments = coop_application.file_extra_attachments.all()
    priorities = Association_Application.objects.filter(application=coop_application)

    if request.method == "GET":
        return render(request, 'users/user-dashboard-coop-request-view.html', {
            'application': coop_application,
            'text_requirements': text_attachments,
            'file_requirementes': file_attachments,
            'priorities': priorities,
        })
    elif request.method == 'POST':
        coop_application.application.is_finalized = True
        coop_application.application.finalization_date = datetime.datetime.now()
        coop_application.application.save()
        coop_application.save()
        return HttpResponseRedirect('/users/requests/')


def delete_coop_request(request, application_id):
    coop_application = CoopApplication.objects.get(pk=application_id)
    application = coop_application.application
    text_attachments = coop_application.text_extra_attachments.all()
    file_attachments = coop_application.file_extra_attachments.all()
    priorities = Association_Application.objects.filter(application=coop_application)
    coop_application.delete()
    for ta in text_attachments:
        ta.delete()
    for fa in file_attachments:
        fa.delete()
    for p in priorities:
        p.delete()
    application.delete()
    return HttpResponseRedirect("/users/requests/")


def new_military_request(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass


def jdate_to_date(date_string):
    return jdatetime.date(int(date_string.split('/')[0]),
                          int(date_string.split('/')[1]),
                          int(date_string.split('/')[2])).togregorian()


def gdate_to_str(date_obj):
    return date_obj[0].__str__() + "/" + date_obj[1].__str__() + "/" + date_obj[2].__str__()


