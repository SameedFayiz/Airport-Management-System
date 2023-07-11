# Generated by Django 4.2.3 on 2023-07-11 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=150)),
                ('line2', models.CharField(max_length=150)),
                ('postalcode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Anniversary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.address')),
                ('anniversary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport.anniversary')),
            ],
        ),
    ]