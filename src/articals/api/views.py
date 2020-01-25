from articals.models import Article
from .serializers import ArticalSeralizer
from rest_framework import viewsets
# from rest_framework.generics import (ListAPIView,
#  RetrieveAPIView , 
#  CreateAPIView ,
#  DestroyAPIView, 
#  UpdateAPIView) 

class ArticalViewSet(viewsets.ModelViewSet):
    serializer_class = ArticalSeralizer
    queryset = Article.objects.all()
# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticalSeralizer


# class ArticleDetailsView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticalSeralizer

# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticalSeralizer

# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticalSeralizer

# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticalSeralizer
