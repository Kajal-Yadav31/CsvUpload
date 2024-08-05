from django.db import models


class Upload(models.Model):
    Dataset_name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.Dataset_name:
            self.Dataset_name = self.file.name
        super().save(*args, **kwargs)
