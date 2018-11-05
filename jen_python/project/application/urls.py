from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='User API')
from . import views


urlpatterns = [
        path('test1/', views.foo),
        path('foo1/', views.foo1),
        path('customer/', views.Index.as_view()),
        path('docs/', include_docs_urls(title='My API title')),
        path('schema/', schema_view),
]

