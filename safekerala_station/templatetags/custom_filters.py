from django import template

register = template.Library()

@register.filter(name='dictlookup')
def dictlookup(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key, None)
    return None
