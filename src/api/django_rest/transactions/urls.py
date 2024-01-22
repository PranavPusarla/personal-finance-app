from django.urls import path
from transactions import views

urlpatterns = [
    path('transactions/', views.transaction_list),
    path('transactions/unclassified', views.unclassified_transaction_daily)
]