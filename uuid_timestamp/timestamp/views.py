from rest_framework import generics

from timestamp.models import UniqueIdentifierTimestamp
from timestamp.serializer import ListUuidTimestampSerializer


class ListUuidTimestampView(generics.ListAPIView):
    serializer_class = ListUuidTimestampSerializer
    queryset = UniqueIdentifierTimestamp.objects.all()
