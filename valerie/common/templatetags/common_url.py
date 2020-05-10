from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def youtube_embedded(text):
    sp = text.split("youtube.com/watch?v=")
    if len(sp) < 2:
        return text

    return '<iframe style="margin-top: 20px;"' \
           'width="450" ' \
           'height="254" ' \
           'src="https://www.youtube.com/embed/'+sp[1]+'" '\
           'frameborder = "0" ' \
           'allow = "autoplay; encrypted-media" ' \
           'allowfullscreen></iframe>'


@register.filter()
@stringfilter
def url_attachment(url):
    return '<a href="'+url+'"><i class="glyphicon glyphicon-globe"></i> '+url+'</a>'


@register.filter()
@stringfilter
def file_attachment(url, title):
    return '<a href="/'+url+'"><i class="glyphicon glyphicon-file"></i> '+title+'</a>'

