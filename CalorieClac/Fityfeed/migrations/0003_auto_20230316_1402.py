# Generated by Django 3.2.13 on 2023-03-16 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fityfeed', '0002_auto_20230315_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg_tbl',
            old_name='em',
            new_name='em1',
        ),
        migrations.RenameField(
            model_name='reg_tbl',
            old_name='ps',
            new_name='psc1',
        ),
        migrations.RenameField(
            model_name='reg_tbl',
            old_name='fn',
            new_name='unm',
        ),
    ]
