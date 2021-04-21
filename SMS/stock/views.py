from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from .models import Brand,Category,Product,Order
from .decorators import admin_required,manager_required
from .forms import OrderCreateForm,OrderFilter
import pytz

@method_decorator(admin_required,name='dispatch')
class BrandCreateView(CreateView,LoginRequiredMixin):
    model = Brand
    template_name = "stock/createBrand.html"
    fields = '__all__'


class BrandListView(ListView):
    model = Brand
    template_name = "stock/listBrand.html"

@method_decorator(admin_required,name='dispatch')
class BrandDeleteView(DeleteView,LoginRequiredMixin):
    model = Brand
    template_name = "stock/deleteBrand.html"
    success_url = reverse_lazy('stock:list_brand')

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Stock Brand Deleted')
        return super().delete(*args,**kwargs)

@method_decorator(admin_required,name='dispatch')
class BrandUpdateView(UpdateView,LoginRequiredMixin):
    model = Brand
    fields = ['Brandstatus']
    success_url = reverse_lazy('stock:list_brand')

@method_decorator(admin_required,name='dispatch')
class CategoryCreateView(CreateView,LoginRequiredMixin):
    model = Category
    template_name = "stock/createCategory.html"
    fields = '__all__'


class CategoryListView(ListView):
    model = Category
    template_name = "stock/listCategory.html"

@method_decorator(admin_required,name='dispatch')
class CategoryDeleteView(DeleteView,LoginRequiredMixin):
    model = Category
    template_name = "stock/deleteCategory.html"
    success_url = reverse_lazy('stock:list_category')

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Stock Category Deleted')
        return super().delete(*args,**kwargs)

@method_decorator(admin_required,name='dispatch')
class CategoryUpdateView(UpdateView,LoginRequiredMixin):
    model = Category
    fields = ['Categorystatus']
    success_url = reverse_lazy('stock:list_category')

@method_decorator(admin_required,name='dispatch')
class ProductCreateView(CreateView,LoginRequiredMixin):
    model = Product
    template_name = "stock/createProduct.html"
    fields = '__all__'

class ProductListView(ListView):
    model = Product
    template_name = "stock/listProduct.html"

@method_decorator(admin_required,name='dispatch')
class ProductDeleteView(DeleteView,LoginRequiredMixin):
    model = Product
    template_name = "stock/deleteProduct.html"
    success_url = reverse_lazy('stock:list_product')

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Stock Product Deleted')
        return super().delete(*args,**kwargs)

@method_decorator(admin_required,name='dispatch')
class ProductUpdateView(UpdateView,LoginRequiredMixin):
    model = Product
    fields = ['Productstatus']
    success_url = reverse_lazy('stock:list_product')


@method_decorator(manager_required,name='dispatch')
class OrderCreateView(CreateView,LoginRequiredMixin):
    # model = Order
    form_class = OrderCreateForm
    template_name = "stock/createOrder.html"
    # fields = ['OrderedProduct','OrderedQuantity','OrderedCustomer']



class OrderListView(ListView):
    model = Order
    template_name = "stock/listOrder.html"



class OrderDetailView(DetailView):
    model = Order
    template_name = "stock/detailOrder.html"



@login_required
def OrderFilterView(request):
    if request.method == 'POST':
        form = OrderFilter(request.POST)
        if form.is_valid():
            sdate = form.cleaned_data['StartingDate']
            edate = form.cleaned_data['EndingDate']
            orders = Order.objects.filter(OrderedDate__lt=edate).filter(OrderedDate__gt=sdate) 
            return render(request,'stock/listCorder.html',{'form':form,'order_list':orders})
    else:
        form = OrderFilter()
    return render(request,'stock/listCorder.html',{'form':form})

