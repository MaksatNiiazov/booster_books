# Generated by Django 5.1.3 on 2024-12-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
