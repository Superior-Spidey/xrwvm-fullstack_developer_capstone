# from django.contrib import admin
# from .models import CarMake, CarModel

# # Register your models here.
# #admin.site.register(CarMake)
# #admin.site.register(CarModel)

# # CarModelInline class
# class CarModelInline(admin.StackedInline):
#     model = CarModel
#     extra = 5
# # CarModelAdmin class
# class CarModelAdmin(admin.ModelAdmin):
#     fields = ['make', 'name', 'type','year']
#     inlines = [CarModelInline]
# # CarMakeAdmin class with CarModelInline
# class CarMakeAdmin(admin.ModelAdmin):
#     fields = ['name', 'description']
# # Register models here
# admin.site.register(CarMake, CarMakeAdmin)
# admin.site.register(CarModel, CarModelAdmin)

from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 0  # Change to 0 if you don't want to show extra empty forms

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

class CarModelAdmin(admin.ModelAdmin):
    fields = ['make', 'name', 'type', 'year']

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
