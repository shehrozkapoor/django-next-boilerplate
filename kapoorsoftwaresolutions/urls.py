"""kapoorsoftwaresolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from allauth.account.models import EmailAddress
from rest_framework.authtoken.models import TokenProxy
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from django_celery_beat.models import ClockedSchedule, SolarSchedule, IntervalSchedule
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(EmailAddress)
admin.site.unregister(TokenProxy)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(SolarSchedule)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(Site)
admin.site.unregister(Group)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("kapoorsoftwaresolutions.api_router")),
]
admin.site.site_header = "Kapoor Software Solutions"
admin.site.site_title = "Kapoor Software Solutions Admin Portal"
admin.site.index_title = "Kapoor Software Solutions Admin"

# swagger
api_info = openapi.Info(
    title="Kapoor Software Solutions API",
    default_version="v1",
    description="API documentation for Kapoor Software Solutions App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]
