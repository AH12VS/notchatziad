# Generated by Django 5.0.6 on 2024-05-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=250, unique=True, verbose_name='ایمیل')),
                ('username', models.CharField(max_length=250, verbose_name='نام کاربری')),
                ('img_prof', models.ImageField(blank=True, null=True, upload_to='img/users/', verbose_name='عکس')),
                ('date_joined', models.DateTimeField(auto_now_add=True, unique=True, verbose_name='زمان پیوستن')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='آخرین ورود')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='بروزرسانی')),
                ('is_admin', models.BooleanField(default=False, verbose_name='مدیر')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('is_staff', models.BooleanField(default=False, verbose_name='کارمند')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='سوپریوزر')),
                ('is_cms_user', models.BooleanField(default=False, verbose_name='کاربر سی ام اس')),
                ('is_in_signup', models.BooleanField(default=True, verbose_name='در مرحله ی ثبت')),
                ('passwd', models.CharField(blank=True, max_length=200, null=True, verbose_name='رمز')),
                ('tmp_token', models.CharField(blank=True, max_length=10, null=True, verbose_name='توکن موقت')),
                ('tmp_token_time', models.DateTimeField(blank=True, null=True, verbose_name='زمان توکن موقت')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]