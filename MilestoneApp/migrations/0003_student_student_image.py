# Generated by Django 3.1 on 2020-09-02 15:02

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MilestoneApp', '0002_auto_20200818_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_image',
            field=versatileimagefield.fields.VersatileImageField(default='No image', upload_to='profile'),
            preserve_default=False,
        ),
    ]
