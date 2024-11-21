from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from trees.models import Tree
from trees.forms import TreeForm

# Create your views here.
def create_tree(request):
    if request.method == "POST":
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tree_list')
    else:
        form = TreeForm()
        return render(request,'treeform.html',{'form':form})

def update_tree(request,t_id):
    l = Tree.objects.get(pk=t_id)
    if request.method == "POST":
        form = TreeForm(request.POST, request.FILES, instance=l)
        if form.is_valid():
            form.save()
            return redirect('tree_list')
    else:
        form = TreeForm(instance=l)
        return render(request,'treeform.html',{'form':form})

def delete_tree(request,t_id):
    Tree.objects.get(pk=t_id).delete()
    return redirect('tree_list')



def tree_list(request):
    trees = Tree.objects.all()
    return render(request, 'tree.html', {'trees': trees})


def photo_list(request):
    photos = Tree.objects.all()
    return render(request, 'photo_list.html', {'photos': photos})

def photo_upload(request):
    if request.method == 'POST':
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = TreeForm()
    return render(request, 'photo_upload.html', {'form': form})


def add_to_cart(request, t_id):
    if request.method == "POST":
        tree = get_object_or_404(Tree, pk=t_id)
        # Add your logic for cart (e.g., save to session, or Cart model)
        # Example:
        cart = request.session.get('cart', [])
        cart.append(tree.id)  # Save the tree's ID to the session
        request.session['cart'] = cart
        return redirect('tree_list')
    return redirect('tree_list')