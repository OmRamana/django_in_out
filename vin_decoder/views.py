from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_vin_details



class GetDroplets(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            "year": get_vin_details()[0],
            "type": get_vin_details()[1],
            "make":get_vin_details()[2],
            "model":get_vin_details()[3],
            "series":get_vin_details()[4],
            "trim":get_vin_details()[5],
            "fuel":get_vin_details()[6],
            "transmission":get_vin_details()[7],
            "drive":get_vin_details()[8]
        }
        return context

class OriginalDroplets(TemplateView):
      template_name = 'droplets.html'
    
     
class VinFormView(TemplateView):
    template_name = 'index.html'
    
    


