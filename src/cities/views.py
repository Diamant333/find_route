from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from cities.form import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home', 'CityDetailView'
)


def home(request, pk=None):
    if request.method == 'POST':
        form = form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    #if pk:
    #    city = get_object_or_404(City, id=pk)
    #    context = {'object': city}
    #    return render(request, 'cities/detail.html', context)
    form = CityForm()
    qs = City.objects.all()
    context = {'object_list': qs, 'form':form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')