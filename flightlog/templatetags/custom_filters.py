from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a class to a form field
    Usage: {{ form.field|add_class:"css_class" }}
    """
    return value.as_widget(attrs={'class': arg})
