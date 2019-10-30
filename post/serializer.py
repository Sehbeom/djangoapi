from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','body']
        #fields = '__all__'  # 7번줄을 이렇게 써도 됨
        #read_only_fields = ('title',)
