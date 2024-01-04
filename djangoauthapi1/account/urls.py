from django.urls import path, include ,admin

urlpatterns = [
    path('admin/' , admin.site.urls)
]