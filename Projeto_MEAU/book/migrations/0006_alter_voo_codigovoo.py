# Generated by Django 4.1.2 on 2022-11-14 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_rename_horariochegadareal_historico_horarioreal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='codigoVoo',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]