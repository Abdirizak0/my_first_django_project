from django import template
from blog.models import UserActionLog

register = template.Library()

@register.inclusion_tag('blog/user_action_logs.html')
def show_user_action_logs(user, limit=5):
    logs = UserActionLog.objects.filter(user=user).order_by('-timestamp')[:limit]
    return {'logs': logs}