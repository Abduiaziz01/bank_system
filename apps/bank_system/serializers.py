from rest_framework import serializers
from .models import User, HistoryTransfer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'age', 'wallet_address']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, write_only=True
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'age', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError ({'password2': 'Пароли отличаются'})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({'phone_number':'Введённый номер не соответсвует стандартам КР (+996)'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            age=validated_data['age'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number',
                  'created_at', 'age')


class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ['id', 'from_user', 'to_user', 'is_completed', 'created_at', 'amount']
