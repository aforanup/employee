from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('employee/', views.EmployeeView.as_view(), name='employee')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
