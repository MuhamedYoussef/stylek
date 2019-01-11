from django.shortcuts import render
from partners.models import Partner


def index(request):
    context = {
        'partners': Partner.objects.order_by('id')[:3]
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
