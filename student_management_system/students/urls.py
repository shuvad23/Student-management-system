from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import homepage,student_registration,student_detail,edit_information,delete_information

urlpatterns = [
    path('',homepage,name='homepage'),
    path('register/',student_registration,name='student_registration'),
    path('student/<int:pk>/',student_detail,name='student_detail'),
    path('edit/student/<int:student_id>',edit_information,name='edit_information'),
    path('delete/student/<int:student_id>',delete_information,name='delete_information')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)