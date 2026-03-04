from django.db import models

# Create your models here.
class job_description(models.Model):
    jd_file=models.FileField(upload_to="job",blank=True)
    resume_folder=models.FileField(blank=True)

