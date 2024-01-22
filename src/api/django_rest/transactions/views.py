from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

# Create your views here.
@csrf_exempt
def transaction_list(request):
    """
    List all code snippets, or create a new transaction.
    """
    if request.method == 'GET':
        return JsonResponse("BB", safe=False)
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def unclassified_transaction_daily(request):
    """
    List all code snippets, or create a new transaction.
    """
    if request.method == 'GET':
        return JsonResponse("BB", safe=False)
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(serializer.data, safe=False)