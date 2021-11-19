from store.models import Order
from django.views.generic.list import ListView




     
class OrderListView(ListView):
    template_name = 'store/orders.html'
    model = Order
    context_object_name = 'orders'
    paginate_by = 5
    def get_queryset(self):
        return Order.objects.filter(user = self.request.user).order_by('-date').exclude(order_status='PENDING')
