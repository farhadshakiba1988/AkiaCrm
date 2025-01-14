from django.contrib import admin

from web.models import Employee, ProductCategory, EmployeeExpertise, Customer, CustomerInteraction, Sale, \
    PerformanceMetric, Territory, Product, SaleItem

admin.site.register(Employee)
admin.site.register(ProductCategory)
admin.site.register(EmployeeExpertise)
admin.site.register(Customer)
admin.site.register(CustomerInteraction)
admin.site.register(Sale)
admin.site.register(PerformanceMetric)
admin.site.register(Territory)
admin.site.register(Product)
admin.site.register(SaleItem)
