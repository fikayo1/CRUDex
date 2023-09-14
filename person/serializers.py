from rest_framework import serializers

class Personserializer(serializers.Serializer):
    name = serializers.CharField()