from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question, Choice
from django.contrib.auth.models import User

# Get questions and display them

@login_required()
def index(request):
    # all_post = Paginator(Question.objects.order_by('-pub_date'),3)
    # page = request.GET.get('page')
    # try:
    #     posts = all_post.page(page)
    # except PageNotAnInteger:
    #     posts = all_post.page(1)
    # except EmptyPage:
    #     posts = all_post.page(all_post.num_pages)
    # context = {'latest_question_list': posts}
    # return render(request, 'polls/index.html', context)
    caty_list = Question.objects.all()
    context = {'latest_question_list': caty_list} 
    return render(request, 'polls/index.html', context)

# Show specific question and choices

# @login_required()
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

# # Get question and display results

# @login_required()
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# # Vote for a question choice

@login_required()
def vote(request):
    caty = get_list_or_404(Question)
    for cat in caty:
        #import pdb; pdb.set_trace()
        try:
            selected_choice = cat.choice_set.get(pk=request.POST[cat.question_text])
        except:
            return HttpResponse("not all votes selected")
        else:
              
        #selected_choice = cat.choice_set.get(pk=request.POST[cat.question_text])
            selected_choice.votes += 1
            current_user = request.user
            selected_choice.owner = current_user.id
            selected_choice.save()

            # current_vote = get_object_or_404(Vote)  
            # current_vote.usr_id = current_user.id
            # current_vote.quest_id = cat.question_id
            # current_vote.cho_id = selected_choice.choice_id  
            # current_vote.save()  
    # # print(request.POST['choice'])
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #return HttpResponseRedirect('polls:index')
    #import pdb; pdb.set_trace()    
    return HttpResponse("Thanks for the response.")
