from django.shortcuts import render
from django.db.models import Count
from agents.models import Agent
from properties.models import Property, Governorate
from about.models import Blogs, AboutUs
from django.db.models import Q
from django.core.paginator import Paginator


def home_view(request):
    agents_list = Agent.objects.all()[:4]
    properties_list = Property.objects.all()[:6]
    Governorates_list = Governorate.objects.annotate(
                    property_count=Count('property')).values('governorate_name' , 'property_count' , 'image')

    if request.method == "GET":
        query = request.GET.get('q')
        if query:
            properties = Property.objects.filter(
              Q(name__icontains= query)|
              Q(governorate__governorate_name__icontains=query)|
              Q(city__icontains=query))

            paginator = Paginator(properties, 12)
            page = request.GET.get('page')
            properties_query = paginator.get_page(page)

            context = {"properties_query":properties_query,
                        "q":query}

            return render(request, 'searches/property_result.html',context )

    try:
        blog = Blogs.objects.get(sub_title="Why Choose Us")
    except :
        blog = Blogs.objects.first()

    context ={
    "agents_list":agents_list,
    "properties_list":properties_list,
    "Governorates_list":Governorates_list,
    'blog':blog
    }

    template_name = 'searches/home.html'

    return render(request, template_name, context)
