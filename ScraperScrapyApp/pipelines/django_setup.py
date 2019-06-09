from django.conf import settings
from django.apps import apps
from PortalDjangoApp.PortalDjangoApp.settings import DATABASES

settings.configure(
    INSTALLED_APPS=("PortalDjangoApp.Portal.apps.PortalConfig"), DATABASES=DATABASES
)
apps.ready = False
apps.populate(["PortalDjangoApp.Portal"])
