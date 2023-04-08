from django import template
from _restaurants.models import Cuisine

register = template.Library()


@register.inclusion_tag('snippets/cuisines.html')
def get_cuisines():
    cuisines = Cuisine.objects.all()
    return {'cuisines': cuisines}
