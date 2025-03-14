# Generated by Django 5.1.7 on 2025-03-13 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0002_alter_llm_internal_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Math', 'Math'), ('Plotting', 'Plotting'), ('User Comms', 'User Comms'), ('Internet Browsing', 'Internet Browsing'), ('API', 'API')], max_length=200)),
                ('source_code', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LLMConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(default=0.0)),
                ('system_prompt', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('llm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ai.llm')),
            ],
        ),
    ]
