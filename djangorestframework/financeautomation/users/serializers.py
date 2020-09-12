from rest_framework import serializers

from users.models import User

class RegisterationSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)

    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','age', 'password']
    
    def save(self):
        user = User.objects.create_user(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'], 
            age = self.validated_data['age'],
            password = self.validated_data['password'],
        )
        
        # user.set_password(password)
        # User.objects.save()

        return user