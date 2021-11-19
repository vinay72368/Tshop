from django.urls import path
from store.views import home,cart,OrderListView,checkout,LoginView,Signup,Signout,add_to_cart
from store.views.cart import add_to_cart
from store.views.contactus import contactus
from store.views import validatePayment, ProductDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',home),
    path('home/', home , name='homepage'),
    path('cart/', cart),
    path('orders/',login_required(OrderListView.as_view(), login_url='/Login/'), name ='orders'),
    path('Login/', LoginView.as_view(), name='login'),
    path('Logout/', Signout),
    path('checkout/', checkout),
    path('Signup/', Signup),
    path('product/<str:slug>',ProductDetailView.as_view()),
    path('addtocart/<str:slug>/<str:size>', add_to_cart),
    path('contactus/',contactus),
    path('validate_payment', validatePayment)

]
