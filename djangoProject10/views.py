from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

def test(request):
    permission_classes = (IsAuthenticated,)
    return HttpResponse("Hello world")
