from store.models import Occassion,Brand,Color,IdealFor,NeckType,Sleeve ,Tshirt
from django.core.paginator import  Paginator
from django.shortcuts import render
from urllib.parse import urlencode
def home(request):
    query = request.GET
    tshirts = []
    tshirts = Tshirt.objects.all()

    
    brand = query.get('brand')
    neckType = query.get('necktype')
    color = query.get('color')
    occassion = query.get('occassion')
    idealfor = query.get('idealfor')
    sleeve = query.get('sleeve')
    page = query.get('page')

    if(page is None or page == ''):
        page = 1


    if brand !='' and brand is not None:
        tshirts = tshirts.filter(brand__slug = brand)
    
    if neckType!='' and neckType is not None:
        tshirts = tshirts.filter(necktype__slug = neckType)
    
    if color!='' and color is not None:
        tshirts = tshirts.filter(color__slug = color)

    if occassion !='' and occassion is not None:
        tshirts = tshirts.filter(occassion__slug = occassion)

    if idealfor !='' and idealfor is not None:
        tshirts = tshirts.filter(idealfor__slug = idealfor)
    
    if sleeve!='' and sleeve is not None:
        tshirts = tshirts.filter(sleeve__slug = sleeve)


    

    occassions = Occassion.objects.all()
    brands = Brand.objects.all()
    sleeves = Sleeve.objects.all()
    idealFor = IdealFor.objects.all()
    neckTypes = NeckType.objects.all()
    colors = Color.objects.all()


    paginator = Paginator(tshirts, 3)
    page_object = paginator.get_page(page)

    query = request.GET.copy()
    query['page'] = ''
    pageurl = urlencode(query)
    
    
    context ={
        "page_obj": page_object,
        "occassions":occassions,
        "brands":brands,
        "colors": colors,
        "sleeves":sleeves,
        "neckTypes":neckTypes,
        "idealFor":idealFor,
        "pageurl":pageurl
    }
    return render(request , template_name='store/home.html', context = context)
