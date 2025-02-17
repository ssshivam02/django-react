from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from apps.ratings.serializers import RatingSerializer
from apps.profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    email = serializers.CharField(source="user.email")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    full_name = serializers.SerializerMethodField(read_only= True)
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name', 'last_name',"full_name","id","phone_number", "profile_photo","about_me","license", "country", "reviews","num_reviews","is_buyer","is_seller","is_agent","ratings","city","gender"]
        
    def get_full_name(self, obj):
        first_name =  obj.user.first_name
        last_name = obj.user.last_name
        return f"{first_name} {last_name}"
    
    def get_reviews(self, obj):
        # agent_review is related name in ratings model
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation['top_agent'] = True
        return representation
    
class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    class Meta:
        model = Profile
        fields = ["phone_number", "profile_photo","about_me","license", "country","is_buyer","is_seller","is_buyer","is_agent","city","gender"]
        
        