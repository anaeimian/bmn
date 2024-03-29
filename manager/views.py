from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import user_passes_test, login_required
import jdatetime
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect,HttpResponse
from association.models import Facility, Association
from manager.forms import NoticeForm, NewsForm, FacilityForm, FieldForm, AssociationForm, FilterRequestsForm
from application.models import CoopApplication
from messaging.models import Message, Conversation
from users.models import Field, BMNUser
from manager.models import Question, News, Notice
import json
import datetime


def is_manager(user):
    if user.is_superuser:
        return True
    else:
        return False


def validate_association_data(name, username, email, password, repeat_password):
    errors = []
    if not name or name == "":
        errors.append("نام پایگاه را باید وارد کنید.")
    if not username or username == "":
        errors.append("نام کاربری پایگاه را باید وارد کنید.")
    if not password or password == "":
        errors.append("رمز عبور پایگاه را باید وارد کنید.")
    if not email or email == "":
        errors.append("ایمیل پایگاه را باید وارد کنید.")
    if not password == repeat_password:
        errors.append("رمزهای عبور وارد شده با هم یکی نیستند.")
    if User.objects.filter(username=username) or User.objects.filter(first_name=name):
        errors.append('این پایگاه قبلا در سیستم ثبت شده است.')

    return errors

@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def home(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    if request.method == 'GET':
        if not request.user.is_authenticated():
            return render(request, 'manager/manager-login.html', {
                'new_messages': newMessages,
            })
        else:
            return render(request, 'manager/manager-dashboard-home.html', {
                'new_messages': newMessages,
            })
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if (user is not None) and user.is_active and user.is_superuser:
            login(request, user)
            return render(request, 'manager/manager-dashboard-home.html', {
                'new_messages': newMessages
            })
        else:
            alerts = "اطلاعات وارد شده معتبر نمی باشد."
            return render(request, 'users/login.html', {
                'alerts': alerts,
                'new_messages': newMessages,
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def logout_user(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect("/manager/")


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def messages(request):
    conversations = Conversation.objects.all().filter(receiver = request.user).order_by('-lastMessageTime')
    newMessages=0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages+=1
    return render(request, 'manager/manager-dashboard-messages-lists.html', {
        'new_messages': newMessages,
        'conversations': conversations
    })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def requests(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    form = FilterRequestsForm()
    return render(request, 'manager/manager-dashboard-requests.html', {
        'form': form,
        'new_messages': newMessages
    })


def get_applications(request):
    if request.method == 'GET':
        receiver_name = request.GET.get('the_post')
        applications = CoopApplication.objects.filter(application__user__user__username=receiver_name)
        results = []
        for application in applications:
            event_json = {}
            event_json['id'] = application.facility.id
            event_json['label'] = application.facility.title
            event_json['value'] = application.facility.title
            results.append(event_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def manager_header_array(index):
    array = ["", "", "", "", "", "", ""]
    array[index] = "active"
    return array


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def faqs(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    all_faq = Question.objects.all()

    return render(request, 'manager/manager-dashboard-faq.html', {
        'faqs': all_faq,
        'new_messages': newMessages
    })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def new_faq(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    if request.method == "POST":
        faq_question_text = request.POST['question']
        faq_answer_text = request.POST['answer']

        error = ['', '']
        is_valid = True
        if not faq_question_text or faq_question_text == "":
            is_valid = False
            error[0] = 'error'
        if not faq_answer_text or faq_answer_text == "":
            is_valid = False
            error[1] = 'error'
        if not is_valid:
            return render(request, 'manager/manager-dashboard-faq-new.html', {
                'prev_question': faq_question_text,
                'prev_answer': faq_answer_text,
                'new_messages': newMessages,
                'errors': error
            })

        Question.objects.create(question_text=faq_question_text, answer_text=faq_answer_text)
        return HttpResponseRedirect('/manager/faqs/')
    else:
        return render(request, 'manager/manager-dashboard-faq-new.html',{'new_messages': newMessages,})


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def edit_faq(request, faq_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    faq = get_object_or_404(Question, pk=faq_id)
    if request.method == "POST":
        faq_question_text = request.POST['question']
        faq_answer_text = request.POST['answer']

        error = ['', '']
        is_valid = True
        if not faq_question_text or faq_question_text == "":
            is_valid = False
            error[0] = 'error'
        if not faq_answer_text or faq_answer_text == "":
            is_valid = False
            error[1] = 'error'

        if not is_valid:
            return render(request, 'manager/manager-dashboard-faq-edit.html', {
                'faq': faq,
                'errors': error,
                'new_messages': newMessages,
            })

        faq.question_text = faq_question_text
        faq.answer_text = faq_answer_text
        faq.save()
        return HttpResponseRedirect('/manager/faqs/')
    else:
        return render(request, 'manager/manager-dashboard-faq-edit.html', {
            'new_messages': newMessages,
            'faq': faq
        })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def delete_faq(request, faq_id):
    faq = get_object_or_404(Question, pk=faq_id)
    faq.delete()
    return HttpResponseRedirect('/manager/faqs/')


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def notices(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    notices = Notice.objects.all()[0:10:-1]
    return render(request, 'manager/manager-dashboard-notices.html', {
        'new_messages': newMessages,
        'notices': notices
    })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def new_notice(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    if request.method == 'GET':
        form = NoticeForm()
        return render(request, 'manager/manager-dashboard-notices-new.html', {
            'new_messages': newMessages,
            'form': form
        })

    else:
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = Notice.objects.create(
                title=form.cleaned_data['title'],
                notice_text=form.cleaned_data['notice_text'],
                initiation_date=jdate_to_date(form.cleaned_data['start_date']),
                expiration_date=jdate_to_date(form.cleaned_data['end_date']),
            )
            notice.attachment = attachment = form.cleaned_data['attachment']
            notice.save()
            return HttpResponseRedirect('/manager/notices/')
        else:
            return render(request, 'manager/manager-dashboard-notices-new.html', {
                'new_messages': newMessages,
                'form': form
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def edit_notice(request, notice_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    notice = get_object_or_404(Notice, pk=notice_id)
    start_date = jdatetime.GregorianToJalali(gmonth=notice.initiation_date.month, gyear=notice.initiation_date.year,
                                             gday=notice.initiation_date.day).getJalaliList()
    end_date = jdatetime.GregorianToJalali(gmonth=notice.expiration_date.month, gyear=notice.expiration_date.year,
                                           gday=notice.expiration_date.day).getJalaliList()
    if request.method == 'GET':
        form = NoticeForm(
            instance=notice,
            initial={
                'start_date': gdate_to_str(start_date),
                'end_date': gdate_to_str(end_date),
                'attachment': None
            }
        )
        return render(request, 'manager/manager-dashboard-notices-edit.html', {
            'new_messages': newMessages,
            'form': form,
            'notice': notice,
        })
    else:
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice.title = form.cleaned_data['title']
            notice.notice_text = form.cleaned_data['notice_text']
            notice.initiation_date = jdate_to_date(form.cleaned_data['start_date'])
            notice.expiration_date = jdate_to_date(form.cleaned_data['end_date'])

            clear_attachment = request.POST.get('clear_attachment', None)

            if clear_attachment:
                if request.POST['clear_attachment']:
                    notice.attachment = None

            notice.attachment = form.cleaned_data['attachment']
            notice.save()

            return HttpResponseRedirect('/manager/notices/')
        else:
            return render(request, 'manager/manager-dashboard-notices-edit.html', {
                'new_messages': newMessages,
                'form': form,
                'notice': notice,
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def delete_notice(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    notice.delete()
    return HttpResponseRedirect('/manager/notices/')


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def notices_all(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    return render(request, 'manager/manager-dashboard-notices-all.html', {
        'new_messages': newMessages,
        'notices': Notice.objects.all()[::-1]
    })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def news(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    news = News.objects.all()[0:10:-1]
    return render(request, 'manager/manager-dashboard-news.html', {
        'new_messages': newMessages,
        'news': news,
    })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def new_news(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    if request.method == 'GET':
        form = NewsForm()
        return render(request, 'manager/manager-dashboard-news-new.html', {
            'new_messages': newMessages,
            'form': form
        })
    else:
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = News.objects.create(
                title=form.cleaned_data['title'],
                news_text=form.cleaned_data['news_text'],
            )
            if form.cleaned_data['attachment']:
                news.attachment = form.cleaned_data['attachment']
                news.save()

            return HttpResponseRedirect('/manager/news/')
        else:
            return render(request, 'manager/manager-dashboard-news-new.html', {
                'new_messages': newMessages,
                'form': form
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def edit_news(request, news_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    new = get_object_or_404(News, pk=news_id)
    if request.method == 'GET':
        form = NewsForm(
            instance=new,
            initial={
                'attachment': None
            }
        )
        return render(request, 'manager/manager-dashboard-news-edit.html', {
            'new_messages': newMessages,
            'form': form,
            'new': new,
        })
    else:
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            new.title = form.cleaned_data['title']
            new.news_text = form.cleaned_data['news_text']
            if request.POST.get('clear_attachment', None):
                new.attachment = None
            new.attachment = form.cleaned_data['attachment']
            new.save()
            return HttpResponseRedirect('/manager/news/')


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def delete_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    news.delete()
    return HttpResponseRedirect('/manager/news/')


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def news_all(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    news = News.objects.all()[::-1]
    return render(request, 'manager/manager-dashboard-news-all.html', {
        'new_messages': newMessages,
        'news': news,
    })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def jdate_to_date(date_string):
    return jdatetime.date(int(date_string.split('/')[0]),
                          int(date_string.split('/')[1]),
                          int(date_string.split('/')[2])).togregorian()


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def facilities(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    if request.method == "GET":
        form = FacilityForm()
        return render(request, 'manager/manager-dashboard-facilities.html', {
            'new_messages': newMessages,
            'form': form,
            'facilities': Facility.objects.all()
        })
    else:
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/manager/facilities/')
        else:
            return render(request, 'manager/manager-dashboard-facilities.html', {
                'new_messages': newMessages,
                'form': form,
                'facilities': Facility.objects.all()
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def delete_facility(request, fac_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    facility = Facility.objects.get(pk=fac_id)
    applications = CoopApplication.objects.filter(facility=facility)
    if request.method == "GET":
        return render(request, 'manager/manager-dashboard-facilities-delete.html', {
            'new_messages': newMessages,
            'facility': facility,
            'applications': applications
        })
    elif request.method == "POST":
        for application in applications:
            application.delete()
        facility.delete()
        return HttpResponseRedirect("/manager/facilities/")


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def edit_facility(request, fac_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    facility = Facility.objects.get(pk=fac_id)
    if request.method == "GET":
        form = FacilityForm(instance=facility)
        return render(request, 'manager/manager-dashboard-facilities-edit.html', {
            'new_messages': newMessages,
            'form': form,
            'facility': facility,
        })
    elif request.method == "POST":
        form = FacilityForm(request.POST)
        if form.is_valid():
            facility.title = form.cleaned_data['title']
            facility.save()
            return HttpResponseRedirect("/manager/facilities/")
        else:
            return render(request, 'manager/manager-dashboard-facilities-edit.html', {
                'new_messages': newMessages,
                'form': form,
                'facility': facility,
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def fields(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    if request.method == "GET":
        form = FieldForm()
        return render(request, 'manager/manager-dashboard-fields.html', {
            'new_messages': newMessages,
            'form': form,
            'fields': Field.objects.all()
        })
    else:
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/manager/fields/')
        else:
            return render(request, 'manager/manager-dashboard-fields.html', {
                'new_messages': newMessages,
                'form': form,
                'fields': Field.objects.all()
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def delete_field(request, field_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    field = Field.objects.get(pk=field_id)
    if request.method == "GET":
        return render(request, 'manager/manager-dashboard-fields-delete.html', {
            'new_messages': newMessages,
            'field': field,
            'users': BMNUser.objects.filter(field=field)
        })
    elif request.method == "POST":
        users = BMNUser.objects.filter(field=field)
        for user in users:
            user.delete()
        field.delete()
        return HttpResponseRedirect("/manager/fields/")


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def edit_field(request, field_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    field = Field.objects.get(pk=field_id)
    if request.method == "GET":
        form = FieldForm(instance=field)
        return render(request, 'manager/manager-dashboard-fields-edit.html', {
            'new_messages': newMessages,
            'form': form,
            'field': field,
        })
    elif request.method == "POST":
        form = FieldForm(request.POST)
        if form.is_valid():
            field.title = form.cleaned_data['title']
            field.save()
            return HttpResponseRedirect("/manager/fields/")
        else:
            return render(request, 'manager/manager-dashboard-fields-edit.html', {
                'form': form,
                'new_messages': newMessages,
                'field': field,
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def associations(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    return render(request, 'manager/manager-dashboard-associations.html', {
        'new_messages': newMessages,
        'associations': Association.objects.all()
    })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def new_association(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    if request.method == "GET":
        form = AssociationForm()
        return render(request, 'manager/manager-dashboard-associations-new.html', {
            'new_messages': newMessages,
            'form': form,
        })
    elif request.method == "POST":
        form = AssociationForm(request.POST, request.FILES)
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['password_repeat']
        errors = validate_association_data(name, username, email, password, repeat_password)

        if errors:
            return render(request, 'manager/manager-dashboard-associations-new.html', {
                'new_messages': newMessages,
                'errors': errors,
                'form': form,
                'username': username,
                'name': name,
                'email': email,
            })

        if form.is_valid():
            user = User.objects.create(username=request.POST['username'], password=request.POST['password'],
                                       email=request.POST['email'], first_name=request.POST['name'])

            association = Association(user=user, url=form.cleaned_data['url'], logo=form.cleaned_data['logo'])
            association.save()

            for field in form.cleaned_data.get('fields'):
                field.associations.add(association)
                field.save()
            for facility in form.cleaned_data.get('facilities'):
                facility.associations.add(association)
                facility.save()

            association.fields = form.cleaned_data['fields']
            association.facilities = form.cleaned_data['facilities']
            association.save()

            return HttpResponseRedirect("/manager/associations/")
        else:
            return render(request, 'manager/manager-dashboard-associations-new.html', {
                'new_messages': newMessages,
                'errors': errors,
                'form': form,
                'username': username,
                'name': name,
                'email': email,
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def edit_association(request, assoc_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    association = Association.objects.get(pk=assoc_id)
    if request.method == "GET":
        form = AssociationForm(instance=association)
        return render(request, 'manager/manager-dashboard-associations-edit.html', {
            'new_messages': newMessages,
            'form': form,
            'association': association,
        })

    elif request.method == "POST":
        form = AssociationForm(request.POST, request.FILES)
        if form.is_valid():
            association.fields = form.cleaned_data['fields']
            association.facilities = form.cleaned_data['facilities']
            association.url = form.cleaned_data['url']
            association.logo = form.clenaed_data['logo']
            association.save()

            return HttpResponseRedirect("/manager/associations/")
        else:
            return render(request, 'manager/manager-dashboard-associations-new.html', {
                'new_messages': newMessages,
                'form': form,
                'association': association,
            })


@user_passes_test(is_manager, login_url='/manager/login/', redirect_field_name=None)
@login_required(login_url='/manager/')
def delete_association(request, assoc_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    association = Association.objects.get(pk=assoc_id)
    applications = CoopApplication.objects.filter(association=association)
    if request.method == "GET":
        return render(request, 'manager/manager-dashboard-associations-delete.html', {
            'new_messages': newMessages,
            'association': association,
            'applications': applications
        })
    elif request.method == "POST":
        for application in applications:
            application.delete()
        association.delete()
        return HttpResponseRedirect("/manager/associations/")


def gdate_to_str(date_obj):
    return date_obj[0].__str__() + "/" + date_obj[1].__str__() + "/" + date_obj[2].__str__()


def get_association(request):
    pass


def compose_message(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    return render( request, 'manager/manager-dashboard-message-new.html')


def compose_message_submit(request):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    if request.method == "POST":
        title = request.POST.get("title")
        receiver = request.POST.get("receiver")
        content = request.POST.get("content")
        facility = request.POST.get("applications")
        conversation = Conversation()
        message = Message()
        conversation.title = title
        user = User.objects.all().filter(username=receiver)[0]
        conversation.receiver = user
        conversation.sender = request.user
        message.reciever = user
        message.text = content
        message.sender = request.user
        application = CoopApplication.objects.filter(application__user__user=user, facility__title=facility)[0]
        message.application = application.application
        conversation.save()
        message.conversation = conversation
        message.save()

    return HttpResponseRedirect("/manager/messages/")


def ajax_search(request):
    if request.is_ajax():
        users = User.objects.filter(username__contains=request.GET.get('term', ''))
        results = []
        for user in users:
            event_json = {}
            event_json['id'] = user.username
            event_json['label'] = user.username
            event_json['value'] = user.username
            results.append(event_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def conversation(request, conversation_id):
    conversations = Conversation.objects.all().filter(receiver=request.user).order_by('-lastMessageTime')
    newMessages = 0
    for conversation in conversations:
        if conversation.is_read == False:
            newMessages += 1
    conversation = Conversation.objects.get(id=conversation_id)
    Conversation.objects.all().filter(id = conversation_id).update(is_read = True)
    messages = Message.objects.filter(conversation=conversation)
    return render(request, 'manager/manager-dashboard-messages-detail.html', {
        'new_messages': newMessages,
        'conversation': conversation,
        'messages': messages
    })


def conversation_reply(request, conversation_id):
    if request.method == "POST":
        text = request.POST["replyText"]
        print(text)
        conversation = Conversation.objects.get(id=conversation_id)
        if conversation.receiver2 is None:

            print("new message")
            conversation.receiver2 = conversation.sender
            print(conversation.id)
            # conversation.lastMessageTime=datetime.datetime.now()
            conversation.update(lastMessageTime=datetime.datetime.now())
            message = Message()
            message.text = text
            message.reciever = conversation.sender
            message.sender = request.user
            message.conversation = conversation
            message.save()
            print(message.id)
        return HttpResponseRedirect('/')