from django.db import models

# Create your models here.

class Blog(models.Model):
    name_blog = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    count_views = models.IntegerField(default=0)


    def __str__(self):
        return self.name_blog

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
