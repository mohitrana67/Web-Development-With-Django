from accounts.models import Account

from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    """Serializer for the user objcts"""
    
    class Meta:
        model = Account
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        )
        # extra_kwargs = {
        #     'password': {'write_only': True, 'min_length': 5}
        # }

        def create(self, validated_data):
            """Create a new user with encrypted password and return it"""
            return Account().objects.create_user(**validated_data)