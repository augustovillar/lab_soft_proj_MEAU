# Generated by Django 4.1.2 on 2022-12-12 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_voo_codigovoo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='status',
            field=models.CharField(choices=[('PREVISTO', 'Previsto'), ('EMBARCANDO', 'Embarcando'), ('CANCELADO', 'Cancelado'), ('PROGRAMADO', 'Programado'), ('TAXIANDO', 'Taxiando'), ('PRONTO', 'Pronto'), ('AUTORIZADO', 'Autorizado'), ('EM_VOO', 'Em Voo'), ('ATERRISSADO', 'Aterrissado')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='voo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.voo'),
        ),
    ]
