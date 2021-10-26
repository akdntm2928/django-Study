from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choise, Question

# from mysite.polls.models import Question,Choise


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'
# def index(request):
#     # latest_question_list: 출판일자을 내림차순으로 정렬하여 5개까지만 나오도록 함
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#     # output =','.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)


# def detail(request, question_id):
#     question =get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':question})
    
# def results(request,question_id):
#     question =get_object_or_404(Question,pk=question_id)
#     return render(request,"polls/result.html",{"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choise = question.choise_set.get(pk=request.POST['choise'])
    except (KeyError, choise.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choise.",
        })
    else:
        selected_choise.votes += 1
        selected_choise.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

