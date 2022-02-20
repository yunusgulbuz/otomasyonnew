from rest_framework import serializers

class DersSerializer(serializers.Serializer):
    ders_name = serializers.CharField(max_length=40)


