from rest_framework import serializers

from lib.models import Book


class BookValidator:

    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError('не может быть отрицательным')


class BookSerializer(serializers.ModelSerializer):
    number_of_page = serializers.IntegerField(validators=[BookValidator()])

    # name = serializers.CharField(allow_blank=True)

    class Meta:
        model = Book
        fields = '__all__'
