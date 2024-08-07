from rest_framework import serializers
from main.models import Contact, Banner, Service, Info

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'