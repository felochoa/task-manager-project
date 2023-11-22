
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

    
#View: Describes which data is sent to the user but not its presentation

# Create your views here.
""" def homePageView(request):
    return HttpResponse("main page") """