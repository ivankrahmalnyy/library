from rest_framework import serializers

from lib.models import Reader


class PhoneValidator:

    def __call__(self, value):
        if len(str(value)) != 11:
            raise serializers.ValidationError('В номере должно быть 11 цифр')
        if str(value)[0] != '7':
            raise serializers.ValidationError('Номер должен начинаться с 7')


class ReaderSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(validators=[PhoneValidator()])

    class Meta:
        model = Reader
        fields = '__all__'
