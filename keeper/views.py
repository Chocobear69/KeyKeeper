from django.views.generic import View
from django.shortcuts import render

from keeper.models import UsersData, User


class SecretListView(View):

    def get(self, request):
        secrets = UsersData.objects.all()
        return render(request, "keeper/index.html", context={"secrets": secrets})

