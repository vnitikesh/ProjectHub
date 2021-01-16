# Generated by Django 3.1.5 on 2021-01-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('codebase_link', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('technology_used', models.CharField(blank=True, max_length=225, null=True)),
                ('graphic', models.FileField(blank=True, max_length=200, null=True, upload_to=None)),
            ],
        ),
    ]
