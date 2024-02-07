from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import Post, Comment
from django.contrib.auth.models import User as auth_user
import datetime


@shared_task
def send_mail_after_news_comment():
    pass

    # for user in Subscribers.objects.all():
    #     user_mail = auth_user.objects.get(id=user.user_id).email
    #     if Post.objects.filter(category=user.category, date_of_post=datetime.date.today()).exists():
    #         message_for_subscriber = f'{Post.objects.filter(category=user.category, date_of_post=datetime.date.today()).first().post_text}'
    #     else:
    #         message_for_subscriber = 'Новостей нет'
    #     if user_mail is None:
    #         continue
    #     else:
    #         send_mail(
    #             subject=f'Новый пост в категории {user.category}',
    #             message= message_for_subscriber,
    #             from_email=settings.DEFAULT_FROM_EMAIL,
    #             recipient_list=[user_mail],
    #             fail_silently=False,)
