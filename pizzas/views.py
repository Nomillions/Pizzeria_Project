from django.shortcuts import render, redirect
from .forms import PizzaComment
from .models import Pizza, Topping, Comment

# Create your views here.


def index(request):
    """Home Page for Pizzeria"""
    return render(request, "pizzas/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("date_added")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("-date_added")
    comments = pizza.comment_set.order_by("-date_added")
    if request.method != "POST":
        form = PizzaComment()
    else:
        form = PizzaComment(data=request.POST)
        if form.is_valid():
            pizza_comment = form.save(commit=False)
            pizza_comment.pizza = pizza
            pizza_comment.save()
            form.save()
            return redirect("pizzas:pizza", pizza_id=pizza_id)

    context = {
        "pizza": pizza,
        "toppings": toppings,
        "comments": comments,
        "form": form,
    }
    return render(request, "pizzas/pizza.html", context)
