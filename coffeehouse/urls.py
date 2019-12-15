
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
#from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('about/', include('about.urls')),
    #path('newblog/', include('newblog.urls')),
    path('blog/', include('blog.urls')),
    path('', include('blog.urls')),
]
if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
