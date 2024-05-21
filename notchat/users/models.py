from django.db import models

# use to make an custom User Model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import identify_hasher


class UserModelManager(BaseUserManager):
    def create_user(
        self,
        password,
        email="",
        username="",
        passwd="",
    ):
        # check email if its empty or not
        if not email:
            raise ValueError("Email is Required")
        #
        #
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            passwd=passwd,
        )
        # user.set_password(password)
        # user.passwd = password
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        password,
        email,
        username="",
        passwd="",
    ):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            passwd=f"{passwd}{password}",
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="ایمیل",
        max_length=250,
        unique=True,
    )
    username = models.CharField(
        verbose_name="نام کاربری",
        max_length=250,
        blank=True,
        null=True,
    )
    img_prof = models.ImageField(
        verbose_name="عکس",
        upload_to="img/users/",
        blank=True,
        null=True,
    )

    # default django user fields
    date_joined = models.DateTimeField(
        verbose_name="زمان پیوستن",
        auto_now_add=True,
        unique=True,
    )
    last_login = models.DateTimeField(verbose_name="آخرین ورود", auto_now=True)
    updated = models.DateTimeField(verbose_name="بروزرسانی", auto_now=True)
    #
    is_admin = models.BooleanField(verbose_name="مدیر", default=False)
    is_active = models.BooleanField(verbose_name="فعال", default=False)
    is_staff = models.BooleanField(verbose_name="کارمند", default=False)
    is_superuser = models.BooleanField(verbose_name="سوپریوزر", default=False)
    # end default django user fields

    # check for signup
    is_in_signup = models.BooleanField(verbose_name="در مرحله ی ثبت", default=True)
    passwd = models.CharField(verbose_name="رمز", max_length=200, null=True, blank=True)
    # end check for signup

    # token
    tmp_token = models.CharField(
        verbose_name="توکن موقت",
        max_length=10,
        null=True,
        blank=True,
    )
    tmp_token_time = models.DateTimeField(
        verbose_name="زمان توکن موقت",
        null=True,
        blank=True,
    )
    # end token

    # object manger
    objects = UserModelManager()
    # object manger

    USERNAME_FIELD = "email"  # use email for username

    # show first part of email (-> before @)
    def __str__(self):
        return str(self.email).split("@")[0]
        # return self.username

    def save(self, *args, **kwargs):
        try:
            hasher = identify_hasher(self.password)
        except:
            self.set_password(self.passwd)
            # self.passwd = ""

        super(UserModel, self).save(*args, **kwargs)

    # default django user method
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # end default django user method
