from django.forms import modelformset_factory
import jdatetime
from django.shortcuts import render
from users.views import jdate_to_date
from cons.models import MilitaryApplication, EducationalBackground, TeachingExperience, JournalPaper, \
    ResearchExperience, \
    InternalInvention, InternationalInvention, TopRankingBackground, OlympiadRanking, InternalResearchPaper, \
    ConferencePapers, JobOffers, Scholarship, ResearchGrant, PostDocBackground, Memberships, EditorsMembership, Notes
from users.models import BMNUser, Application
from cons.forms import MilitaryApplicationForm, EducationForm, TeachingForm, InternationalPapersForm, \
    InternalPapersForm, \
    ResearchExperienceForm, InternalInventionForm, RankingForm, OlympiadRankingForm, ConferencePaperForm, OffersForm, \
    ScholarshipForm, GrantForm, PostDocForm, MembershipForm, EditorsForm, MyNoteForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


@login_required(login_url='/login/')
def dashboard(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    if request.method == "GET":
        try:
            application = MilitaryApplication.objects.get(application__user=bmn_user)
        except ObjectDoesNotExist:
            form = MilitaryApplicationForm()
            return render(request, 'cons/basic-info-form.html', {
                'form': form
            })
        except MultipleObjectsReturned:
            return HttpResponse("System Error. Please contact the administrator.")

        return render(request, 'cons/user-dashboard-app.html', {
            'military_application': application,
        })
    if request.method == "POST":
        form = MilitaryApplicationForm(request.POST, request.FILES)
        if form.is_valid():

            application = Application.objects.create(user=bmn_user)

            in_country_period_end = jdate_to_date(form.cleaned_data['begin_date'])
            in_country_period_start = jdate_to_date(form.cleaned_data['end_date'])

            consapp = MilitaryApplication(
                application=application,
                personneli_photo=form.cleaned_data['personneli_photo'],
                national_id_photo=form.cleaned_data['national_id_photo'],
                social_id_number=form.cleaned_data['social_id_number'],
                marital_status=form.cleaned_data['marital_status'],
                national_booklet_photo=form.cleaned_data['national_booklet_photo'],
                inner_phone_number=form.cleaned_data['inner_phone_number'],
                outer_phone_number=form.cleaned_data['outer_phone_number'],
                in_country_period_start=in_country_period_start,
                in_country_period_end=in_country_period_end,
                resume=form.cleaned_data['resume'],
            )
            consapp.save()
            return HttpResponseRedirect("/users/cons/")
        else:
            return render(request, 'cons/basic-info-form.html', {
                'form': form
            })


@login_required(login_url='/users/')
def app(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    if request.method == "GET":
        try:
            application = MilitaryApplication.objects.get(application__user=bmn_user)
        except ObjectDoesNotExist:
            return HttpResponseRedirect("/cons/")
        except MultipleObjectsReturned:
            return HttpResponse("System Error. Please contact the administrator.")
        return render(request, 'cons/user-dashboard-app.html', {
            'military_application': application,
        })


@login_required(login_url='/login/')
def education(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        mil_application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    EducationFomset = modelformset_factory(model=EducationalBackground, form=EducationForm)

    if request.method == "GET":
        formset = EducationFomset(queryset=mil_application.educational_backgrounds.all())
        megalist = zip(formset.forms, mil_application.educational_backgrounds.all())
        for form, education in megalist:
            temp_begin_date = to_jdate(education.start_of_education_date)
            temp_end_date = to_jdate(education.end_of_education_date)
            form.fields['begin_date'].initial = temp_begin_date
            form.fields['end_date'].initial = temp_end_date

        return render(request, 'cons/education-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = EducationFomset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not EducationalBackground.objects.filter(id=form_id):
                        education = EducationalBackground(
                            title=form.cleaned_data['title'],
                            country=form.cleaned_data['country'],
                            education_major=form.cleaned_data['education_major'],
                            university=form.cleaned_data['university'],
                            photo_of_document=form.cleaned_data['photo_of_document'],
                            gpa=form.cleaned_data['gpa'],
                            photo_of_grades=form.cleaned_data['photo_of_grades'],
                            vezarat_proof=form.cleaned_data['vezarat_proof'],
                            start_of_education_date=jdate_to_date(form.cleaned_data['begin_date']),
                            end_of_education_date=jdate_to_date(form.cleaned_data['end_date']),
                        )
                        education.application = mil_application
                        education.save()
                    else:
                        education = EducationalBackground.objects.get(id=form_id)
                        education.title = form.cleaned_data['title']
                        education.country = form.cleaned_data['country']
                        education.education_major = form.cleaned_data['education_major']
                        education.university = form.cleaned_data['university']
                        education.photo_of_document = form.cleaned_data['photo_of_document']
                        education.gpa = form.cleaned_data['gpa']
                        education.photo_of_grades = form.cleaned_data['photo_of_grades']
                        education.vezarat_proof = form.cleaned_data['vezarat_proof']
                        education.start_of_education_date = jdate_to_date(form.cleaned_data['begin_date'])
                        education.end_of_education_date = jdate_to_date(form.cleaned_data['end_date'])
                        education.save()

            mil_application.educational_background_completed = True
            mil_application.save()
            return HttpResponseRedirect("/users/cons/")
        else:
            return render(request, 'cons/education-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def teaching_experience(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    TeachingFormset = modelformset_factory(model=TeachingExperience, form=TeachingForm)

    if request.method == "GET":

        TeachingFormset = TeachingFormset(queryset=application.teaching_experiences.all())

        return render(request, 'cons/teaching-info-form.html', {
            'formset': TeachingFormset,
        })

    elif request.method == "POST":
        formset = TeachingFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not TeachingExperience.objects.filter(id=form_id):
                        teaching_experiece_obj = TeachingExperience(
                            application=application,
                            university=form.cleaned_data['university'],
                            type_of_teaching=form.cleaned_data['type_of_teaching'],
                            length=form.cleaned_data['length'],
                            photo_of_teaching_certificate=form.cleaned_data['photo_of_teaching_certificate'],
                        )
                        teaching_experiece_obj.save()
                    else:
                        teaching_experiece_obj = TeachingExperience.objects.get(id=form_id)
                        teaching_experiece_obj.application = application
                        teaching_experiece_obj.university = form.cleaned_data['university']
                        teaching_experiece_obj.type_of_teaching = form.cleaned_data['type_of_teaching']
                        teaching_experiece_obj.length = form.cleaned_data['length']
                        teaching_experiece_obj.photo_of_teaching_certificate = form.cleaned_data[
                            'photo_of_teaching_certificate']
                        teaching_experiece_obj.save()

            application.teaching_background_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/teaching-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def international_papers(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    InternationalPapersFormset = modelformset_factory(model=JournalPaper, form=InternationalPapersForm)
    formset = InternationalPapersFormset(queryset=application.journal_papers.all())

    if request.method == "GET":
        return render(request, 'cons/journal-papers-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = InternationalPapersFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not JournalPaper.objects.filter(id=form_id):
                        paper = JournalPaper(
                            application=application,
                            paper_title=form.cleaned_data['paper_title'],
                            journal_title=form.cleaned_data['journal_title'],
                            total_number_of_authors=form.cleaned_data['total_number_of_authors'],
                            applicants_location_in_authors=form.cleaned_data['applicants_location_in_authors'],
                            link=form.cleaned_data['link'],
                        )
                        paper.save()

                    else:
                        paper = JournalPaper.objects.get(id=form_id)
                        paper.paper_title = form.cleaned_data['paper_title']
                        paper.journal_title = form.cleaned_data['journal_title']
                        paper.total_number_of_authors = form.cleaned_data['total_number_of_authors']
                        paper.applicants_location_in_authors = form.cleaned_data['applicants_location_in_authors']
                        paper.link = form.cleaned_data['link']
                        paper.save()

            application.international_papers_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/journal-papers-info-form.html', {
                'formset': formset,
            })

    else:
        return render(request, 'cons/teaching-info-form.html', {
            'formset': formset,
        })


@login_required(login_url='/login/')
def internal_papers(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    InternalPapersFormset = modelformset_factory(model=InternalResearchPaper, form=InternalPapersForm)
    formset = InternalPapersFormset(queryset=application.internal_journal_papers.all())

    if request.method == "GET":
        for form, paper in zip(formset.forms, application.internal_journal_papers.all()):
            temp_pub_date = to_jdate(paper.publish_date)
            form.fields['publish_date'].initial = temp_pub_date

        return render(request, 'cons/internal-papers-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = InternalPapersFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not InternalResearchPaper.objects.filter(id=form_id):
                        paper = InternalResearchPaper(
                            application=application,
                            publish_date=jdate_to_date(form.cleaned_data['publish_date']),
                            paper_title=form.cleaned_data['paper_title'],
                            journal_title=form.cleaned_data['journal_title'],
                            total_number_of_authors=form.cleaned_data['total_number_of_authors'],
                            applicants_location_in_authors=form.cleaned_data['applicants_location_in_authors'],
                            link=form.cleaned_data['link'],
                        )
                        paper.save()

                    else:
                        paper = InternalResearchPaper.objects.get(id=form_id)
                        paper.publish_date = jdate_to_date(form.cleaned_data['publish_date'])
                        paper.paper_title = form.cleaned_data['paper_title']
                        paper.journal_title = form.cleaned_data['journal_title']
                        paper.total_number_of_authors = form.cleaned_data['total_number_of_authors']
                        paper.applicants_location_in_authors = form.cleaned_data['applicants_location_in_authors']
                        paper.link = form.cleaned_data['link']
                        paper.save()

            application.internal_papers_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")
        else:
            return render(request, 'cons/internal-papers-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login')
def confpapers(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    ConferencePaperFormset = modelformset_factory(model=ConferencePapers, form=ConferencePaperForm)
    formset = ConferencePaperFormset(queryset=application.conference_papers.all())

    if request.method == "GET":
        for form, paper in zip(formset.forms, application.conference_papers.all()):
            temp_pub_date = paper.publish_date
            form.fields['publish_date'].initial = to_jdate(temp_pub_date)
        return render(request, 'cons/conference-papers-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = ConferencePaperFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset.forms:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not ConferencePapers.objects.filter(id=form_id):
                        paper = ConferencePapers(
                            application=application,
                            publish_date=jdate_to_date(form.cleaned_data['publish_date']),
                            paper_title=form.cleaned_data['paper_title'],
                            conference_title=form.cleaned_data['conference_title'],
                            total_number_of_authors=form.cleaned_data['total_number_of_authors'],
                            applicants_location_in_authors=form.cleaned_data['applicants_location_in_authors'],
                            link=form.cleaned_data['link'],
                        )
                        paper.save()
                    else:
                        paper = ConferencePapers.objects.get(id=form_id)
                        paper.publish_date = jdate_to_date(form.cleaned_data['publish_date'])
                        paper.paper_title = form.cleaned_data['paper_title']
                        paper.conference_title = form.cleaned_data['conference_title']
                        paper.total_number_of_authors = form.cleaned_data['total_number_of_authors']
                        paper.applicants_location_in_authors = form.cleaned_data['applicants_location_in_authors']
                        paper.link = form.cleaned_data['link']
                        paper.save()
            application.conference_papers_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")
        else:
            return render(request, 'cons/conference-papers-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def research(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    ResearchFormset = modelformset_factory(model=ResearchExperience, form=ResearchExperienceForm)
    formset = ResearchFormset(queryset=application.research_experiences.all())

    if request.method == "GET":
        return render(request, 'cons/research-experience-info-form.html', {
            'formset': formset,
        })
    elif request.method == "POST":
        formset = ResearchFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not ResearchExperience.objects.filter(id=form_id):
                        research_experience = ResearchExperience(
                            application=application,
                            university=form.cleaned_data['university'],
                            length=form.cleaned_data['length'],
                            image_of_research_certificate=form.cleaned_data['image_of_research_certificate'],
                            title=form.cleaned_data['title'],
                        )
                        research_experience.save()
                    else:
                        research_experience = ResearchExperience.objects.get(id=form_id)
                        research_experience.university = form.cleaned_data['university']
                        research_experience.length = form.cleaned_data['length']
                        research_experience.image_of_research_certificate = form.cleaned_data[
                            'image_of_research_certificate']
                        research_experience.title = form.cleaned_data['title']
                        research_experience.save()

            application.research_experience_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/research-experience-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def internal_inventions(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    InventionFormset = modelformset_factory(model=InternalInvention, form=InternalInventionForm)
    formset = InventionFormset(queryset=application.internal_inventions.all())

    if request.method == "GET":
        return render(request, 'cons/internal-inventions-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = InventionFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not InternalInvention.objects.filter(id=form_id):
                        invention = InternalInvention(
                            application=application,
                            invention_title=form.cleaned_data['invention_title'],
                            number_of_all_partners=form.cleaned_data['number_of_all_partners'],
                            applicants_location_in_partners=form.cleaned_data['applicants_location_in_partners'],
                            invention_number=form.cleaned_data['invention_number'],
                            certificate=form.cleaned_data['certificate'],
                            invention_level=form.cleaned_data['invention_level'],
                        )
                        invention.save()
                    else:
                        invention = InternalInvention.objects.get(id=form_id)
                        invention.invention_title = form.cleaned_data['invention_title']
                        invention.number_of_all_partners = form.cleaned_data['number_of_all_partners']
                        invention.applicants_location_in_partners = form.cleaned_data['applicants_location_in_partners']
                        invention.invention_number = form.cleaned_data['invention_number']
                        invention.certificate = form.cleaned_data['certificate']
                        invention.invention_level = form.cleaned_data['invention_level']

                        invention.save()

            application.internal_inventions_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/internal-inventions-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def international_inventions(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    InternationalInventionFormset = modelformset_factory(model=InternationalInvention, form=InternalInventionForm)
    formset = InternationalInventionFormset(queryset=application.internaional_inventions.all())

    if request.method == "GET":
        for form, obj in zip(formset.forms, application.internaional_inventions.all()):
            form.fields['link'].initial = obj.link

        return render(request, 'cons/international-inventions-info-form.html', {
            'formset': formset,
        })
    elif request.method == "POST":
        formset = InternationalInventionFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not InternationalInvention.objects.filter(id=form_id):
                        invention = InternationalInvention(
                            application=application,
                            invention_title=form.cleaned_data['invention_title'],
                            number_of_all_partners=form.cleaned_data['number_of_all_partners'],
                            applicants_location_in_partners=form.cleaned_data['applicants_location_in_partners'],
                            patent_type=form.cleaned_data['patent_type'],
                        )
                        invention.save()
                    else:
                        invention = InternationalInvention.objects.get(id=form)
                        invention.invention_title = form.cleaned_data['invention_title']
                        invention.number_of_all_partners = form.cleaned_data['number_of_all_partners']
                        invention.applicants_location_in_partners = form.cleaned_data['applicants_location_in_partners']
                        invention.patent_type = form.cleaned_data['patent_type']
                        invention.save()

            application.international_inventions_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")
        else:
            return render(request, 'cons/international-inventions-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def postdoc(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    PostDocFormset = modelformset_factory(model=PostDocBackground, form=PostDocForm)
    formset = PostDocFormset(queryset=application.post_docs.all())

    if request.method == "GET":
        for form, obj in zip(formset.forms, application.post_docs.all()):
            temp_start = to_jdate(obj.start_of_postdoc_date)
            temp_end = to_jdate(obj.end_of_postdoc_date)
            form.fields['start_date'].initial = temp_start
            form.fields['end_date'].initial = temp_end

        return render(request, 'cons/postdoc-info-form.html', {
            'formset': formset
        })

    elif request.method == "POST":
        formset = PostDocFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset.forms:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not PostDocBackground.objects.filter(id=form_id):
                        postdoc = PostDocBackground(
                            application=application,
                            university=form.cleaned_data['university'],
                            photo_of_document=form.cleaned_data['photo_of_document'],
                            start_of_postdoc_date=jdate_to_date(form.cleaned_data['start_date']),
                            end_of_postdoc_date=jdate_to_date(form.cleaned_data['end_date']),
                        )
                        postdoc.save()

                    else:
                        postdoc = PostDocBackground.objects.get(id=form_id)
                        postdoc.university = form.cleaned_data['university']
                        postdoc.photo_of_document = form.cleaned_data['photo_of_document']
                        postdoc.start_of_postdoc_date = jdate_to_date(form.cleaned_data['start_date'])
                        postdoc.end_of_postdoc_date = jdate_to_date(form.cleaned_data['end_date'])

                        postdoc.save()

            application.postdoc_backgournd_completed = True
            application.save()
            return HttpResponseRedirect('/users/cons/')
        else:
            return render(request, 'cons/postdoc-info-form.html', {
                'formset': formset
            })


@login_required(login_url='/login/')
def memberships(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    MembershipFormset = modelformset_factory(model=Memberships, form=MembershipForm)
    formset = MembershipFormset(queryset=application.memberships.all())

    if request.method == "GET":
        return render(request, 'cons/memberships-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = MembershipFormset(request.POST)
        if formset.is_valid():
            for form in formset.forms:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not Memberships.objects.filter(id=form_id):
                        membership = Memberships(
                            application=application,
                            title_of_association=form.cleaned_data['title_of_association'],
                            membership_type=form.cleaned_data['membership_type'],
                            length=form.cleaned_data['length'],
                        )
                        membership.save()

                    else:
                        membership = Memberships.objects.get(id=form_id)
                        membership.title_of_association = form.cleaned_data['title_of_association']
                        membership.membership_type = form.cleaned_data['membership_type']
                        membership.length = form.cleaned_data['length']

                        membership.save()

            application.memberships_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/memberships-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def editors(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    EditorsFormset = modelformset_factory(model=EditorsMembership, form=EditorsForm)
    formset = EditorsFormset(queryset=application.editors_membership.all())

    if request.method == "GET":
        return render(request, 'cons/editors-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = EditorsFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset.forms:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not EditorsMembership.objects.filter(id=form_id):
                        editor = EditorsMembership(
                            application=application,
                            title=form.cleaned_data['title'],
                            position=form.cleaned_data['position'],
                            length=form.cleaned_data['length'],
                            photo_of_certificate=form.cleaned_data['photo_of_certificate'],
                        )
                        editor.save()
                    else:
                        editor = EditorsMembership.objects.get(id=form_id)
                        editor.title = form.cleaned_data['title']
                        editor.position = form.cleaned_data['position']
                        editor.length = form.cleaned_data['length']
                        editor.photo_of_certificate = form.cleaned_data['photo_of_certificate']

                        editor.save()

            application.editors_memberships_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/editors-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def rankings(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    RankingsFormset = modelformset_factory(model=TopRankingBackground, form=RankingForm)
    formset = RankingsFormset(queryset=application.ranking_backgrounds.all())

    if request.method == "GET":
        return render(request, 'cons/top-rankings-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = RankingsFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not TopRankingBackground.objects.filter(id=form_id):
                        ranking = TopRankingBackground(
                            application=application,
                            type=form.cleaned_data['type'],
                            rank=form.cleaned_data['rank'],
                            photo_of_certificate=form.cleaned_data['photo_of_certificate'],
                        )
                        ranking.save()
                    else:
                        ranking = TopRankingBackground.objects.get(id=form_id)
                        ranking.type = form.cleaned_data['type']
                        ranking.rank = form.cleaned_data['rank']
                        ranking.photo_of_certificate = form.cleaned_data['photo_of_certificate']
                        ranking.save()

            application.rankings_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/top-rankings-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def olympiads(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    OlympiadsFormset = modelformset_factory(model=OlympiadRanking, form=OlympiadRankingForm)
    formset = OlympiadsFormset(queryset=application.olympiad_ranking.all())

    if request.method == "GET":
        return render(request, 'cons/olympiads-rankings-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = OlympiadsFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not OlympiadRanking.objects.filter(id=form_id):
                        olympiad = OlympiadRanking(
                            application=application,
                            type=form.cleaned_data['type'],
                            title=form.cleaned_data['title'],
                            ranking_or_medal=form.cleaned_data['ranking_or_medal'],
                            photo_of_certificate=form.cleaned_data['photo_of_certificate'],
                        )
                        olympiad.save()
                    else:
                        olympiad = OlympiadRanking.objects.get(id=form_id)
                        olympiad.type = form.cleaned_data['type']
                        olympiad.title = form.cleaned_data['title']
                        olympiad.ranking_or_medal = form.cleaned_data['ranking_or_medal']
                        olympiad.photo_of_certificate = form.cleaned_data['photo_of_certificate']
                        olympiad.save()

            application.olympiads_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/olympiads-rankings-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def offers(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    JobOffersFormset = modelformset_factory(model=JobOffers, form=OffersForm)
    formset = JobOffersFormset(queryset=application.job_offers.all())

    if request.method == "GET":

        for form, obj in zip(formset.forms, application.job_offers.all()):
            temp_start_date = to_jdate(obj.start_date)
            form.fields['start_date'].initial = temp_start_date

        return render(request, 'cons/job-offers-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = JobOffersFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset.forms:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not JobOffers.objects.filter(id=form_id):
                        offer = JobOffers(
                            application=application,
                            title=form.cleaned_data['title'],
                            position=form.cleaned_data['position'],
                            start_date=jdate_to_date(form.cleaned_data['start_date']),
                            photo_of_contract=form.cleaned_data['photo_of_contract'],
                        )
                        offer.save()
                    else:
                        offer = JobOffers.objects.get(id=form_id)
                        offer.title = form.cleaned_data['title']
                        offer.position = form.cleaned_data['position']
                        offer.start_date = jdate_to_date(form.cleaned_data['start_date'])
                        offer.photo_of_contract = form.cleaned_data['photo_of_contract']

                        offer.save()
            application.offers_completed = True
            application.save()

            return HttpResponseRedirect("/users/cons/")
        else:
            return render(request, 'cons/job-offers-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def scholarships(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    ScholarshipsFormset = modelformset_factory(form=ScholarshipForm, model=Scholarship)
    formset = ScholarshipsFormset(queryset=application.scholarships.all())

    if request.method == "GET":

        for form, obj in zip(formset.forms, application.scholarships.all()):
            temp_start_date = to_jdate(obj.start_date)
            temp_end_date = to_jdate(obj.end_date)
            form.fields['start_date'].initial = temp_start_date
            form.fields['end_date'].initial = temp_end_date
        return render(request, 'cons/scholarships-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = ScholarshipsFormset(request.POST, request.FILES)

        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not Scholarship.objects.filter(id=form_id):
                        scholarship = Scholarship(
                            application=application,
                            research_center=form.cleaned_data['research_center'],
                            scholarship_title=form.cleaned_data['scholarship_title'],
                            scholarship_type=form.cleaned_data['scholarship_type'],
                            scholarship_fund=form.cleaned_data['scholarship_fund'],
                            scholarship_currency=form.cleaned_data['scholarship_currency'],
                            start_date=jdate_to_date(form.cleaned_data['start_date']),
                            end_date=jdate_to_date(form.cleaned_data['end_date']),
                            photo_of_certificate=form.cleaned_data['photo_of_certificate'],
                        )
                        scholarship.save()
                    else:
                        scholarship = Scholarship.objects.get(id=form_id)
                        scholarship.research_center = form.cleaned_data['research_center']
                        scholarship.scholarship_title = form.cleaned_data['scholarship_title']
                        scholarship.scholarship_type = form.cleaned_data['scholarship_type']
                        scholarship.scholarship_fund = form.cleaned_data['scholarship_fund']
                        scholarship.scholarship_currency = form.cleaned_data['scholarship_currency']
                        scholarship.start_date = jdate_to_date(form.cleaned_data['start_date'])
                        scholarship.end_date = jdate_to_date(form.cleaned_data['end_date'])
                        scholarship.photo_of_certificate = form.cleaned_data['photo_of_certificate']

                        scholarship.save()
            application.scholarships_completed = True
            application.save()

            return HttpResponseRedirect("/users/cons/")

        else:
            import pdb
            pdb.set_trace()
            return render(request, 'cons/scholarships-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def grants(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    GrantFormset = modelformset_factory(model=ResearchGrant, form=GrantForm)
    formset = GrantFormset(queryset=application.grants.all())

    if request.method == "GET":
        for form, obj in zip(formset.forms, application.grants.all()):
            temp_start_date = to_jdate(obj.start_date)
            temp_end_date = to_jdate(obj.end_date)
            form.fields['start_date'].initial = temp_start_date
            form.fields['end_date'].initial = temp_end_date

        return render(request, 'cons/grants-info-form.html', {
            'formset': formset,
        })

    elif request.method == "POST":
        formset = GrantFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset.forms:
                if form.has_changed():
                    form_id = form.fields['id'].initial
                    if not ResearchGrant.objects.filter(id=form_id):
                        grant = ResearchGrant(
                            application=application,
                            research_center=form.cleaned_data['research_center'],
                            grant_title=form.cleaned_data['grant_title'],
                            grant_fund=form.cleaned_data['grant_fund'],
                            grant_currency=form.cleaned_data['grant_currency'],
                            start_date=jdate_to_date(form.cleaned_data['start_date']),
                            end_date=jdate_to_date(form.cleaned_data['end_date']),
                            photo_of_certificate=form.cleaned_data['photo_of_certificate'],
                        )
                        grant.save()

                    else:
                        grant = ResearchGrant.objects.get(id=form_id)
                        grant.research_center = form.cleaned_data['research_center']
                        grant.grant_title = form.cleaned_data['grant_title']
                        grant.grant_fund = form.cleaned_data['grant_fund']
                        grant.grant_currency = form.cleaned_data['grant_currency']
                        grant.start_date = jdate_to_date(form.cleaned_data['start_date'])
                        grant.end_date = jdate_to_date(form.cleaned_data['end_date'])
                        grant.photo_of_certificate = form.cleaned_data['photo_of_certificate']

                        grant.save()
            application.grants_completed = True
            application.save()

            return HttpResponseRedirect("/users/cons/")
        else:
            return render(request, 'cons/grants-info-form.html', {
                'formset': formset,
            })


@login_required(login_url='/login/')
def notes(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    if request.method == "GET":
        if Notes.objects.filter(application=application):
            note = Notes.objects.get(application=application)
            form = MyNoteForm(instance=note)
        else:
            form = MyNoteForm()
        return render(request, 'cons/notes-info-form.html', {
            'form': form,
        })

    elif request.method == "POST":
        form = MyNoteForm(request.POST)
        if form.is_valid():
            note = Notes(
                application=application,
                text=form.cleaned_data['text']
            )
            note.save()
            application.notes_completed = True
            application.save()
            return HttpResponseRedirect("/users/cons/")

        else:
            return render(request, 'cons/notes-info-form.html', {
                'form': form,
            })


@login_required(login_url='/login/')
def submit(request):
    bmn_user = BMNUser.objects.get(user=request.user)
    try:
        application = MilitaryApplication.objects.get(application__user=bmn_user)
    except ObjectDoesNotExist:
        return HttpResponse("System Error. Please contact the administrator.")
    except MultipleObjectsReturned:
        return HttpResponse("System Error. Please contact the administrator.")

    return


def jdate_to_date(date_string):
    return jdatetime.date(int(date_string.split('/')[0]),
                          int(date_string.split('/')[1]),
                          int(date_string.split('/')[2])).togregorian()


def to_jdate(date):
    return jdatetime.datetime.fromgregorian(datetime=date).strftime('%Y/%m/%d')
