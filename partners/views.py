from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Partner
from .data import cities, districts


def search(request):
    partners_list = Partner.objects.order_by('id')

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            partners_list = partners_list.filter(name__icontains=name.strip())

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            partners_list = partners_list.filter(city__iexact=city)

    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            partners_list = partners_list.filter(district__iexact=district)

    if 'spa' in request.GET and request.GET['spa'] == 'on':
        partners_list = partners_list.filter(cats__icontains='spa')

    if 'beauty' in request.GET and request.GET['beauty'] == 'on':
        partners_list = partners_list.filter(cats__icontains='beauty')

    if 'wc' in request.GET and request.GET['wc'] == 'on':
        partners_list = partners_list.filter(cats__icontains='weight')

    if 'pg' in request.GET and request.GET['pg'] == 'on':
        partners_list = partners_list.filter(cats__icontains='photographers')

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
    partner = get_object_or_404(Partner, id=partner_id)
    context = {
        'partner': partner
    }
    return render(request, 'partners/partner.html', context)
