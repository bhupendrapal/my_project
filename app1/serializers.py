from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length= 100)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    marks = serializers.IntegerField()
    is_active = serializers.BooleanField()
    
    
    # def create(self, validated_data):
    #     print("in create method", validated_data)
    #     return create(validated_data)