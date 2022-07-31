from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#memory test uploaded by admin
class Test(models.Model):
	test_title = models.CharField(max_length=100)
	display_image = models.ImageField(upload_to='memtest_display_pics')
	html_file = models.FileField() #upload file to templates/memtests 
	css_file = models.FileField() #upload file to static/memtests/css
	js_file = models.FileField() #upload file to static/memtests/js]

	def __str__(self):
		return self.test_title

#user's test result (per test taken)
class TestResult(models.Model):
	test = models.ForeignKey(Test, on_delete=models.PROTECT, related_name='test')
	score = models.IntegerField() #get from test.js
	date_tested = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

