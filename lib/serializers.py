from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from lib.models import Autor, Book, Reader


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class BookValidator:

    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError('не может быть отрицательным')


class BookSerializer(serializers.ModelSerializer):
    number_of_page = serializers.IntegerField(validators=[BookValidator()])
    autor = serializers.SlugRelatedField(queryset=Autor.objects.all(), slug_field='last_name')

    # name = serializers.CharField(allow_blank=True)

    class Meta:
        model = Book
        fields = '__all__'


class PhoneValidator:

    def __call__(self, value):
        if len(str(value)) != 11:
            raise serializers.ValidationError('В номере должно быть 11 цифр')
        if str(value)[0] != '7':
            raise serializers.ValidationError('Номер должен начинаться с 7')


class ReaderSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(validators=[PhoneValidator()])
    active_book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='name', many=True)

    # def validate_books(self, active_book):
    #     if len(active_book) > 3:
    #         raise serializers.ValidationError("Читатель не может иметь более 3 книг")
    #     return active_book
    #
    # def validate(self, data):
    #     books = data.get('quantity')
    #     for book in books:
    #         if book.quantity == 0:
    #             raise serializers.ValidationError(f"Книга '{book.name}' недоступна для добавления в библиотеку")
    #     return data

    def validate(self, attrs):
        if len(attrs['active_book']) > 3:
            raise serializers.ValidationError('Can\'t add more than 3 books')
        return attrs

    # def create(self, validated_data):
    #     reader = super().create(validated_data)
    #
    #     reader.set_password(reader.password)
    #     reader.save()
    #     return reader
    #
    def create(self, validated_data):
        active_book = validated_data['active_book']
        # reader = super().create(validated_data)
        for book in active_book:
            if book.quantity == 0:
                raise serializers.ValidationError(f'Невозможно добавить книгу "{book.name}", нет в наличии!')
            return super().create(validated_data)

        #     book.quantity -= 1
        #     book.save()
        #     reader.active_book.add(book)
        # reader.set_password(reader.password)
        # reader.save()
        # return reader



    def update(self, instance, validated_data):
        if validated_data['active_book']:
            # Уменьшаем количество экземпляров книги, если книга добавляется в актив читателя
            for active_book in validated_data['active_book']:
                if active_book not in instance.active_book.all():
                    if active_book.quantity > 0:
                        active_book.quantity -= 1
                        active_book.save()
                    else:
                        raise ValidationError(f'The book {active_book.name} is missing')
            # Увеличиваем количество экземпляров книги, если книга удаляется из актива читателя
            for active_book in instance.active_book.all():
                if active_book not in validated_data['active_book']:
                    active_book.quantity += 1
                    active_book.save()

        return super().update(instance, validated_data)
    class Meta:
        model = Reader
        fields = '__all__'