from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Organisation, Project, Encoder, Donation


@csrf_exempt
def get_user(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    return JsonResponse(Encoder().encode(user), safe=False)


@csrf_exempt
def create_user(request):
    user = User()
    user.email = request.POST.get('email', None)
    user.password = request.POST.get('password', None)
    if user.email or user.password is None:
        return HttpResponseBadRequest()
    user.first_name = request.POST.get('first_name', None)
    user.second_name = request.POST.get('second_name', None)
    user.birthday = request.POST.get('birthday', None)
    user.country = request.POST.get('country', None)
    user.save()
    return JsonResponse({'email': user.email, 'id': user.pk}, safe=False)


@csrf_exempt
def change_password(request):
    id = request.GET.get('id', None)
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseBadRequest()

    old_password = request.POST.get('old password', None)
    if old_password is not user.password:
        return HttpResponseBadRequest()

    new_password = request.POST.get('new password', None)
    if new_password is None:
        return HttpResponseBadRequest()
    user.password = new_password
    user.save()
    return HttpResponse()


@csrf_exempt
def restore_password(request):
    email = request.GET.get('email', None)
    if email is None:
        return HttpResponseBadRequest()
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    return HttpResponse()


@csrf_exempt
def create_new_password(request):
    id = request.GET.get('id', None)
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    new_password = request.POST.get('new password', None)
    if new_password is None:
        return HttpResponseBadRequest()
    user.password = new_password
    user.save()
    return HttpResponse()


@csrf_exempt
def login(request):
    email = request.GET.get('email', None)
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    password = request.POST.get('password', None)
    if password == user.password:
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def logout(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    return HttpResponse()


@csrf_exempt
def update_profile(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    user.first_name = request.POST.get('first_name', None)
    user.second_name = request.POST.get('second_name', None)
    user.birthday = request.POST.get('birthday', None)
    user.country = request.POST.get('country', None)
    user.save()
    return HttpResponse()


@csrf_exempt
def change_email(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    new_email = request.POST.get('new_email', None)
    if new_email is None:
        return HttpResponseBadRequest()
    user.email = new_email
    user.save()
    return HttpResponse()


@csrf_exempt
def current_donations(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    donation = user.donations
    return JsonResponse(Encoder().encode(donation), safe=False)


@csrf_exempt
def get_projects(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return HttpResponseBadRequest()
    return JsonResponse(Encoder().encode(project), safe=False)


@csrf_exempt
def get_project(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return HttpResponseBadRequest()
    return JsonResponse(Encoder().encode(project), safe=False)


@csrf_exempt
def get_organisations(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        organisation = Organisation.objects.get(pk=id)
    except Organisation.DoesNotExist:
        return HttpResponseBadRequest()
    return JsonResponse(Encoder().encode(organisation), safe=False)


@csrf_exempt
def donate_organization(request):
    donate = Donation()
    id = request.GET.get('id', None)
    organisation_id = request.GET.get('organisation id', None)
    if id is None or organisation_id is None:
        return HttpResponseBadRequest()
    try:
        organisation = Organisation.objects.get(pk=organisation_id)
    except Organisation.DoesNotExist:
        return HttpResponseBadRequest()
    return None


@csrf_exempt
def donate_project(request):
    id = request.GET.get('id', None)
    project_id = request.GET.get('project id', None)
    if id is None or project_id is None:
        return HttpResponseBadRequest()
    try:
        user = User.objects.get(pk=id)
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist or User.DoesNotExist:
        return HttpResponseBadRequest()
    return None


@csrf_exempt
def delete_donate(request):
    id = request.GET.get('id', None)
    period = request.GET.get('period', None)
    sum = request.GET.get('sum', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        donate = Donation.objects.get(pk=id)
    except Donation.DoesNotExist:
        return HttpResponseBadRequest()
    donate.delete()
    return HttpResponse()
