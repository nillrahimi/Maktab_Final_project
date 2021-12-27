from django.db import models
from accounts.models import Manager


class TypeCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField( max_length=50)
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE, related_name="restaurant_branch")
    manager_id = models.ForeignKey("accounts.Manager", on_delete=models.CASCADE)
    type_category = models.ForeignKey(TypeCategory,on_delete=models.CASCADE)
    city = models.CharField( max_length=50)
    address = models.CharField( max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)


class MealCategory(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=50)
    type_category = models.ForeignKey(TypeCategory, on_delete=models.CASCADE,related_name = "typecategory_food")
    meal_category = models.ManyToManyField(MealCategory,related_name = "mealcategory_food" )
    description = models.CharField( max_length=300,null=True,blank =True)
    image = models.ImageField(upload_to='media/')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Menu(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE,related_name = "food_menu")
    remaining = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.food_id ,self.branch_id)


class OrderStatus(models.Model):
    status = models.CharField( max_length=50)

    def __str__(self):
        return self.status


class Order(models.Model):
    orderstatus_id = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, related_name='orderstatus_order')
    customer_id = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE,related_name = "customer_order")
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} {}'.format(self.customer_id ,self.orderstatus_id)


class OrderItem(models.Model):
    menu_id = models.ManyToManyField(Menu, related_name='menu_orderitem')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return '{} {}'.format(self.order_id ,self.menu_id)
        

class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    alley =  models.CharField(max_length=50)
    number = models.IntegerField()
    customer_id = models.ManyToManyField('accounts.Customer', related_name='customer_address')
    def __str__(self):
        return '{} {}'.format(self.street ,self.customer_id)



