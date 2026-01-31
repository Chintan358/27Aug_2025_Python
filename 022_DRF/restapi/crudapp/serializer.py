from rest_framework import serializers
from crudapp.models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields = '__all__'

    def to_representation(self, instance):
        resp =  super().to_representation(instance)
        resp['country'] = CountrySerializer(instance.country).data
        return resp
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = '__all__'

    def validate(self, attrs):
        
        if attrs['qty']<10:
            raise serializers.ValidationError("Qty must be above or equal 10")
        return attrs
        
    def to_representation(self, instance):
        resp =  super().to_representation(instance)
        resp['author'] = AuthorSerializer(instance.author).data
        return resp