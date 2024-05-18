from tortoise import fields, models


class DadosPressao(models.Model):
    id = fields.IntField(pk=True)
    unidade_de_medida = fields.CharField(max_length=255, unique=True)
