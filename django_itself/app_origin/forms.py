from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name', 'description', 'main_text', 'image']
        widgets = {
            'main_text': CKEditorWidget(),
            # Optionally, uncomment to use CKEditor for description as well
            # 'description': CKEditorWidget(config_name='default'),
        }