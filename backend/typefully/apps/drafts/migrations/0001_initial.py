# Generated by Django 5.0 on 2024-06-14 16:59

import typefully.apps.drafts.utils.empty_editor_content
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.JSONField(default=typefully.apps.drafts.utils.empty_editor_content.make_empty_editor_content, null=True)),
                ('preview', models.CharField(default='', max_length=256)),
            ],
        ),
    ]
