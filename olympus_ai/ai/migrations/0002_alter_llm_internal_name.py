# Generated by Django 5.1.7 on 2025-03-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llm',
            name='internal_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
