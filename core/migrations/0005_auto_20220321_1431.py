# Generated by Django 3.2 on 2022-03-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220316_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rates',
            old_name='date',
            new_name='date_rate',
        ),
        migrations.AlterField(
            model_name='rates',
            name='rate_base',
            field=models.CharField(choices=[('USD', 'Usd'), ('BRL', 'Brl')], default='USD', max_length=3, verbose_name='Valor Base'),
        ),
    ]
