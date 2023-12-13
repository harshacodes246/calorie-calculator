from django.contrib import admin
from .models import reg_tbl,Fooditem

# Register your models here.
admin.site.register(reg_tbl),
admin.site.register(Fooditem),
# class foodAdmin(admin.ModelAdmin):
#     class Meta:
#         model=Fooditem
#     list_display=['name']
#     list_filter=['name']
# admin.site.register(Customer)
# admin.site.register(UserFooditem)
# admin.site.register(Category)
# admin.site.register(Fooditem,foodAdmin)
