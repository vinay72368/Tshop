from django.db import models





class TshirtProperties(models.Model):
    title = models.CharField(max_length=30, null=False)
    slug = models.CharField(max_length=30, null=False , unique= True)

    def __str__(self) -> str:
        return self.title

    class Meta :
        abstract = True

# Create your models here.
class Occassion(TshirtProperties):
    pass
class IdealFor(TshirtProperties):
    pass
class NeckType(TshirtProperties):
    pass
class Sleeve(TshirtProperties):
    pass
class Brand(TshirtProperties):
    pass
class Color(TshirtProperties):
    pass
