from django.db import models


# Create your models here.
class Header(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='headers', null=True, blank=True)

    def __str__(self):
        return self.text


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='services', null=True, blank=True)
    icon_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    image = models.ImageField(upload_to='banners', null=True, blank=True)
    client_count = models.CharField(max_length=12, default=1)
    text = models.TextField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.text


class SkillsTitle(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class WorkProgress(models.Model):
    icon = models.ImageField(upload_to='works/',null=True,blank=True)
    icon_url = models.CharField(null=True, blank=True, max_length=144)
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=255)
    description = models.TextField()

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Portfolios"


class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    position = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='blogs/')
    content = models.TextField(blank=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def embed_url(self):
        if self.video_url:
            # Agar URL "watch?v=" bo'lsa, uni embed formatiga o'zgartiradi
            if "watch?v=" in self.video_url:
                return self.video_url.replace("watch?v=", "embed/")
            # Agar URL "youtu.be/" bo'lsa, uni embed formatiga o'zgartiradi
            elif "youtu.be/" in self.video_url:
                return self.video_url.replace("youtu.be/", "www.youtube.com/embed/")
        return None

    class Meta:
        verbose_name_plural = "Blogs"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CompanyData(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name



