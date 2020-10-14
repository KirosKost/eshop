from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from . models import Post



def blog(request):
    product = Product.objects.all()
    product_list = Product.objects.all()
    cart_product_form = CartAddProductForm()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'cart_product_form': cart_product_form, 
                'producent': product,
                'products': products,   
    }
    return render(request, 'blog/blog.html', context)