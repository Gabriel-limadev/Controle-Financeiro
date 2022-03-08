# Generated by Django 4.0.2 on 2022-02-26 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Categorie',
                'db_table': 'categorie',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Revenue',
                'db_table': 'revenue',
                'ordering': ['date', 'value'],
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('categorie', models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='finance.categorie')),
            ],
            options={
                'verbose_name': 'Expense',
                'db_table': 'expense',
                'ordering': ['date', 'value'],
            },
        ),
    ]
