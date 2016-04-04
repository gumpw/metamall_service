from rest_framework import serializers

from api.models import Config, SmsTemplate


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


class SmsRequestSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    phoneNo = serializers.CharField()
    type = serializers.ChoiceField(choices=(("register", "注册"), ("login", "登陆"),
                                            ("withdraw", "提现"), ("recover", "找回密码")))


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
