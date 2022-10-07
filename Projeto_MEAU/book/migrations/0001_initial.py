# Generated by Django 4.1.1 on 2022-10-07 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id_historico', models.IntegerField(primary_key=True, serialize=False)),
                ('historicoPartidaReal', models.DateTimeField()),
                ('horarioChegadaReal', models.DateTimeField()),
                ('data', models.DateTimeField()),
                ('estado', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'historico',
            },
        ),
        migrations.CreateModel(
            name='Voo',
            fields=[
                ('id_voo', models.IntegerField(primary_key=True, serialize=False)),
                ('codigoVoo', models.CharField(max_length=12)),
                ('aeroportoOrigem', models.CharField(max_length=200)),
                ('aeroportoDestino', models.CharField(max_length=200)),
                ('horarioPartidaProgramado', models.DateTimeField()),
                ('horarioChegadaProgramado', models.DateTimeField()),
                ('rota', models.CharField(max_length=10)),
                ('companhia', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'voo',
            },
        ),
        migrations.CreateModel(
            name='relacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_historico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.historico')),
                ('id_voo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.voo')),
            ],
        ),
    ]
