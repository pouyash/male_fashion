from django import template

register = template.Library()


@register.filter(name='three_digits')
def three_digits(val):
    return '{:,}'.format(val)
