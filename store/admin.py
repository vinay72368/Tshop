from django.contrib import admin
from store.models import Color, Tshirt,Order,Cart,OrderItem,Payment,SizeVariant, Brand, IdealFor, NeckType, Occassion, Sleeve
from django.utils.html import format_html

# Register your models here.
class SizeVariantConfiguration(admin.TabularInline):
    model = SizeVariant

class OrderItemConfiguration(admin.TabularInline):
    model = OrderItem


class TshirtConfiguration(admin.ModelAdmin):
    inlines = [ SizeVariantConfiguration ]
    list_display=['get_image','name' , 'discount']
    list_editable = ['discount']
    sortably_by = ['name']
    list_filter = ['discount']
    list_display_links = ['name']
    list_per_page = 5

    def get_image(self, obj):
        return format_html(f"""
            <a taregt ='_blank' href='{obj.image.url}'><img height ='50px' src='{obj.image.url}'/></a>
        """)

class CartConfiguration(admin.ModelAdmin):
    model = Cart
    #fields = ('sizeVariant','quantity','user')
    list_display=['quantity' , 'size','tshirt', 'user', 'username']
    fieldsets = (
        ("Cart Info", {"fields": ('user','get_tshirt','get_sizeVariant', 'quantity')}),
    )

    readonly_fields = ('quantity','user', 'get_sizeVariant' , 'get_tshirt')
    
    def get_sizeVariant(self , obj):
        return obj.sizeVariant.size

    def get_tshirt(self,obj):
        tshirt = obj.sizeVariant.tshirt
        tshirt_id = tshirt.id
        name=tshirt.name
        return format_html(f'<a href="/admin/store/tshirt/{tshirt_id}/change/" target="_blank">{name}</a>')
    
    get_tshirt.short_description = 'Tshirt'
    get_sizeVariant.short_description = 'Size'

    def size(self, obj):
        return obj.sizeVariant.size
    
    def tshirt(self,obj):
        return obj.sizeVariant.tshirt.name
    
    def username(self, obj):
        return obj.user.first_name



class OrderConfiguration(admin.ModelAdmin):
    
    list_display=['user' , 'shipping_address', 'phone', 'date','order_status' , 'payment_method']
    readonly_fields = ('user', 
     'phone',
     'shipping_address', 
     'total', 'payment_method', 'payment' , 'payment_request_id','payment_id', 'payment_status' )

    fieldsets = (
        ("Order Information", { "fields": ('order_status', 'shipping_address', 'phone', 'total' ,'user')}),
        ("Payment Information", {"fields": ('payment', 'payment_request_id' , 'payment_id', 'payment_status')})
    )

    inlines = [OrderItemConfiguration]

    def payment_request_id(self, obj):
        return obj.payment_set.all()[0].payment_request_id
   
    def payment_status(self, obj):
        return obj.payment_set.all()[0].payment_status

    def payment_id(self , obj):
        payment_id = obj.payment_set.all()[0].payment_id
        if(payment_id is None or payment_id==''):
            return "Payment ID Not Available"
        else:
            return payment_id
    
    def payment(self, obj):
        payment_id = obj.payment_set.all()[0].id
        return format_html(f'<a href="/admin/store/payment/{payment_id}/change/" target="_blank">Click For Payment Information</a>')

admin.site.register(Tshirt , TshirtConfiguration)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(IdealFor)
admin.site.register(NeckType)
admin.site.register(Occassion)
admin.site.register(Sleeve)
admin.site.register(Cart, CartConfiguration)
admin.site.register(Payment)
admin.site.register(OrderItem)
admin.site.register(Order, OrderConfiguration)


