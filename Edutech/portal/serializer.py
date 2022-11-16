from rest_framework import serializers
from .models import *


class User(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'