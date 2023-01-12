from django.urls import include, path

urlpatterns = [
    path('api/', include('recipe_api.urls')),
]