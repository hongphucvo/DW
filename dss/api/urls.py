
# from django.conf.urls import url
from django.urls import path, include
from .views import (
    CustomerListApiView,
)

urlpatterns = [
    path('api/', CustomerListApiView.as_view()),
]

# urlpatterns = [
# #     path("admin/", admin.site.urls),
#     path('api-auth/', include('rest_framework.urls')),
# #     path('api/',include(api_url))
# ]