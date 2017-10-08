from rest_framework import serializers


def get_datetime(timestamp):
    from datetime import datetime
    import pytz
    tz = pytz.timezone('Asia/Kolkata')
    return datetime.fromtimestamp(timestamp / 1000.0, tz)


def get_timestamp(datetime):
    return int(datetime.timestamp() * 1000)


class TimestampField(serializers.Field):
    def to_internal_value(self, data):
        if type(data) is str:
            data = float(data)
        return get_datetime(data)

    def to_representation(self, value):
        return get_timestamp(value)