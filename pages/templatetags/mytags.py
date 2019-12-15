from django import template

register = template.Library()

@register.filter
def gettext(data):
    print(data)
    return data.split('-')[0]
@register.filter
def getheader(data):
    print(data)
    return data.split('-')[1]