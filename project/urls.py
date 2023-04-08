"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from project import settings
from django.urls import path
from _users import views as users_views
from _restaurants import views as restaurants_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', users_views.ModeratorLoginView.as_view(), name='login'),
    path('logout/', users_views.log_out, name='logout'),
    path('', restaurants_views.index, name='index'),
    path('restaurants/', restaurants_views.RestaurantListView.as_view(), name='restaurants_list'),
    path('restaurants/create/', restaurants_views.RestaurantCreateView.as_view(), name='restaurant_create'),
    path('restaurants/<slug:slug>/', restaurants_views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurants/<slug:slug>/update/', restaurants_views.RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('restaurants/<slug:slug>/delete/', restaurants_views.RestaurantDeleteView.as_view(), name='restaurant_delete'),
    path('cuisines/<slug:slug>', restaurants_views.CuisineView.as_view(), name='cuisine'),
    path('search/>', restaurants_views.search, name='search'),
]

handler404 = '_restaurants.views.page_not_found_error'
handler500 = '_restaurants.views.internal_server_error'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
