from rest_framework import serializers
from articals.models import Article


class ArticalSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')
