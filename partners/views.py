from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Partner
from .data import cities, districts


def search(request):
    partners_list = Partner.objects.order_by('id')

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            partners_list = partners_list.filter(name__icontains=name)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            partners_list = partners_list.filter(city__iexact=city)
    
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            partners_list = partners_list.filter(district__iexact=district)
            
    paginator = Paginator(partners_list, 20)
    page = request.GET.get('page')
    partners = paginator.get_page(page)

    context = {
        'partners': partners,
        'cities': cities,
        'districts': districts,
        'values': request.GET
    }
    return render(request, 'partners/search.html', context)


def partner(request, partner_id):
    partner = Partner.objects.filter(id=partner_id).first()
    context = {
        'partner': partner
    }
    return render(request, 'partners/partner.html', context)
