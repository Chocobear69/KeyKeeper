from django.views.generic import View
from django.http.response import HttpResponse
from django.shortcuts import render

from keeper.models import UsersData, User


class SecretListView(View):

    def get(self, request):
        """
                if user := User.object.get(id=request.user.id):
            user_data = UsersData.objects.filter(user=user)
                    return HttpResponse(status=403)
        :param request:
        :return:
        """
        return render(request, "keeper/index.html", context={"name": "Vlad"})

