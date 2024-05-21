from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


class RoomModel(models.Model):
    name = models.CharField(
        verbose_name="نام",
        max_length=250,
    )
    desc = models.CharField(
        verbose_name="توضیحات",
        max_length=250,
    )
    slug = models.SlugField(
        verbose_name="اسلاگ",
        max_length=250,
        unique=True,
        allow_unicode=True,
        blank=True,
        null=True,
    )
    slug_time = models.DateTimeField(
        verbose_name="زمان اسلاگ",
        default=timezone.now,
    )
    created = models.DateTimeField(
        verbose_name="زمان ساخت",
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = (
            slugify(self.name, allow_unicode=True)
            + "-"
            + str(slugify(self.slug_time, allow_unicode=True)).replace("-", "")
        )

        super(RoomModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:room_page", args=[self.slug])
