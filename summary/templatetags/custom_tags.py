from django import template
register = template.Library()


def zip_lists(a, b):
    return zip(a, b)


register.filter('zip_lists', zip_lists)
