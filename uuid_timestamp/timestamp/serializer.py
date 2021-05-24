from rest_framework import serializers

from timestamp.models import UniqueIdentifierTimestamp


class ListUuidTimestampSerializer(serializers.ModelSerializer):
    unique_identifier = serializers.UUIDField()
    timestamp = serializers.DateTimeField()

    class Meta:
        model = UniqueIdentifierTimestamp
        fields = ('unique_identifier', 'timestamp')

    def to_representation(self, data):
        res = super(ListUuidTimestampSerializer, self).to_representation(data)
        return {res.get('timestamp'): res.get('unique_identifier', None)}
