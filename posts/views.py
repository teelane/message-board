from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView): # GET Method
    """
    PostListView is going to retrieve all of the objects from the Post table in the database
    """

    # template_name attribute is going to render an specific html file
    template_name = "posts/list.html"
    # model is foing to be from which table we want to retrieve the data
    model = Post
    # context_object_name allows us to modify the name on how we call it in the htmls
    context_object_name = "posts"


class PostDetailView(DetailView): # GET Method
    """
    PostDetailView is going to retrieve a single element from the Post table in the db.
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView): # POST Method
    """
    PostCreateView is going to allow us to create a new post an add it to the db
    """

    template_name = "posts/new.html"
    model = Post
    # fields attribute allw us to control which elements to display on the form to create a new object
    # the name of the fiels have to match with the attributes of the model.
    fields = ["title", "subtitle","body"]
    
class PostUpdateView(UpdateView):  # POST Method
    """
    PostUpdateView allows us to update an existing post from the db
    """
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle","body"]

class PostDeleteView(DeleteView): # DELETE Method
    """
    PostDeleteView allows us to delete an existing post from the db
    """

    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")