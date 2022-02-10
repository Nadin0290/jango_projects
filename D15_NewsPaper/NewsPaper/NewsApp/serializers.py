from .models import *
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['category_type', 'header','text', 'rating', 'author_id']


# class SClassSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = SClass
#        fields = ['id', 'grade', ]


# class StudentSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Student
#        fields = ['id', 'name', ]