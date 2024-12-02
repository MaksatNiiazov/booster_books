# Generated by Django 5.1.3 on 2024-12-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
