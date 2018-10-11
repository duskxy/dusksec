from django.shortcuts import render

from django.views.generic import View,ListView

from .models import Src,asset

# Create your views here.

class index(ListView):
    template_name = 'src.html'
    model = Src
    context_object_name = 'src_list'
   # def get_queryset(self):
   #    self.ass = get_object_or_404(Src,id=self.args[0])
   #    return asser.objects.filter(url=self.ass)
    def get_context_data(self,**kwargs):
        context = super(index,self).get_context_data(**kwargs)
        context["asset_list"] = asset.objects.filter(url_id=self.kwargs['gs'])
        context["src_url"] = Src.objects.get(id=self.kwargs['gs'])
        return context

