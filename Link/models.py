from django.db import models
from uuid import uuid4

# Create your models here.
class DBLink(models.Model):
    link = models.CharField(max_length=200)
    short = models.CharField(max_length=7)

    def create_short_link(self, link_text: str):
        if link_text is not None and link_text != "":
            self.link = link_text
        x = self.generate()
        while DBLink.objects.filter(short=x).exists():
            x = self.generate()
        self.short = x
        self.save()


    def generate(self) -> str:
        return str(uuid4())[0:7]


    def get_link_from_short(self, short_code: str):
        pass