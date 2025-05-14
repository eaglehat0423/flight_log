from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={"class": css_class})
    return field  # フィールドでない場合はそのまま返す


@register.filter(name='extract_iata')
def extract_iata(value):
    if value:
        parts = value.split('/')
        if parts:
            return parts[0]
    return value  # 返す値がない場合、そのまま返す
