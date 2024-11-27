from django.views.generic import ListView
from django.shortcuts import render
from WHS.models import *
from CONF.models import *
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def stock_in_all(request):
    # all_stock = 
    all_stock = Stock_In.objects.all().select_related()
    return render(request, 'stock_in_all.html', {'all_stock': all_stock})

@login_required
def stock_in_detail(request, id):
    # Retrieve a specific record by ID
    stock = get_object_or_404(Stock_In, id=id)
    context={'stock':stock,}
    return render(request, 'stock_in_detail.html' , context)


@login_required
def stock_out_all(request):
    # all_stock = 
    all_stock = Stock_Out.objects.all().select_related()
    return render(request, 'stock_out_all.html', {'all_stock': all_stock})

@login_required
def stock_out_detail(request, id):
    # Retrieve a specific record by ID
    stock = get_object_or_404(Stock_Out, id=id)
    context={'stock':stock,}
    return render(request, 'stock_out_detail.html' , context)

@login_required
def whs_all(request):
    # all_stock = 
    all_whs = WHSBranch.objects.all().select_related()
    return render(request, 'whs_all.html', {'all_whs': all_whs})

@login_required
def whs_detail(request, id):
    # Retrieve a specific record by ID
    whs = get_object_or_404(WHSBranch, id=id)
    whs_in_detail = Stock_IN_Detail.objects.filter(location=whs).distinct('item')
    whs_out_detail = Stock_Out_Detail.objects.filter(location=whs).distinct('item')
    context = {
        'whs': whs,
        'whs_in_detail':whs_in_detail,
        'whs_out_detail':whs_out_detail,
    }
    return render(request, 'whs_detail.html', context)


        # 'stock_in_details': stock_in_details,
        # 'stock_out_details': stock_out_details
    # stock_in_details = Stock_IN_Detail.objects.filter(location=whs)
    # stock_out_details = Stock_Out_Detail.objects.filter(location=whs)