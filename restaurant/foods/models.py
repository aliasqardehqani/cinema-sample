from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from django.utils import timezone
class Foods(models.Model):
    FOOD_TYPE = [
        ("B", "صبحانه"),
        ("DR", "نوشیدنی"),
        ("L", "ناهار"),
        ("D", "شام"),
    ]
    name = models.CharField(_('نام غذا'), max_length=100)
    description = models.CharField(_("توضیحات"), max_length=300)
    discount = models.IntegerField(default=0)
    rate = models.IntegerField(_("امتیاز"))
    price = models.IntegerField(_("قیمت"))
    time = models.DateField(_("زمان  انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to="media/")
    type_food = models.CharField(_("نوع غذا"), max_length=10, choices=FOOD_TYPE, default='DR')


class Comment(models.Model):
    post = models.ForeignKey('foods.Foods', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.author)

class Sales(models.Model):
    f_name = models.CharField(max_length=25, null=False)
    l_name = models.CharField(max_length=25, null=False)
    numbers = models.IntegerField()
    email = models.EmailField(max_length=250, null=False, unique=True, default='ali@gmail.com')
    address = models.TextField()
    post_num = models.IntegerField()
    receiver_name = models.CharField(max_length=20, null=False)
