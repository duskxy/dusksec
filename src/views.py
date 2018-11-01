from django.shortcuts import render
from pure_pagination import Paginator,PageNotAnInteger
from django.views.generic import View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Src,asset

# Create your views here.

class index(LoginRequiredMixin,ListView):
    template_name = 'src.html'
    model = Src
    context_object_name = 'src_list'
   # def get_queryset(self):
   #    self.ass = get_object_or_404(Src,id=self.args[0])
   #    return asser.objects.filter(url=self.ass)
    def get_context_data(self,**kwargs):
        try:
            page = self.request.GET.get('page',1)
        except PageNotAnInteger:
            page =1
        context = super(index,self).get_context_data(**kwargs)
        assquery = asset.objects.filter(url_id=self.kwargs['gs'])
        context["src_url"] = Src.objects.get(id=self.kwargs['gs'])
        p = Paginator(assquery,10,request=self.request)
        asset_list = p.page(page)
        context["asset_list"] = asset_list
        return context

