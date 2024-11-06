# recommendations/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def round_value(value, arg=0):
    try:
        return round(value, int(arg))
    except (ValueError, TypeError):
        return value
