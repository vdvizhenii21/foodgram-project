from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import User, Follow
from rest_framework.validators import UniqueTogetherValidator



class CustomUserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)
    def get_is_subscribed(self, user_object): 
        return Follow.objects.filter(
            user=self.context['request'].user, follower=user_object.id).exists()
    class Meta:
        model = User
        fields = ['email', 'id', 'username', 'first_name', 'last_name', ]
        

class RegistrationSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)
    def get_is_subscribed(self, user_object): 
        return Follow.objects.filter(
            user=self.context['request'].user, follower=user_object.id).exists()
    class Meta:
        model = User
        fields = ['email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed']


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    follower = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'follower']
            )
        ]