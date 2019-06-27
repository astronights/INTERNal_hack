from django.contrib import admin

# Register your models here.
from dashboard.models import Company, StockPrice, Score

admin.site.register(Company)
admin.site.register(StockPrice)
admin.site.register(Score)
