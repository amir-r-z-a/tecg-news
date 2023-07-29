from rest_framework import serializers
from .models import News, Tag


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'text']


#
# class TagsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =