# Generated by Django 2.2.6 on 2019-10-16 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTimeCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sitecode', models.CharField(max_length=50)),
                ('nameofcontracter', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserTimeCardMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Totalhrs', models.CharField(max_length=50)),
                ('Totalamount', models.CharField(max_length=50)),
                ('MachineCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administer.Job')),
                ('Sitecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.UserTimeCard')),
            ],
        ),
        migrations.CreateModel(
            name='UserTimeCardLabor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Totalhrs', models.CharField(max_length=50)),
                ('Totalamount', models.CharField(max_length=50)),
                ('JobCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administer.Job')),
                ('Sitecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.UserTimeCard')),
            ],
        ),
    ]
