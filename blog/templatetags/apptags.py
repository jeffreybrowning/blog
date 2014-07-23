from django import template

register = template.Library()

def fart_split(value, sep = "  "):
    parts = value.split(sep)
    return (parts)

register.filter('fartsplit', fart_split)