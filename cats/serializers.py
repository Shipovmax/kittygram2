import datetime as dt
from typing import Any

from rest_framework import serializers

from .models import CHOICES, Achievement, AchievementCat, Cat, User


class UserSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'cats')
        ref_name = 'ReadOnlyUsers'


class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = Achievement
        fields = ('id', 'achievement_name')


class CatSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, required=False)
    color = serializers.ChoiceField(choices=CHOICES)
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'achievements', 'owner',
                  'age')

    def get_age(self, obj: Cat) -> int:
        return dt.date.today().year - obj.birth_year

    def validate_birth_year(self, value: int) -> int:
        current_year = dt.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f'birth_year cannot be in the future (got {value}, '
                f'current year is {current_year})'
            )
        return value

    def create(self, validated_data: dict[str, Any]) -> Cat:
        if 'achievements' not in self.initial_data:
            cat = Cat.objects.create(**validated_data)
            return cat
        else:
            achievements = validated_data.pop('achievements')
            cat = Cat.objects.create(**validated_data)
            for achievement in achievements:
                current_achievement, _ = Achievement.objects.get_or_create(
                    **achievement)
                AchievementCat.objects.create(
                    achievement=current_achievement, cat=cat)
            return cat
