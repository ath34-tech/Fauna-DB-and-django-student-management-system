from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('add',views.AddStudent,name='add'),
    path('update/<str:id>',views.UpdateStudent,name='update'),
    path('delete/<str:id>',views.DeleteStudent,name='delete'),

]