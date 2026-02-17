from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Category

def post_view(request):

    if request.method == "POST":
        author = request.POST.get("author")
        body = request.POST.get("body")
        status = request.POST.get("status")
        category_id = request.POST.get("category")

        category = Category.objects.get(id=category_id)

        post = Post.objects.create(
            author=author,
            body=body,
            category=category,
            status=status
        )
        return redirect("post_view")

    posts = Post.objects.filter(status="public")
    categories = Category.objects.all()


    return render(request,"index.html", context={"posts": posts, "categories": categories})



