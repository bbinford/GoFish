from django.shortcuts import render
from .models import GuideBusiness

# Create your views here.


def guide(request):
    data = GuideBusiness.objects.get(pk=1)
    user = request.user.get_username()
    return render(request, 'base.html', {'data': data,
                                         'user': user})
