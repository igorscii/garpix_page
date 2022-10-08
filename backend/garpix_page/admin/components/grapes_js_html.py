import os
from django.contrib import admin
from .grepesjs_mixin import GrapesJsAdminMixin
from garpix_page.models import GrapesJsHtmlComponent
from .base_component import BaseComponentAdmin
from django.conf import settings


@admin.register(GrapesJsHtmlComponent)
class GrapesJsHtmlComponentAdmin(BaseComponentAdmin, GrapesJsAdminMixin):
    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        css = request.POST.get('html_css')
        js = request.POST.get('html_js')
        field_name = 'html'
        filename_css = f'{settings.MEDIA_ROOT}/grapesjs/{field_name}_{obj.pk}_css.css'
        filename_js = f'{settings.MEDIA_ROOT}/grapesjs/{field_name}_{obj.pk}_js.js'
        os.makedirs(os.path.dirname(filename_css), exist_ok=True)
        with open(filename_css, "w") as f:
            f.write(css)

        os.makedirs(os.path.dirname(filename_js), exist_ok=True)
        with open(filename_js, "w") as f:
            f.write(js)

        return obj
