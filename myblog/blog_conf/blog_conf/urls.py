from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog_app.views import frontpage, post_detail, post_create, post_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name="frontpage"),
    path('post_create/', post_create, name="post_create"),
    path('post_test/', post_test, name="post_test"),
    path("<slug:slug>/", post_detail, name="post_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

