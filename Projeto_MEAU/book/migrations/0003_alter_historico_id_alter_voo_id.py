# Generated by Django 4.1.2 on 2022-11-08 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_id_historico_historico_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]