from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# Barcha modellarning ro'yxatini olamiz
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass  # Agar model avval ro'yxatdan o'tgan bo'lsa, xatolikni e'tiborsiz qoldiramiz

