# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 14:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SignedStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signedStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='student')),
            ],
            options={
                'verbose_name': 'signedStudents',
                'verbose_name_plural': 'signedStudents|plural',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherName', models.TextField(max_length=200, verbose_name='teacher|name')),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teacher|plural',
            },
        ),
        migrations.CreateModel(
            name='TeacherGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherGradeShort', models.TextField(max_length=5, verbose_name='teacherGrade|short')),
                ('teacherGradeLong', models.TextField(max_length=10, verbose_name='teacherGrade|long')),
            ],
            options={
                'verbose_name': 'teacherGrade',
                'verbose_name_plural': 'teacherGrade|plural',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termName', models.TextField(max_length=200, verbose_name='term|name')),
                ('termMaxStudents', models.IntegerField(default=15, verbose_name='term|maxStudents')),
                ('termTeacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.Teacher')),
            ],
            options={
                'verbose_name': 'term',
                'verbose_name_plural': 'term|plural',
            },
        ),
        migrations.CreateModel(
            name='TermTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStart', models.TimeField(verbose_name='termTime|start')),
                ('timeStop', models.TimeField(verbose_name='termTime|stop')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.Term', verbose_name='term')),
            ],
            options={
                'verbose_name': 'termTime',
                'verbose_name_plural': 'termTime|plural',
            },
        ),
        migrations.CreateModel(
            name='TermType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.TextField(max_length=100, verbose_name='termType|name')),
            ],
            options={
                'verbose_name': 'termType',
                'verbose_name_plural': 'termType|plural',
            },
        ),
        migrations.AddField(
            model_name='term',
            name='termType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.TermType'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacherGrade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.TeacherGrade'),
        ),
        migrations.AddField(
            model_name='signedstudents',
            name='signedTermTime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.TermTime', verbose_name='term'),
        ),
    ]
