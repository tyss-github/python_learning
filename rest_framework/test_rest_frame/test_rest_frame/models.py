#coding:utf-8
from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
LANGUAGE_CHOICES = ((0, '中文'), (1, '英文'))
STYLE_CHOICES = ((0, '散文'), (1, '诗歌'), (1, '技术博文'))


class Article(models.Model):
    """
    文章的简要说明
    """
    title = models.CharField(max_length=100, blank=True, default='', verbose_name="文章标题")
    content = models.TextField(verbose_name="文章内容")
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100, verbose_name="语言")
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="发表日期")

    class Meta:
        ordering = ('created',)
