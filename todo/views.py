
from django.shortcuts import render, redirect
from .models import Todo

def list_view(request):

    if request.method == "POST":
        body = request.POST.get("body")
        duration = request.POST.get("duration")
        duration_type = request.POST.get("duration_type")
        status = request.POST.get("status")

        Todo.objects.create(
            body=body,
            duration=duration,
            duration_type=duration_type,
            status=status
        )

        return redirect("list_view")

    posts = Todo.objects.all()

    return render(request, "todo.html", {"todo": posts})
