
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Appsubhujo.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "Appsubhujo.views.page_not_found_view"
