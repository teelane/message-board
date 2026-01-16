from django.views.generic import (
    ListView,
    DetailView
)
from .models import Post

class PostListView(ListView):
    """
    PostListView is going to retrieve all of the objects
    """

    #template_name attribute is going to render a specifc html file
    template_name = "posts/list.html"
    #model is going to be from which table we want to retrieve the data
    model = Post
    #context_object_name allow us to modify the name on how we call it in the htmls
    context_object_name = "posts"