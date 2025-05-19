from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def nav_active(context, url_name):
    try:
        if context['request'].resolver_match.url_name == url_name:
            return 'text-purple-500 dark:text-purple-400 font-semibold'
    except:
        return ''
    return ''
