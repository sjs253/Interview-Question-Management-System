from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Question, Answer
# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    # ctx = {
    #     "user": request.user,
    #     "answers": Answer.objects.all()
    # }
    # for ans in ctx['answers']:
    #     ans.answer.replace('\n', '<br />')

    ctx = {}

    if request.POST:
        
        # ctx = {
        #         'questions': Question.objects.filter(graphs=True)
        # }

        
        if request.POST.get('dropdown')  == 'graphs':
            ctx = {
                'questions': Question.objects.filter(graphs=True),
                'answers': Answer.objects.all()
            }

        if request.POST.get('dropdown')  == 'trees':
            ctx = {
                'questions': Question.objects.filter(trees=True),
                'answers': Answer.objects.all()
            }

        if request.POST.get('dropdown')  == 'greedy':
            ctx = {
                'questions': Question.objects.filter(greedy=True),
                'answers': Answer.objects.all()
            }

        if request.POST.get('dropdown')  == 'arrays':
            ctx = {
                'questions': Question.objects.filter(arrays=True),
                'answers': Answer.objects.all()
            }

        if request.POST.get('dropdown')  == 'strings':
            ctx = {
                'questions': Question.objects.filter(strings=True),
                'answers': Answer.objects.all()
            }           
        
        if request.POST.get('dropdown')  == 'dp':
            ctx = {
                'questions': Question.objects.filter(Dp=True),
                'answers': Answer.objects.all()
            }

    else :
        ctx = {
            'questions': Question.objects.all(),
            'answers': Answer.objects.all()
        }

    
    return render(request, 'feed.html', ctx)

def question(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    if request.POST:
        que = Question()
        que.question = request.POST['question']
        que.author = request.user

        if request.POST.get('graphs', False) == 'on':
            que.graphs = True
        else:
            que.graphs = False

        if request.POST.get('trees', False) == 'on':
            que.trees = True
        else:
            que.trees = False

        if request.POST.get('arrays', False) == 'on':
            que.arrays = True
        else:
            que.arrays = False
    
        if request.POST.get('strings', False) == 'on':
            que.strings = True
        else:
            que.strings = False

        if request.POST.get('greedy', False) == 'on':
            que.greedy = True
        else:
            que.greedy = False

        if request.POST.get('Dp', False) == 'on':
            que.Dp = True
        else:
            que.Dp = False

        que.save()
        print("Question added to database")

    
    ctx = {
        'questions': Question.objects.filter(author=request.user)
    }
    return render(request, 'question.html', ctx)


def answer(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    # if request.POST:
    #     ans = Answer()
    #     ans.answer = request.POST['answer']
    #     ans.author = request.user
    #     ans.question = pk 
    #     ans.save()
    #     print("Answer added to database")

    ctx = {
         'questions': Question.objects.all()
     }

    return render(request, 'answer.html', ctx)

def delete_question(request,pk):
    que=Question()
    Question.objects.filter(_id=pk).delete()
    ctx = {
         'questions': Question.objects.filter(author=request.user).order_by('-_id')
     }
    return render(request, 'question.html', ctx)

def add_answer(request,pk):
    if request.POST:
        ans = Answer()
        ans.answer = request.POST['answer']
        print(ans.answer)
        
        ans.author = request.user
        ans.question_id = pk 
        ans.save()
        print("Answer added to database")

    ctx = {
         'questions': Question.objects.all()
     }

    return render(request, 'answer.html', ctx)