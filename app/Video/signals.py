from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from app.Video.models import Video

@receiver(post_migrate)
def load_video_data(sender, **kwargs):
    if not Video.objects.exists():call_command('loaddata', 'app/Video/fixtures/initial_video_data.json')
