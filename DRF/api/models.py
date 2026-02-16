from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model
User = get_user_model()



choices= (
    ('A','A'),
    ('B',"B"),
    ('C','C')
)
class Product(models.Model):
    name= models.CharField(max_length=30)  
    price=models.IntegerField()
    category= models.CharField(max_length=1,choices=choices)
    available_stock= models.IntegerField()
    
    def clean(self):
        if (self.available_stock<=0):
            raise ValidationError("Stock can not be negative")
    def __str__(self):
        
        return f"name : {self.name}"
    

payment_methods=(
    ('COD','COD'),
    ('Bank',"Bank")
)
STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateField(auto_now_add=True)
    status= models.CharField(max_length=10,choices=STATUS_CHOICES)
    payment_method= models.CharField(max_length=4,choices=payment_methods)
    
    def __str__(self):
        return f"date= {self.date}"
        
  
  
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def total_items(self):
        return sum(item.quantity for item in self.cartitem_set.all())

    @property
    def total_price(self):
        return sum(
            item.quantity * item.product.price
            for item in self.cartitem_set.all()
        )

           
    

    
    

class Cart_item(models.Model):
    
    cart= models.ForeignKey(Cart,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"id= {self.id}"
    
class Order_item(models.Model):
    
    order= models.ForeignKey(Order,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.IntegerField()
    price_at_purchase= models.IntegerField()
    
    
    def __str__(self):
        return f"id= {self.id}"
    
        
    
