from django.db import models
from taggit.managers import TaggableManager
from taggit.models import Tag
import taggit_templatetags2

'''
    TODO: Learn how to filter those values when storing to database
    whether a has value is md5, sha1 or sha256
    TODO: How to connect two tables together
    TODO: How to add tags to the tag table
'''


class Hash(models.Model):
    md5 = models.CharField(max_length=32, blank=True)
    sha1 = models.CharField(max_length=40, blank=True)
    sha256 = models.CharField(max_length=64, blank=True)
    upload_tags = TaggableManager()

    def __str__(self):
        string = ''
        if self.md5 is not '':
            string += '\nmd5= ' + self.md5
        if self.sha1 is not '':
            string += '\nsha1= ' + self.sha1
        if self.sha256 is not '':
            string += '\nsha256= ' + self.sha256
        return string

    def get_tags(self):
        return self.upload_tags.names()


class SearchTag(models.Model):
    tags = models.CharField(max_length=1000)
    count = models.IntegerField(default=1)

    def as_dict(self):
        return {
            "tags": self.tags,
            "count": self.count
        }

    def __str__(self):
        string = 'Tag Name: '+self.tags + '\n' + 'count:'+str(self.count)
        return string


# TODO: find the best way to associate the hash with searchtags

