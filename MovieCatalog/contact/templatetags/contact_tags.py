from django import template
from contact.forms import ContactForm


register = template.Library()


@register.inclusion_tag('include/tags/contact_form.html')
def contact_form():
    return {'contact_form' : ContactForm()}