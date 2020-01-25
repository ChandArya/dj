from django.conf.urls import url
from .views import ArticalViewSet
# from .views import (ArticleListView, 
# ArticleDetailsView, 
# ArticleCreateView, 
# ArticleUpdateView, 
# ArticleDeleteView)

# urlpatterns = [
    
#     url(r'^(?P<pk>\d+)/$', ArticleDetailsView.as_view()),
#     url(r'^create/', ArticleCreateView.as_view()),
#     url(r'^(?P<pk>\d+)/update/$', ArticleUpdateView.as_view()),
#     url(r'^(?P<pk>\d+)/delete/$', ArticleDeleteView.as_view()),
#     url(r'^$', ArticleListView.as_view())
   
   
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticalViewSet, basename='article')
urlpatterns = router.urls