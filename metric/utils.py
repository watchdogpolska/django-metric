from datetime import datetime

def filter_today(qs, field):
    today = datetime.today()
    return qs.filter(**{'{}__date__gte'.format(field): today})


def filter_month(qs, field):
    start = datetime.today().replace(day=1)
    return qs.filter(**{'{}__date__gte'.format(field): start})
