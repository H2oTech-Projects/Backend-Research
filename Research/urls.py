from django.urls import path
from . import views

urlpatterns = [
    #path('update-balance/', views.update_balance, name='update_balance'),
    path('transfer-balance/', views.transfer_balance, name='transfer_balance'),
    path('nested-transaction/', views.nested_transaction_example, name='nested'),
    path('atomic-request/', views.atomic_request_example, name='atomic'),
    path('user-register/', views.register_user, name='register'),
]

'''#urlpatterns += [
    path('transfer-balance-with-error/', views.transfer_balance_with_error, name='transfer_balance_with_error'),
]'''

