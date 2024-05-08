from rest_framework import serializers

from .models import User, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    # Create user with hashed password
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "transaction_type",
            "value",
            "category",
            "user",
            "date",
            "payment_method",
        ]
        extra_kwargs = {"user": {"write_only": True}}
