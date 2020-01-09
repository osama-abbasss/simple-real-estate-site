from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .  import models
from django.core.paginator import Paginator
from django.db.models import Count
from .forms import ReserveFrom
from django.contrib import messages
from django.core.mail import send_mail

def properties_view(request):
    properties = models.Property.objects.all()
    paginator = Paginator(properties, 9)
    page = request.GET.get('page')
    properties_list = paginator.get_page(page)

    governorates = models.Governorate.objects.all()
    governorates_list = models.Governorate.objects.annotate(
                    property_count=Count('property')).values('governorate_name' , 'property_count' , 'image')

    template_name = 'properties/properties.html'
    context = {
        'properties_list':properties_list,
        "governorates":governorates_list

    }

    return render(request, template_name, context)


class PropertyDetailView(DetailView):
    model = models.Property
    template_name = 'properties/property_detail.html'


def reserve_property(request):
    template_name = 'properties/contact.html'
    form = ReserveFrom(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            reserve = models.ReserveProperty(
                    first_name= first_name,
                    last_name= last_name,
                    email= email,
                    message= message
            )
            reserve.save()
            send_mail('Hello', 'we are receved your message and we will contact yos as son as posipole', email, ['eng.oabbass@gmail.com'])
            return redirect('/')
        else:
            messages.error(request, 'Message Error, Try again!')
            return redirect('properties:reserve')
    context ={}
    return render(request, template_name, context)
