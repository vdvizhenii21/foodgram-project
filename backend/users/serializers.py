from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import BooleanField
from .models import User, Follow
from rest_framework.validators import UniqueTogetherValidator

# User = get_user_model()

class UserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)
        def get_is_subscribed(self, current_user): 
            request_user = self.context['request'].user 
            return request_user.follower.filter(user=current_user).exists()
    class Meta:
        model = User
        fields = ['email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed']
        

class RegistrationSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField()
    def get_is_subscribed(self, current_user): 
            request_user = self.context['request'].user 
            return request_user.follower.filter(user=current_user).exists()
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