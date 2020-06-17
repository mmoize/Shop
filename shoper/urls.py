from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'shoper'

urlpatterns = [
    path('', views.product_list, name='product_list' ),
    path('<category_slug>[-\w+]', views.product_list, name='product_list_by_category'),
    path('<int:id>\d+/<slug:slug>[-\w]+)/', views.product_detail, name='product_detail'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


                         