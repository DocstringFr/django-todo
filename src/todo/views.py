from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo.models import ToDo


class TodosListView(ListView):
    model = ToDo
    template_name = "todo/index.html"
    context_object_name = "todos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time"] = datetime.today()
        return context


class CreateTodo(CreateView):
    model = ToDo
    fields = ["title", ]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.title = form.instance.title.capitalize()

        return super().form_valid(form)


class DeleteTodo(DeleteView):
    model = ToDo

    def get_success_url(self):
        return reverse('home')


def update_todo(request, pk):
    todo = ToDo.objects.get(pk=pk)
    todo.done = not todo.done
    todo.save()
    return JsonResponse({"Success": True})


def delete_all(request):
    finished_todos = ToDo.objects.filter(done=True)
    finished_todos.delete()
    return HttpResponseRedirect(reverse("home"))
