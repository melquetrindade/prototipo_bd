# Generated by Django 5.0.3 on 2024-03-16 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_api_app', '0003_alter_pagamento_ownercaixa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa_diacaixa',
            name='ownerDiaCaixa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bd_api_app.diacaixa'),
        ),
    ]