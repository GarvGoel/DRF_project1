from rest_framework import serializers
from .models import EmployeeData
from django.utils.text import slugify


class EmployeeDataSerializer(serializers.ModelSerializer):

    # SerialzerMethodField are used to return something that is not available in models, something that has to be computed dynamically
    makeSentence = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeData
        fields = '__all__'

    # get_ is attached to the name to get the value
    def get_makeSentence(self, obj):
        name = obj.name
        age = obj.age
        return f'{name} is {age} years old'

    def validate(self, validated_data):

        if validated_data.get('age'):
            age = validated_data.get('age')
            if age < 18:
                raise serializers.ValidationError("Age should be >=18")
        return super().validated_data
