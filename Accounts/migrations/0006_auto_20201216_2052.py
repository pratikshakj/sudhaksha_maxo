# Generated by Django 3.1.3 on 2020-12-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_classroom_classid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='class_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='class_sec',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='class_subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]