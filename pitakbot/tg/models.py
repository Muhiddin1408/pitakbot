from django.db import models


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name="Telegram ID")
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    step = models.IntegerField(default=0)
    is_from = models.CharField(max_length=100, default="", verbose_name="Qayerda")
    is_to = models.CharField(max_length=100, default="", verbose_name="Qayerga")
    date = models.CharField(max_length=100, default="", verbose_name="Qachon")
    car = models.CharField(max_length=100, default="", verbose_name="Avtomobil")
    phone = models.CharField(max_length=100, default="", verbose_name="Telefon")
    comment = models.TextField(default="", verbose_name="Izoh")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"


class Order(models.Model):
    is_from = models.CharField(max_length=100, default="", verbose_name="Qayerda")
    is_to = models.CharField(max_length=100, default="", verbose_name="Qayerga")
    date = models.CharField(max_length=100, default="", verbose_name="Qachon")
    car = models.CharField(max_length=100, default="", verbose_name="Avtomobil")
    telegram_id = models.BigIntegerField(default=1, verbose_name="Telegram ID")
    username = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="", verbose_name="Telefon")
    comment = models.TextField(default="", verbose_name="Izoh")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


class Telegram_group(models.Model):
    telegram_id = models.BigIntegerField(default=1, verbose_name="Telegram ID")
    name = models.CharField(max_length=100, default="", verbose_name="Grux yoki Kanal nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Telegram group yoki kanal"
        verbose_name_plural = "Telegram group yoki kanallar"
