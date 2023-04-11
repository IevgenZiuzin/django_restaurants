import json

from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse, HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy

from .models import Restaurant
from .forms import RestaurantAddForm


def index(request):
    return redirect('restaurants_list')


class RestaurantListView(ListView):
    model = Restaurant
    paginate_by = 6
    ordering = ['id']


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    form_class = RestaurantAddForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('restaurant_detail', kwargs={'slug': self.object.slug})


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantAddForm
    login_url = reverse_lazy('login')


class RestaurantDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurants_list')
    login_url = reverse_lazy('login')


class RestaurantDetailView(DetailView):
    model = Restaurant
    fields = '__all__'


class CuisineView(ListView):
    model = Restaurant
    template_name = 'restaurant_list'

    def get_queryset(self):
        return Restaurant.objects.filter(cuisine__slug=self.kwargs['slug'])


def search(request):
        try:
            search_data = json.load(request)
            results = Restaurant.objects.filter(Q(title__icontains=search_data['value']) |
                                                Q(cuisine__title__icontains=search_data['value']))
            html = render(request, 'snippets/search_results.html', {'results': results})
            return HttpResponse(html)
        except Exception:
            return HttpResponse(status=500)


def page_not_found_error(request, exception):
    return render(request, '404.html', status=404)


def internal_server_error(request, *args, **argv):
    return render(request, '500.html', status=500)
