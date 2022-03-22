from django.db import models


class Base(models.Model):
    date_created = models.DateTimeField('Data de criação', auto_now_add=True)
    date_update = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        abstract = True


class Coin(Base):
    name = models.CharField("Nome da moeda", max_length=64, null=False)
    sigla = models.CharField("Sigla da moeda", max_length=16, null=False)

    def __str__(self):
        return self.sigla


class Rates(Base):

    class CHOICES_COIN_BASE(models.Choices):
        usd = "USD"
        brl = "BRL"

    rate_base = models.CharField(
        "Valor Base",
        max_length=3,
        choices=CHOICES_COIN_BASE.choices,
        default=CHOICES_COIN_BASE.usd
    )
    coin = models.ForeignKey("Coin", on_delete=models.PROTECT)
    date_rate = models.DateField("Data da quotação", null=False)
    value = models.DecimalField(max_digits=10, decimal_places=7, null=False)

    def __str__(self):
        return f"Quotação {self.coin}"

    def save(self, *args, **kwargs):
        rate = Rates.objects.filter(coin=self.coin, date_rate=self.date_rate).all()
        if self._state.adding and not rate:
            super().save(*args, **kwargs)
