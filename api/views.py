from rest_framework import viewsets
from .models import Product, Order, Category
from .serializers import ProductSerializer, OrderSerializer, CategorySerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.http import HttpResponse
from .tasks import test_task
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Удаляем кэш после создания нового продукта
        cache.delete('product_list_cache')
        return super().perform_create(serializer)

    @method_decorator(cache_page(60 * 15,key_prefix='product_list_cache'))  # Кэшируем на 15 минут
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)



def run_task(request):
    # Запускаем фоновую задачу
    test_task.delay()

    return HttpResponse("Фоновая задача была запущена!")
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('user', 'product')
    serializer_class = OrderSerializer
