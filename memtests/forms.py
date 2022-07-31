from django import forms
from .models import Test

#admin add memory test (this is a model form -- a form that works with a specific data base model)
class TestUploadForm(forms.ModelForm):

	class Meta:
		model = Test
		fields = ['test_title', 'display_image', 'html_file', 'css_file', 'js_file']