
from django.forms import IntegerField
from rest_framework import serializers
from .models import Blog, Comment, Event, GameRecord
# basic serializer

class CommentSerializer(serializers.Serializer):
    email=serializers.EmailField()
    content=serializers.CharField(max_length=50)
    created=serializers.DateTimeField()


# serializerserializer
class Mserializer(serializers.Serializer):
    class Meta:
        model=Comment
        fields= '__all__'

class BlogSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=60)
    content=serializers.CharField(max_length=60)

    # field level vallidation
    def validate_title(self,value):
        """
        Check that the blog post is about Django
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.content=validated_data.get('content', instance.content)
        instance.save()
        return instance()
        
        # object level validation
    

class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=50)
    start=serializers.DateTimeField()
    finish= serializers.DateTimeField()

    def validate(self,data):
        """
        Check that start is before finish
        """
        if data['start']>data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data 


    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description=validated_data.get('description', instance.description)
        instance.start = validated_data.get('start',instance.start)
        instance.finish = validated_data.get('finish', instance.finish)
        instance.save()
        return instance()

def multiple_of_ten(value):
    if value%10!=0:
        raise serializers.ValidationError('Not a multiple of ten')

class GameRecordSerializer(serializers.Serializer):
   
    score=serializers.IntegerField(validators=[multiple_of_ten])

    def create(self, validated_data):

        return GameRecord.objects.create(**validated_data)

        

