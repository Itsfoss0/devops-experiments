# Generated by Django 4.2.7 on 2023-12-24 14:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('reg_no', models.CharField(max_length=10)),
                ('level', models.CharField(choices=[('Freshman', 'Freshman'), ('Junior', 'Junior'), ('Senior', 'Senior')], default='Freshman', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Math', 'Math'), ('Science', 'Science'), ('History', 'History')], max_length=10)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
    ]