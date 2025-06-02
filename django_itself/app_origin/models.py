from django.db import models

class News(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    main_text = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.name