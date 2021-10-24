# Generated by Django 3.1.1 on 2021-10-04 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('view_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('release_date', models.DateField()),
                ('arist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_list', to='view_main.musician')),
            ],
        ),
    ]