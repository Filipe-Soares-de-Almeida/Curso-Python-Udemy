from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_date', 'show')
  search_fields = ('first_name', 'last_name', 'phone', 'email')
  list_per_page = 10
  list_max_show_all = 100
  list_display_links = ('id', 'first_name')
  list_editable = ('show',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)
  ordering = ('-id',) 