from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Choice, Question

# Create your views here.
class IndexView(ListView):
    template_name = 'polls_app/polls_index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls_app/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls_app/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls_app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls_app:results', args=(question.id,)))
     
