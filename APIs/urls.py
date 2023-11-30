from django.urls import path
from .views import  *

urlpatterns = [
    path('bedaia',BedaiaListAPIView.as_view(),name='bedaias'),
    path('bedaia/<str:slug>',BedaiaDetailsAPIView.as_view(),name='bedaia'),
    path('nukhba',NukhbaListAPIView.as_view(),name='nukhbas'),
    path('nukhba/<str:slug>',NukhbaDetailsAPIView.as_view(),name='nukhba'),   
]