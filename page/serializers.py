from rest_framework import serializers

from page.models import Car


class CarListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()


class CarCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

    def create(self, validated_data):
        title =self.validated_data.get('title').upper()
        price = self.validated_data.get('price')
        return Car.objects.create(
            title=title,
            price=price
        )

    def update(self, instance, validated_data):
        instance.title = self.validated_data.get('title', instance.title)
        instance.price = self.validated_data.get('price', instance.price)
        instance.save()
        return instance


class CarDestroySerializer(serializers.Serializer):
    id = serializers.IntegerField()


