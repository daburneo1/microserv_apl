# Generated by Django 3.1.6 on 2021-02-16 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0004_auto_20210216_0329'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='state',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='state', to='appi.coursestate'),
        ),
    ]