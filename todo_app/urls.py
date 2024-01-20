from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.home , name='home'),
    path('delete/<str:pk>/' , views.delete , name='delete'),
    path('update/<str:pk>/' ,views.update ,name='update'),
    path('homecview/' , views.TaskListView.as_view(), name='homecview'),
    path('detailedcview/<int:pk>/' ,views.DetailedView.as_view() , name='detailedcview'),
    path('updatedcview/<int:pk>/' ,views.UpdateDetailedView.as_view() , name='updatecview'),
    path('deletedcview/<int:pk>/' ,views.TaskDeleteView.as_view() , name='deletecview')
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)