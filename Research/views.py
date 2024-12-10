from django.http import JsonResponse
from .models import Account
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

'''def update_balance(request):
    account = Account.objects.first()
    account.balance += 100
    account.save()  # Automatically committed in autocommit mode.
    return JsonResponse({'status': 'Balance updated'})
'''
def transfer_balance(request):
    try:
        with transaction.atomic():
            # Fetch two accounts
            account1 = Account.objects.get(id=1)
            account2 = Account.objects.get(id=2)

            transfer_amount = 5000
            if account1.balance < transfer_amount:
                raise ValidationError("Insufficient balance for this transfer.")

            # Perform a transfer
            account1.balance -= transfer_amount # Deduct from account1
            account2.balance += 50  # Add to account2

            # Save both accounts
            account1.save()
            account2.save()

        return JsonResponse({'status': 'Transfer successful'})
    
    except ValidationError as e:
        # Handle validation errors explicitly
        return JsonResponse({'status': 'Transfer failed', 'error': str(e)})

    except Exception as e:
        return JsonResponse({'status': 'Transfer failed', 'error': str(e)})
    
'''def transfer_balance_with_error(request):
    try:
        with transaction.atomic():
            account1 = Account.objects.get(id=1)
            account2 = Account.objects.get(id=2)

            transfer_amount = 50

            # Check if account1 has sufficient balance
            if account1.balance < transfer_amount:
                raise ValidationError("Insufficient balance for this transfer.")

            account1.balance -= transfer_amount # Assume this exceeds the balance
            account1.save()

            # This line will not be executed because of the error above
            account2.balance += transfer_amount
            account2.save()

        return JsonResponse({'status': 'Transfer successful'})
    
    except ValidationError as e:
        # Handle validation errors explicitly
        return JsonResponse({'status': 'Transfer failed', 'error': str(e)})

    except Exception as e:
        return JsonResponse({'status': 'Transfer failed', 'error': str(e)})
'''

from django.db import transaction
from django.http import JsonResponse
from .models import Account

def nested_transaction_example(request):
    try:
        with transaction.atomic():
            account1 = Account.objects.get(id=1)
            account2 = Account.objects.get(id=2)

            # Deduct balance from account1
            account1.balance -= 500
            account1.save()

            # Create a savepoint
            savepoint = transaction.savepoint()

            try:
                with transaction.atomic():
                # Attempt to add a large balance to account2 (e.g., causes a validation error)
                    account2.balance += 1000000000000  # Unrealistic amount
                    account2.save()

            except Exception as e:
                # Rollback to the savepoint if something goes wrong
                transaction.savepoint_rollback(savepoint)
                return JsonResponse({'status': 'Partial rollback occurred', 'error': str(e)})

            # Commit changes after the savepoint
            transaction.savepoint_commit(savepoint)

        return JsonResponse({'status': 'Transaction successful'})

    except Exception as e:
        return JsonResponse({'status': 'Transaction failed', 'error': str(e)})


def atomic_request_example(request):
    try:
        account1 = Account.objects.get(id=1)
        account2 = Account.objects.get(id=2)

        # Perform a transfer
        transfer_amount = 500
        if account1.balance < transfer_amount:
            raise ValueError("Insufficient balance.")

        account1.balance -= transfer_amount
        account2.balance += transfer_amount

        account1.save()
        account2.save()

        return JsonResponse({'status': 'Transfer successful'})

    except Exception as e:
        return JsonResponse({'status': 'Transfer failed', 'error': str(e)})
    
def register_user(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            raise ValueError("Username already exists.")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        
        return JsonResponse({'status': 'User registered successfully'})
    except Exception as e:
        return JsonResponse({'status': 'Registration failed', 'error': str(e)})

def transferring_balance(request):
    try:
        with transaction.atomic():
            # Lock the account record for updating
            account = Account.objects.select_for_update().get(id=1)

            transfer_amount = 500
            if account.balance < transfer_amount:
                raise ValueError("Insufficient balance.")

            account.balance -= transfer_amount
            account.save()

            return JsonResponse({'status': 'Transfer successful'})

    except Exception as e:
        return JsonResponse({'status': 'Transfer failed', 'error': str(e)})