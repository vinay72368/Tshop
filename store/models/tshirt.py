from django.db import models


from store.models.tshirt_properties import Brand, Color, Occassion, IdealFor,NeckType, Sleeve 
class Tshirt(models.Model):
    name = models.CharField(max_length=50,null=False)
    slug = models.CharField(max_length=200,null=True , unique=True, default="")
    description = models.CharField(max_length=50,null=True)
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='upload/images' , null=False)
    occassion = models.ForeignKey(Occassion,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    sleeve = models.ForeignKey(Sleeve,on_delete=models.CASCADE)
    necktype = models.ForeignKey(NeckType,on_delete=models.CASCADE)
    idealfor = models.ForeignKey(IdealFor,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name