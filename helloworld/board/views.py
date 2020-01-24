from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Board, Post, Topic
from .forms import NewTopicForm

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
# Create your views here.

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        user = User.objects.first()
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit = False)
            topic.board = board
            topic.starter = user
            topic.save()       

            post = Post.objects.create(
                topic = topic,
                created_by = user,
                message = form.cleaned_data.get('message')
            )
            return redirect('board_topics', pk = board.pk)
    else:
        form = NewTopicForm()        

    return render(request, 'new_topic.html', {'board': board, 'form': form})
