# Generated by Django 4.2.7 on 2024-09-24 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_produtos', '0002_compra_compraproduto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='preco_total',
        ),
    ]
