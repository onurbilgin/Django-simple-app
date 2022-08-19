from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Giris.models import Kisi
from .models import Gezi
from .forms import BilgiFormu
from .forms import GeziFormu
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def ilksayfa(request):
    return render(request, 'giris/ilksayfa.html')
def ikincisayfa(request):
    return  render(request, 'giris/ikincisayfa.html')
#def ucuncusayfa(request):
    #return render(request, 'giris/ucuncusayfa.html')


def bilgi(request):
    submitted = False
    if request.method == 'POST':
        form = BilgiFormu(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('menu3?submitted=True')
    else:
        form = BilgiFormu()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'Giris/bilgi.html', {'form': form, 'submitted': submitted})

@login_required(login_url=reverse_lazy('login'))
def gezi_se(request):
    submitted = False
    if request.method == 'POST':
        form = GeziFormu(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = GeziFormu()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'giris/gezi.html', {'form': form, 'submitted': submitted})


class GeziList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Gezi
    context_object_name = 'geziler'

    def get_context_data(self, **kwargs):
        context = super(GeziList, self).get_context_data(**kwargs)
        return context

class GeziView(DetailView):
    model = Gezi
    context_object_name = 'gezi'
    def get_context_data(self, **kwargs):
        context = super(GeziView, self).get_context_data(**kwargs)
        return context

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('registers-success')
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)