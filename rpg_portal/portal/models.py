from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.urls import reverse


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title_of_post = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_text = models.TextField()
    date_of_post = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('category', through='PostCategory')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_of_comment = models.DateTimeField(auto_now_add=True)

    def accept(self):
        self.accepted = True
        self.save()

    def decline(self):
        self.accepted = False
        self.save()

    def leave_a_comment(self):
        return self.comment_text


    def get_comment_author(self):
        return self.user

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)