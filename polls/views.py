from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Organisation, Project, UserEncoder


@csrf_exempt
def get_user(request):
    id = request.GET.get('id', None)
    if id is None:
        return HttpResponseBadRequest()
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    return JsonResponse(UserEncoder().encode(user), safe=False)


@csrf_exempt
def create_user(request):
    user = User()
    user.email = request.POST.get('email', None)
    user.password = request.POST.get('password', None)
    user.first_name = request.POST.get('first_name', None)
    user.second_name = request.POST.get('second_name', None)
    user.birthday = request.POST.get('birthday', None)
    user.country = request.POST.get('country', None)
    user.save()
    return JsonResponse(UserEncoder().encode(user), safe=False)


def get_organisations(request):
    organisation = Organisation()
    organisation.name = "test.org"
    organisation.save()
    return JsonResponse(list(Organisation.objects.all().values()), safe=False)


def get_projects(request):
    project = Project()
    project.name = "test.project"
    project.save()
    return JsonResponse(list(Project.objects.all().values()), safe=False)


def change_password(request):
    return JsonResponse(list(User.objects.all().values()), safe=False)


def restore_password(request):
    return None


def create_new_password(request):
    return None


def login(request):
    return None


def logout(request):
    return None


def update_profile(request):
    return None


def change_email(request):
    return None


def donate_history(request):
    return None


def current_donations(request):
    return None


def get_project(request):
    return None


def donate_organization(request):
    return None


def donate_project(request):
    return None


def delete_donate(request):
    return None


def get_countries(request):
    return None
