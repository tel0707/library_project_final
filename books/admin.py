from django.contrib import admin
from .models import Book
from django.contrib import messages
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    field = ('title', 'author', 'publisher', 'is_active', 'is_deleted', 'year', 'isbn')
    list_display = ('title', 'author', 'publisher', 'is_active', 'is_deleted', 'year', 'isbn')
    actions =['make_active', 'make_inactive', 'make_deleted', 'make_undeleted']

    @admin.action(description='Aktiv qilish')
    def make_active(self, request, queryset):
        updated_count = queryset.update(is_active=True)
        self.message_user(
            request,
            f'{updated_count} kitob(lar) faol holatga o\'tkazildi.',
            messages.SUCCESS
        )

    @admin.action(description='Neaktiv qilish')
    def make_inactive(self, request, queryset):
        updated_count = queryset.update(is_active=False)
        self.message_user(
            request,
            f'{updated_count} kitob(lar) faol holatga o\'tkazildi.',
            messages.SUCCESS
        )
    @admin.action(description='O\'chirish')
    def make_deleted(self, request, queryset):
        updated_count = queryset.update(is_deleted=False)
        self.message_user(
            request,
            f'{updated_count} kitob(lar) o\'chirildi .',
            messages.SUCCESS
        )

    @admin.action(description='O\'chirishni bekor qilish')
    def make_undeleted(self, request, queryset):
        updated_count = queryset.update(is_deleted=True)
        self.message_user(
            request,
            f'{updated_count} kitob(lar) o\'chirildi .',
            messages.SUCCESS
        )