from social_profiles.models import SocialProfile
from rest_framework import serializers
from social_profiles.services.follows.serializers import EachSocialProfileSerializer
class SocialProfileSerializer(serializers.ModelSerializer):
    followers = EachSocialProfileSerializer(many=True, read_only= True)
    following = EachSocialProfileSerializer(many=True,read_only=True)
    
    class Meta:
        model = SocialProfile
        fields = ['id', 'account', 'username', 'display_name', 'verified_profile', 'profile_picture', 'biography_text', 'created_date', 'profile_type', 'private_profile', "followers", "following"]
        depth = 0