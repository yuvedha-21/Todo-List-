from django.urls import URLPattern, path
from . import views
urlpatterns=[
    path('',views.alltodos,name='alltodos'),
    path('delete-item/<int:pk>',views.deleteitem,name='deleteitem'),
    path('update-item/<int:pk>',views.updateitem,name='updateitem')

]