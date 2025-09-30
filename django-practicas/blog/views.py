from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostForm, CommentForm

# Create your views here.

def hola(request):
    return render(request, 'hola.html', {})

class AddPost(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'AddPost.html', context)
    
    def post(self, request, *args, **kwargs):

        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            context = {
                'message': 'Post creado exitosamente'
            }
            return redirect('hola')
        
        context = {
            'form': form
        }
        return render(request, 'AddPost.html', context)

class AddComment(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        context = {
            'form': form
        }
        return render(request, 'AddComment.html', context)
    
    def post(self, request, *args, **kwargs):

        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            context = {
                'message': 'Comentario creado exitosamente'
            }
            return redirect('hola')
        
        context = {
            'form': form
        }
        return render(request, 'AddComment.html', context)