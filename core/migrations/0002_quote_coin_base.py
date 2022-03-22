# Generated by Django 3.2 on 2022-03-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='coin_base',
            field=models.CharField(choices=[('usd', 'USD'), ('brl', 'BRL')], default='usd', max_length=3, verbose_name='Valor Base'),
        ),
    ]