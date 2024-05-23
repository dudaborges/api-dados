from tortoise import fields, models


class PressureData(models.Model):
    id = fields.IntField(pk=True)
    pressure = fields.IntField(max_length=255, null=True)
    timestamp = fields.DatetimeField(auto_now=True)
