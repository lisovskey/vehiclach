from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Mark, Model


@receiver(pre_save, sender=Mark)
@receiver(pre_save, sender=Model)
def slugify(sender, instance, *args, **kwargs):
    instance.slug = instance.name.replace(' ', '_')
