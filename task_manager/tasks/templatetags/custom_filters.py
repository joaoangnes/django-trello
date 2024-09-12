from django import template

register = template.Library()

@register.filter
def getattr_custom(obj, attr):
    return getattr(obj, attr, None)
  
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)