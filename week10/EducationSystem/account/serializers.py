from django.contrib.auth import authenticate
from rest_framework import serializers
from account.models import User
from rest_auth.registration.serializers import RegisterSerializer
from .utils import send_activation_code

#so that no one can see the passwords, we do not create the password fields in the model of the user
#instead we add it in the serializers

#todo: register serializer

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(min_length=6, write_only=True)
#     password_confirm = serializers.CharField(min_length=6, write_only=True)
#     is_student = serializers.BooleanField()
#
#     class Meta:
#         model = User
#         fields = ['email', 'is_student', 'password', 'password_confirm', ]
#
# # validate <=> clean
# # validated_data <=> cleaned_data
#     def validate(self, validated_data):
#         email = validated_data.get('email')
#         password = validated_data.get('password')
#         password_confirm = validated_data.get('password_confirm')
#         is_student = validated_data.get('is_student')
#         if password != password_confirm:
#             raise serializers.ValidationError('Passwords do not match')
#         return validated_data
#
#     def create(self, validated_data):
#         """called when the object is being saved"""
#         email = validated_data.get('email')
#         password = validated_data.get('password')
#         is_student = validated_data.get('is_student')
#         user = User.objects.create_user(email=email, password=password, is_student=is_student)
#         send_activation_code(email=user.email, activation_code=user.activation_code)
#         return user
#

class CustomRegisterSerializer(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_student': self.validated_data.get('is_student', ''),
            'is_teacher': self.validated_data.get('is_teacher', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_student = self.cleaned_data.get('is_student')
        user.is_teacher = self.cleaned_data.get('is_teacher')
        user.save()
        adapter.save_user(request, user, self)
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


