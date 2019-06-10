from django import template as template_engine


RELATIVE_PREFIX = "../"
RELATIVE_PREFIX_OFFSET = len(RELATIVE_PREFIX)

register = template_engine.Library()


@register.filter
def normalize_news_url(url):
    if url.startswith(RELATIVE_PREFIX):
        url = f'https://{url[RELATIVE_PREFIX_OFFSET:]}'

    return url
