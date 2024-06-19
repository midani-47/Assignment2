# blog/templatetags/blog_extras.py

from django import template

register = template.Library()

@register.filter
def has_liked(post, user):
    return post.likes.filter(id=user.id).exists()
