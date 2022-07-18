from django import template
from movies.models import Category


register = template.Library()

@register.inclusion_tag('include/tags/categories_drop_down.html')
def get_category_drop_down():
    """Рендер всплывающего меню с категориями в меню"""
    categories = Category.objects.all()
    return {'categories': categories}