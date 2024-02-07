from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail, EmailMultiAlternatives
from datetime import datetime
from rpg_portal import settings
from .models import Post
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm
from django.db.models.signals import post_save
from .tasks import send_mail_after_news_comment
#from .mixins import UserToFormMixin


def notify_about_new_post(sender, **kwargs):
    pass
    # for user in Subscribers.objects.filter(category=kwargs['instance'].category):
    #     send_mail(
    #         subject='Новый пост',
    #         message=f'Новый пост в категории {kwargs["instance"].category}',
    #         from_email=settings.DEFAULT_FROM_EMAIL,
    #         recipient_list=[user.email],
    #         fail_silently=False,)


post_save.connect(notify_about_new_post, sender=Post)

class ProtectedPostsView(LoginRequiredMixin, ListView):
    template_name = 'posts.html'


class PostsList(ListView):
    model = Post
    ordering = '-date_of_post'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostFilter(self.request.GET, queryset)
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_comments(self):
        return Comment.objects.filter(post=self.get_object())


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'portal.add_post'
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    send_mail_after_news_comment()

    def form_valid(self, form):
        post = form.save(commit=False)
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'portal.change_post'
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'portal.delete_post'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class MyView(PermissionRequiredMixin, ListView):
    permission_required = 'protect.view_post'