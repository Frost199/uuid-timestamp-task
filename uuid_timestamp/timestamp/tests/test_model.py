from unittest import TestCase

from timestamp.models import UniqueIdentifierTimestamp


class ModelTest(TestCase):
    """
    Model Test Class
    """

    def test_create_uuid_with_a_timestamp(self):
        uuid_timestamp = UniqueIdentifierTimestamp.objects.create()
        self.assertEqual(str(uuid_timestamp), str(uuid_timestamp.unique_identifier))
