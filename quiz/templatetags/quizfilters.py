from django import template

register = template.Library()

@register.filter
def get_item(list_obj, index):
    return list_obj[index]