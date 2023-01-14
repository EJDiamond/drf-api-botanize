from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """
    Answer serializer adding is_owner, profile_id and
    profile_image to the answer list
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Answer
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]


class AnswerDetailSerializer(AnswerSerializer):
    """
    References the post id which the answer is linked to
    """
    post = serializers.ReadOnlyField(source='post.id')
