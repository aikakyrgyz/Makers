from rest_framework import serializers

from .models import Subject, Course, Module


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title', ]


class CourseSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'owner', 'subject', 'title', 'overview', 'created',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = instance.owner.email
        representation['subject'] = SubjectSerializer(instance.subject).data
        serializer = ModuleSerializer(instance.modules.all(), many=True, context=self.context)
        representation['modules'] = serializer.data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['teacher_id'] = user_id
        course = Course.objects.create(**validated_data)
        return course


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


