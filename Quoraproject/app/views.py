from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Question, Answer, Like
from .forms import AnswerForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')


# Home page to show all the details on a screen
def home(request):
    questions = Question.objects.all()

    if request.method == "POST":
        if "submitanswer" in request.POST:
            content = request.POST['content']
            question_id = request.POST['question_id']
            question = get_object_or_404(Question, pk=question_id)
            
            # Create the answer and associate it with the question
            answer = Answer(answer_text=content, question=question, created_by=request.user)
            answer.save()
        if "submitquestion" in request.POST:
            model = Question()
            model.title = request.POST.get("title")
            model.description = request.POST.get("description")
            model.created_by = request.user
            model.save()


    return render(request, 'home.html', {'questions': questions})

# Show question answer details
def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(question=question)
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.created_by = request.user
            answer.save()
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    
    return render(request, 'question_detail.html', {'question': question, 'answers': answers, 'form': form})

def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    existing_like = Like.objects.filter(answer=answer, user=request.user).first()
    if not existing_like:
        Like.objects.create(answer=answer, user=request.user)
    return JsonResponse({
        'success': True,
        'new_like_count': answer.likes.count(),
    })