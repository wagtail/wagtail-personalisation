# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 07:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtail_personalisation', '0012_remove_personalisablepagemetadata_is_segmented'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalisationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailed_visits', models.BooleanField(default=False, help_text='Enable to gather more detailed metadata about the visits to your segments and the rules that matched. Please note that this will create additional load on your database. Usage of caching is recommended.')),
                ('reverse_match', models.BooleanField(default=False, help_text='Enable to reverse match past visits with users as soon as a user logs in. This will ensure your data is as complete as possible.')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SegmentVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(db_index=True, editable=False, max_length=64, null=True)),
                ('visit_date', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
            ],
        ),
        migrations.CreateModel(
            name='SegmentVisitMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matched_rules', models.CharField(max_length=2048)),
            ],
        ),
        migrations.RemoveField(
            model_name='segment',
            name='visit_count',
        ),
        migrations.AddField(
            model_name='segmentvisitmetadata',
            name='segment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtail_personalisation.Segment'),
        ),
        migrations.AddField(
            model_name='segmentvisitmetadata',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtail_personalisation.SegmentVisit'),
        ),
        migrations.AddField(
            model_name='segmentvisit',
            name='segments',
            field=models.ManyToManyField(through='wagtail_personalisation.SegmentVisitMetadata', to='wagtail_personalisation.Segment'),
        ),
        migrations.AddField(
            model_name='segmentvisit',
            name='served_segment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='served_segment', to='wagtail_personalisation.Segment'),
        ),
        migrations.AddField(
            model_name='segmentvisit',
            name='served_variant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='served_variant', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='segmentvisit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]