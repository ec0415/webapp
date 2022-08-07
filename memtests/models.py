from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#memory test uploaded by admin
class Test(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	html_file = models.FileField(upload_to='html_files') 
	css_file = models.FileField(upload_to='css_files') 
	js_file = models.FileField(upload_to='js_files') 

	def __str__(self):
		return self.test_title


#user's test result (per test taken)
#class TestResult(models.Model):
#	test = models.ForeignKey(Test, on_delete=models.PROTECT, related_name='test')
#	score = models.IntegerField() #get from test.js
#	date_tested = models.DateTimeField(default=timezone.now)
#	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

