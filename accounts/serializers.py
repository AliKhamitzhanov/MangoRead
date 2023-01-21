from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    """Serializer for creating a new User."""
    username = serializers.CharField(max_length=95)
    nickname = serializers.CharField(max_length=95)
    photo = serializers.ImageField(default='media/default/default.png')
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = 'username nickname photo password'.split()

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise ValidationError("This username is already in use!!!")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        users = super().create(validated_data)
        users.set_password(password)

        users.save()

        Token.objects.create(users=users)

        return users


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(
        write_only=True, style={"input_type": "password"},
        validators=[validate_password], required=True
    )

    class Meta:
        model = User
        fields = "id username nickname password".split()
        read_only_fields = "id nickname".split()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username nickname photo".split()

    def validate(self, attrs):
        queryset = User.objects.exclude(id=self.context["request"].user.id)
        if queryset.filter(username=attrs["username"]).exists():
            raise ValidationError({"message": "Username already in use!"})
        return attrs


class UpdatePasswordSerializer(LoginSerializer):
    old_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = "old_password password password2".split()
