# Generated by Django 3.1.6 on 2021-02-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kisi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adi', models.CharField(max_length=50, verbose_name='Adı')),
                ('soyadi', models.CharField(max_length=50, verbose_name='Soyadı')),
                ('tel', models.CharField(blank=True, max_length=20, verbose_name='Telefonu')),
                ('adres', models.TextField(blank=True, verbose_name='Adresi')),
            ],
        ),
    ]