from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    ''' a view that renders the bag content'''
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_name):
    """ Add a product/service to bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_name in list(bag.keys()):
        bag[item_name]
    else:
        bag[item_name] = item_name

    request.session['bag'] = bag
    return redirect(redirect_url)