from rest_framework import serializers

from lib.models import Autor


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = '__all__'