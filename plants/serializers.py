from rest_framework import serializers
from plants.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    plant_type_display = serializers.ReadOnlyField(source='get_plant_type_display')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    class Meta:
        model = Plant
        fields = [
            'id', 'owner', 'created_at', 'is_owner', 'profile_id',
            'profile_image', 'updated_at', 'plant_name',
            'plant_type', 'image', 'age', 'about', 'plant_type_display',
        ]
