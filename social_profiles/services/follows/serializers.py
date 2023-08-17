from rest_framework import serializers
from social_profiles.models import SocialProfile

class EachSocialProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialProfile
        fields = ('id','username')
        read_only_fields = ('id','username')

class FollowerSerializer(serializers.ModelSerializer):
    followers = EachSocialProfileSerializer(many=True, read_only= True)
    following = EachSocialProfileSerializer(many=True,read_only=True)
    
    class Meta:
        model = SocialProfile
        fields = ('followers','following')
        read_only_fields = ('followers','following')

class BlockPendingSerializer(serializers.ModelSerializer):
    pending_request = EachSocialProfileSerializer(many=True, read_only= True)
    blocked_user = EachSocialProfileSerializer(many=True,read_only=True)

    class Meta:
        model = SocialProfile
        fields = ('pending_request','blocked_user')
        read_only_fields = ('pending_request','blocked_user')