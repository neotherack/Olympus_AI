# Generated by Django 5.1.7 on 2025-03-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0005_llm_model_quantization_alter_llm_model_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='version',
            field=models.CharField(default='latest', max_length=200),
        ),
    ]
