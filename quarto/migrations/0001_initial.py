# Generated by Django 2.2.6 on 2019-10-04 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('andar', models.IntegerField()),
                ('banheiro', models.IntegerField()),
                ('cama', models.IntegerField()),
                ('diaria', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='ImagemQuarto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarto.Quarto')),
            ],
        ),
    ]
