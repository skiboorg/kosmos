from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string

class ServiceName(models.Model):
    name = models.CharField('Вид работы', max_length=255, blank=False, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=False, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=False, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)
    topText = RichTextUploadingField('Верхний текст на страницу с услугой', blank=True, null=True)
    bottomText = RichTextUploadingField('Нижний текст на страницу с услугой', blank=True, null=True)
    pageTable = RichTextUploadingField('Таблица (прайс-лист)', blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        testSlug = ServiceName.objects.filter(name_slug=slug)
        slugRandom = ''
        if testSlug:
            slugRandom = '-'+''.join(choices(string.ascii_lowercase + string.digits, k=2))
        self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(ServiceName, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return f'/service/{self.name_slug}/'

    def __str__(self):
        return 'Вид работы : {}'.format(self.name)

    class Meta:
        verbose_name = "Вид работы"
        verbose_name_plural = "Виды работ"


