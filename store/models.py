
from django.db.models.fields.related import ManyToManyField
from profiles.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
#=======================Peofile==================================================================================================================

        
#===================Categories====================================
class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, null=True, blank=True)
    image = models.ImageField(blank=True)
   # slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Catégories'

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    @property
    def imageCat(self):
        try:
            if self.image.url !='':
                image=self.image.url
        except:
            image='store/img/dkandroid.png'
        return image

    def __str__(self):
        return self.name

#=========================Product===========================================
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, verbose_name='Catégorie', on_delete=models.RESTRICT, null=True, blank=True)
    # slug = models.SlugField( unique=True, max_length=200)
    price = models.IntegerField( verbose_name='Prix réduit')
    oldPrice = models.IntegerField(verbose_name='Prix Normal' )
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Produits'
        ordering = ('-added_at',)
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    @property
    def CategoryExcept(self):
        try:
            
            categoryName = self.category.name
        except:
            categoryName=''
        return categoryName


    def __str__(self):
        return 'Nom: {0}'.format(self.name)


#=========================Commandes==================================================
class Order(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, verbose_name='Client', null=True, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Commandes'
        ordering = ('-ordered_at',)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.qty for item in orderitems])
        return total
        
    def __str__(self):
        return 'Commande Numéro {0}'.format(str(self.id))

#=====================OrderItem=========================================================
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,verbose_name='Produit',blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, verbose_name='Element_de_commande',blank=True, null=True)
    qty = models.IntegerField(default=0, verbose_name="Quantité", blank=True, null=True)
    ordered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Eléments de commande'
        verbose_name = 'Elément de commande'
    @property
    def get_total(self):
        total = self.product.price * self.qty
        return total
    

    def __str__(self):
        return ' {0} {1} par {2}'.format(str(self.qty), self.product.name,self.order.profile)

#===========================Adresse de livraison============================================
class ShippingAddress(models.Model):
    """docstring for ShippingAdress"""
    profile=models.ForeignKey(
        Profile, verbose_name='Adresse_de_livraison' , on_delete=models.SET_NULL , null=True)
    order=models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name='Commande liée', blank=True, null=True)
    address=models.CharField(max_length=200, null=True)
    city=models.CharField(max_length=200, null=True)
    state=models.CharField(max_length=200, null=True)
    zipcode=models.CharField(max_length=200, null=True)
    ordered_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Adresse de livraison'
        ordering=('-ordered_at',)

    def __str__(self):
        return '{0}: {1} {2}, {3}'.format(self.profile, self.address,self.city,self.state)
