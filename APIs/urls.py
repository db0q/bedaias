from django.urls import path
from .views import  *

urlpatterns = [
    path('bedaia',BedaiaListAPIView.as_view(),name='bedaias'),
    path('bedaia/<str:slug>',BedaiaDetailsAPIView.as_view(),name='bedaia'),
     path('Nukhba',NukhbaListAPIView.as_view(),name='Nukhba'),
    path('Nukhba/<str:slug>',NukhbaDetailsAPIView.as_view(),name='Nukhba'),   
]