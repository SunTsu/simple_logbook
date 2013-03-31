from django.conf import settings
def simple_logbook_settings(request):
    return dict(settings=settings)
