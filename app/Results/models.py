from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from io import BytesIO
from django.core.files.base import ContentFile
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from app.quiz.models import Topic


class ResultsTest(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='tests', verbose_name='Тема')
    name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Email пользователя')
    score = models.PositiveIntegerField(verbose_name='Набранные баллы')
    total_questions = models.PositiveIntegerField(verbose_name='Всего вопросов')
    correct_answers = models.PositiveIntegerField(verbose_name='Правильные ответы')
    wrong_answers = models.PositiveIntegerField(verbose_name='Неправильные ответы')
    percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процент правильных ответов')
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True, verbose_name='Сертификат (PDF)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата прохождения')

    def __str__(self):
        return f"Тест по теме '{self.topic.name}' от {self.name} ({self.email})"

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'
        ordering = ['-created_at']


@receiver(post_save, sender=ResultsTest)
def generate_certificate(sender, instance, created, **kwargs):
    if created and not instance.certificate:
        # Создание контекста для шаблона
        context = {
            'name': instance.name,
            'topic': instance.topic.name,
            'percentage': instance.percentage,
            'correct_answers': instance.correct_answers,
            'total_questions': instance.total_questions,
            'date': instance.created_at.strftime('%d-%m-%Y'),
        }

        # Рендерим HTML из шаблона
        html_string = render_to_string('certificate_template.html', context)

        # Генерация PDF из HTML с помощью xhtml2pdf
        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

        if pisa_status.err:
            print("Ошибка при генерации PDF")

        # Сохранение PDF в поле certificate
        pdf_file.seek(0)
        filename = f"certificate_{instance.id}.pdf"
        instance.certificate.save(filename, ContentFile(pdf_file.read()))
