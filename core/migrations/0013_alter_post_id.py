# Generated by Django 4.2.3 on 2023-07-31 14:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cd3bc4c1-c4e9-4a62-ac27-f01359efe4b1'), primary_key=True, serialize=False),
        ),
    ]