from rest_framework import serializers

from ads.models import Categories, User, Ads, City


class CategorySerializer(serializers.ModelSerializer):
    # class CategorySerializer(serializers.Serializer):
    #     name = serializers.CharField(max_length=150)

    class Meta:
        model = Categories
        fields = '__all__'


class AdsSerializer(serializers.ModelSerializer):
    # author_name = serializers.SlugRelatedField(required=False,
    #                                            many=False,
    #                                            # read_only=False,
    #                                            queryset=User.objects.all(),
    #                                            slug_field='username')

    class Meta:
        model = Ads
        fields = '__all__'
        # fields = ['id','name','author_name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False,
                                             many=True,
                                             # read_only=False,
                                             queryset=City.objects.all(),
                                             slug_field='name')

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'age', 'locations']


class CreateUserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False,
                                             many=True,
                                             # read_only=False,
                                             queryset=City.objects.all(),
                                             slug_field='name')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'age', 'locations']

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("locations")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        for city in self._locations:
            location_obj, _ = City.objects.get_or_create(name=city)
            user.locations.add(location_obj)
        user.save()
        return user
