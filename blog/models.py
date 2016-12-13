from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    Post Class inheriting "models.Model" creating Post model for blog posts.
    a Django Model in a database is a spreadsheet with columns (fields) and rows (data).
    For more field types not used here look at https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types

    to create tables for models in database:
        python manage.py makemigrations blog
        python manage.py migrate blog
    """

    author = models.ForeignKey('auth.User')  # this is a link to another model
    title = models.CharField(max_length=200)
    text = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """  """

        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        """  """

        return self.title
