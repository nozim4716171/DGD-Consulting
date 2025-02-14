from django import template

register = template.Library()

@register.filter
def slicewords(value, start_index):
    words = value.split()
    return " ".join(words[int(start_index):])