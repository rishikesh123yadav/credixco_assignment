# Generated by Django 3.1.4 on 2021-04-07 06:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_auto_20201212_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='creator_teacherId',
            new_name='create_by',
        ),
        migrations.AddField(
            model_name='student',
            name='creator_Id',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]