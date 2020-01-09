from django.shortcuts import render
from django.views.generic import DetailView
from .models import Agent
from about.models import Blogs
from django.core.paginator import Paginator


def agents_list_view(request):
    agents = Agent.objects.all()
    paginator = Paginator(agents, 8)
    page = request.GET.get('page')
    agent_list = paginator.get_page(page)
    try:
        blog = Blogs.objects.get(sub_title="Why Choose Us")
    except:
        blog = Blogs.objects.first()
    context = {
        'agent_list':agent_list,
        'blog':blog,
    }
    template_name = 'agents/agents_list.html'
    return render(request, template_name, context)


class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agents/agent_detail.html'
