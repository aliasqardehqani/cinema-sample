from django.urls import path
from .views import food_list, food_detail, add_comment, discount, contact
app_name = 'foods'

urlpatterns = [
    path("", food_list, name='food_list'),
    path("<int:id>/", food_detail, name='detail'),
    path('<int:pk>', add_comment, name='addComment'),
    path('<int:pk>/comment.html/', add_comment, name='addComment'),
    path('discount/', discount, name='discount'),
    path('contact/', contact, name='contact'),

]
