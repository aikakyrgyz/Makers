from django.contrib.auth import authenticate
from rest_framework import serializers
from account.models import MyUser
from .utils import send_activation_code

#so that no one can see the passwords, we do not create the password fields in the model of the user
#instead we add it in the serializers

#todo: register serializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'password', 'password_confirm']

# validate <=> clean
# validated_data <=> cleaned_data
    def validate(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match')
        return validated_data

    def create(self, validated_data):
        """called when the object is being saved"""
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        print(user.activation_code)
        send_activation_code(email=user.email, activation_code=user.activation_code)
        return user


#todo: login serializer

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(label='Password', style={'input_type':'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request = self.context.get('request'), email = email, password = password)
            if not user:
                message = 'Unable to log in with provided credentials'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Must include [email] and [password]'
            raise serializers.ValidationError(message, code='authorization')
        attrs['user'] = user
        return attrs






# https://github.com/konradgalczynski07/instagram-api-clone
# https://github.com/justdjango/teach-me-django/blob/master/users/models.py
# https://github.com/kani0798/blog-api