from django.views import View
from django.http import HttpResponse


class HelloView(View):
    def get(self, request, *args, **kwargs):
        todo_list = [
            'Hello',
        ]
        return HttpResponse(
            f"<ul><li>{todo_list[0]} </li></ul>'")
