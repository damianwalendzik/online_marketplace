from django import path

from . import views

urls = [
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]