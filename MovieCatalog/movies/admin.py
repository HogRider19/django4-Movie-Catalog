from django.contrib import admin
from django import forms
from . import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = models.Movie
        fields = '__all__'


class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'draft']
    actions = ['publish', 'unpublish']
    form = MovieAdminForm

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=False)
        if row_update == 1: 
            message_bit = '1 запись обновлена'
        else:
            message_bit = f"{row_update} записисей обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=True)
        if row_update == 1: 
            message_bit = '1 запись была добавлена'
        else:
            message_bit = f"{row_update} записисей были добавлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change', )

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change', )



admin.site.register(models.Category)
admin.site.register(models.Actor, ActorAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.MovieShorts)
admin.site.register(models.RatingStar)
admin.site.register(models.Rating)
admin.site.register(models.Review)
admin.site.register(models.Treller)
