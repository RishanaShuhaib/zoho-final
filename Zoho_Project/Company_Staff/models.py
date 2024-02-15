from django.db import models
from Register_Login.models import *

class Unit(models.Model):
    unit_name=models.CharField(max_length=255)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
class Items(models.Model):
    item_type=models.CharField(max_length=255)
    item_name=models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    hsn_code=models.IntegerField(null=True,blank=True)
    tax_reference=models.CharField(max_length=255,null=True)
    intrastate_tax=models.IntegerField(null=True,blank=True)
    interstate_tax=models.IntegerField(null=True,blank=True)

    selling_price=models.IntegerField(null=True,blank=True)
    sales_account=models.CharField(max_length=255)
    sales_description=models.CharField(max_length=255)

    purchase_price=models.IntegerField(null=True,blank=True)
    purchase_account=models.CharField(max_length=255)
    purchase_description=models.CharField(max_length=255)
   
    minimum_stock_to_maintain=models.IntegerField(blank=True,null=True)  
    inventory_account=models.CharField(max_length=255,null=True)

    date=models.DateTimeField(auto_now_add=True)                                       

    opening_stock=models.IntegerField(blank=True,null=True,default=0)
    is_active = models.CharField(max_length=255,null=True)
    current_stock=models.IntegerField(blank=True,null=True,default=0)
    opening_stock_per_unit=models.IntegerField(blank=True,null=True,)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)

    track_inventory=models.IntegerField(blank=True,null=True)
class Godown(models.Model):
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    date = models.DateField()
    HSN = models.CharField(max_length=255)
    stock_in_hand = models.IntegerField()
    godown_name = models.CharField(max_length=255)
    godown_address = models.CharField(max_length=255)
    stock_keeping = models.IntegerField()
    distance = models.IntegerField()
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, related_name='godowns')
    is_edited = models.BooleanField(default=False)
class Comment(models.Model):
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    godown = models.ForeignKey(Godown, related_name='comments', on_delete=models.CASCADE)
class Godownhistory(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,related_name="history")
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,related_name="history")
    godown = models.ForeignKey(Godown, on_delete=models.CASCADE,related_name="history")
    current_date = models.DateField(auto_now_add=True)
class Holiday(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    holiday_name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(LoginDetails, on_delete=models.CASCADE, null=True, blank=True)
    company=models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateField(null=True, blank=True)
    is_edited = models.BooleanField(default=False)
class CommentHoliday(models.Model):
    holidaymonth = models.CharField(max_length=7)
    comment_text = models.TextField()