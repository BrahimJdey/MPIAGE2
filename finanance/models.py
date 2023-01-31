from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "User: "+self.username
    
    
class Client(models.Model):
    Name = models.CharField(max_length=40,null=False)
    # LastName = models.CharField(max_length=40)
    # profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40,)
    mobile = models.CharField(max_length=20,null=False)
    Type =models.ForeignKey("Type",on_delete=models.CASCADE)
   
    def __str__(self):
        return self.Name
    
class Type(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Fournisseur(models.Model):
    Name = models.CharField(max_length=40)
    # LastName = models.CharField(max_length=40)
    # profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    Type =models.ForeignKey(Type,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name

class FactureCl(models.Model):
    code = models.CharField(max_length = 100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    journal = models.CharField(max_length = 100)
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    date_facturation = models.DateField()
    HTaxe = models.FloatField()
    
    def __str__(self):
        return self.code
    @property
    def total(self):
        Total = ((self.produit.quantity+self.produit.prix) * self.HTaxe) + (self.produit.quantity+self.produit.prix)
        return Total
    
class FactureFr(models.Model):
    code = models.CharField(max_length = 100)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    journal = models.CharField(max_length = 100)
    date_facturation = models.DateField()
    HTaxe = models.FloatField()
    
    def __str__(self):
        return self.code
    @property
    def total(self):
        Total = -((self.produit.quantity+self.produit.prix) * self.HTaxe) - (self.produit.quantity+self.produit.prix)
        return Total
    
class Produit(models.Model):
    libelle = models.CharField(max_length = 100)
    quantity = models.FloatField()
    prix = models.FloatField()
    

    def __str__(self):
        return self.libelle

class Journal(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
class PieceCompt(models.Model):
    ref = models.FloatField()
    date_comptable = models.DateField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    partenaire = models.ForeignKey(Client, on_delete=models.CASCADE)
    deb = models.FloatField()
    cred = models.FloatField()
    @property
    def total(self):
        Total = self.deb-self.cred
        return Total
    
    