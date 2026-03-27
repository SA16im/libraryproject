from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.bookmodule.urls')), # أي رابط يبدأ بـ books سيذهب لتطبيقنا
]
