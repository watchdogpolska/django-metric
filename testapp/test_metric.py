from metric.utils import filter_today
from django.utils.translation import ugettext_lazy as _
from testapp.models import News


def news_count():
    return News.objects.count()


news_count.name = _("News count")
news_count.description = _("Total count of news")


def news_daily():
    return filter_today(News.objects, 'created_at').count()


news_count.name = _("News daily")
news_count.description = _("Count of news today")