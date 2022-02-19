from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('employee/', include([
        path('', views.EmployeeView.as_view(), name='employee'),
        path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(),
             name='employee_delete'),
        path('<int:pk>/details/',
             views.EmployeeDetailView.as_view(), name='employee_detail'),
        path('<int:profile_pk>/update_skill/<int:pk>/',
             views.UpdateSkillView.as_view(), name='update_skillset')
    ]))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
