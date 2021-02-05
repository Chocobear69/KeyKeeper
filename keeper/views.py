from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from keeper.forms import EditDataForm
from keeper.models import UsersData, User


class SecretListView(View):

    def get(self, request):
        secrets = UsersData.objects.all()
        return render(request, "keeper/list.html", context={"secrets": secrets})


class SecretEditView(View):

    def get(self, request):
        secret = get_object_or_404(UsersData, pk=request.GET.get("pk"))
        form = EditDataForm()
        return render(request, "keeper/edit_form.html", context={"secret": secret, "form": form})

    def post(self, request):
        form = EditDataForm(request.POST)
        if form.is_valid():
            return HttpResponse(status=200)
        return HttpResponse(status=500)
