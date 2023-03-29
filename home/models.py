from django.db import models
import uuid
from django.contrib.auth.models import User
 
class Blog(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4)
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    main_image = models.ImageField(upload_to='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

