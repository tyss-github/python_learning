#coding:utf-8
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


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
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code article.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.content, lexer, formatter)
        super(Article, self).save(*args, **kwargs)
