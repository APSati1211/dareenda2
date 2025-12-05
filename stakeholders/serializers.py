from rest_framework import serializers
from .models import Stakeholder, SolutionsPage

class StakeholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stakeholder
        fields = '__all__'

class SolutionsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionsPage
        fields = '__all__'