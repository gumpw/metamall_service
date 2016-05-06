from rest_framework import serializers

from api.models import Config, SmsTemplate, Province, City, Area


class ConfigSerializer(serializers.Serializer):
    configName = serializers.CharField(max_length=32)
    configContent = serializers.CharField(max_length=256)
    gmtCreate = serializers.DateTimeField()
    gmtModified = serializers.DateTimeField()

    def create(self, validate_data):
        return Config.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.configName = validate_data.get('configName', instance.configName)
        instance.configContent = validate_data.get('configContent', instance.configContent)
        instance.gmtCreate = validate_data.get('gmtCreate', instance.gmtCreate)
        instance.gmtModified = validate_data.get('gmtModified', instance.gmtModified)
        instance.save()
        return instance

class ProvinceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)
    alias = serializers.CharField(max_length=32)

    def create(self, validate_data):
        return Province.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.id = validate_data.get('id', instance.id)
        instance.name = validate_data.get('name', instance.name)
        instance.alias = validate_data.get('alias', instance.alias)
        instance.save()
        return instance


class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    provinceId = serializers.IntegerField()
    name = serializers.CharField(max_length=32,allow_null=True)
    alias = serializers.CharField(max_length=32, allow_null=True)

    def create(self, validate_data):
        return City.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.id = validate_data.get('id', instance.id)
        instance.provinceId = validate_data.get('provinceId', instance.provinceId)
        instance.name = validate_data.get('name', instance.name)
        instance.alias = validate_data.get('alias', instance.alias)
        instance.save()
        return instance


class QuerySerializer(serializers.Serializer):
    q_id = serializers.IntegerField()

    def create(self, validated_data):
        return City.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.q_id = validated_data.get('q_id', instance.q_id)
        instance.save()
        return instance





class AreaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cityId = serializers.IntegerField()
    provinceId = serializers.IntegerField()
    name = serializers.CharField(max_length=32)
    alias = serializers.CharField(max_length=32)

    def create(self, validate_data):
        return Area.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.id = validate_data.get('id', instance.id)
        instance.cityId = validate_data.get('cityId', instance.cityId)
        instance.provinceId = validate_data.get('provinceId', instance.provinceId)
        instance.name = validate_data.get('name', instance.name)
        instance.alias = validate_data.get('alias', instance.alias)
        instance.save()
        return instance

class SmsRequestSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    phoneNo = serializers.CharField()
    type = serializers.ChoiceField(choices=(("register", "注册"), ("login", "登陆"),
                                            ("withdraw", "提现"), ("recover", "找回密码")))


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('provinceId')

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Area
        fields = ('cityId')


class SmsResponseSerializer(serializers.Serializer):
    code = serializers.CharField()
    msg = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class SmsTemplateSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=12)
    templateContent = serializers.CharField(max_length=256)  # Field name made lowercase.
    gmtModified = serializers.DateTimeField()

    def create(self, validate_data):
        return SmsTemplate.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.type = validate_data.get('type', instance.type)
        instance.templateContent = validate_data.get('templateContent', instance.templateContent)
        instance.gmtModified = validate_data.get('gmtModified', instance.gmtModified)
        instance.save()
        return instance
