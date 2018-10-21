from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=50, default='title')
    description=models.CharField(max_length=50, default='description')
    date = models.DateTimeField(default=datetime.now,blank=True)
    status = models.CharField(max_length=50, default='status')
    created_date = models.DateTimeField(default=datetime.now,blank=True)
    modified_date = models.DateTimeField(default=datetime.now,blank=True)
	
    def __unicode__(self):
        return self.title
		
    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk':self.pk})