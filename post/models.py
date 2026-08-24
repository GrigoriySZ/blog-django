from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name='Заголовок',
        help_text='Введит заголовок поста'
    )
    content = models.TextField(
        verbose_name='Содержание',
        help_text='Введите текст поста'
    )
    created_at = models.DateTimeField(
        # Фиксирует один раз при добавлении
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_at = models.DateTimeField(
        # Фиксирует каждый раз при обновлении
        auto_now=True,
        verbose_name='Дата обновления '
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
        ordering = ['-created_at']