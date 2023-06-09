from django.shortcuts import render
from .models import PortfolioWorks
# Create your views here.


def works(request):
    my_works = PortfolioWorks.objects.all()
    return render(request, 'my_works/my_works.html', {'my_works': my_works})
