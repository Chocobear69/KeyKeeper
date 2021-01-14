from django.views.generic import View
from django.http.response import HttpResponse

from keeper.models import UserData


class SecretListView(View):
    def get(self, request):
        return HttpResponse(status=200)
