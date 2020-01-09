from django.shortcuts import render
from django.views.generic import DetailView
from .models import AboutUs, Blogs
from agents.models import Agent

def about_us_view(request):
    about = AboutUs.objects.last()
    blogs_list = Blogs.objects.all()
    agents = Agent.objects.all()[:4]
    context = {'about':about,
                'blogs_list':blogs_list,
                'agents':agents}
    tempalte_name = 'about/about.html'

    return render(request, tempalte_name, context)


class BolgDetailView(DetailView):
    model = Blogs
    template_name = 'about/blog_detail.html'
