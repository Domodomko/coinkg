from rest_framework import serializers

from .models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'publish', 'views')


class SuccessStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStory
        fields = ('title', 'content')


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('content',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'type', 'value')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone', 'content', 'publish')


class CreditSerializer(serializers.ModelSerializer):
    # user = ProfileSerializer(many=True)

    class Meta:
        model = Credit
        fields = ('id', 'product', 'sum', 'time', 'passport', 'publish', 'currency', 'other_credits', 'user')


class CreditsInfoSerializer (serializers.ModelSerializer):
    class Meta:
        model = CreditsInfo
        fields = ('id', 'title', 'content', 'image')
