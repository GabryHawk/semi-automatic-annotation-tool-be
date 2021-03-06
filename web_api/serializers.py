from web_api.models import Detector, Dataset, Annotation, PreprocessedDataset
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
class DetectorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Detector
        fields = ['id', 'name', 'command', 'class_list', 'is_both']

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Dataset
        fields = ['id', 'name', 'rgb_path', 'thermal_path']

class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    checker = UserSerializer(read_only=True)
    class Meta:
        model = Annotation
        fields = ['id', 'rgb_url', 'rgb_boxes', 'thermal_url', 'thermal_boxes', 'checker']

class PreprocessedDatasetSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    annotation_set = AnnotationSerializer(many=True, read_only=True)
    detector = DetectorSerializer(read_only=True)
    class Meta:
        model = PreprocessedDataset
        fields = ['id', 'name', 'time', 'status', 'annotation_set', 'detector']