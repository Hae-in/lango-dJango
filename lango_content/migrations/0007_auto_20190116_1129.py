# Generated by Django 2.1.4 on 2019-01-16 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lango_content', '0006_auto_20190116_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='pattern',
            field=models.ManyToManyField(related_name='pattern_tag', to='lango_content.PatternType'),
        ),
    ]
