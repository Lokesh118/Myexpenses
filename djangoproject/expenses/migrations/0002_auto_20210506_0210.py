# Generated by Django 3.2 on 2021-05-06 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='data',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=266),
        ),
    ]
