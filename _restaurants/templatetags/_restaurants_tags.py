from django import template
from _restaurants.models import Cuisine

register = template.Library()


@register.inclusion_tag('snippets/cuisines.html', takes_context=True)
def get_cuisines(context):
    cuisines = Cuisine.objects.all()
    return {'cuisines': cuisines, 'request_path': context.request.path}
