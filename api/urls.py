from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/', views.product_list),
    path('get_all/', views.get_all_data),
    path('edit/', views.edit_date),
    path('delete/', views.cancel),
   
]