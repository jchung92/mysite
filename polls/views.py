from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
<<<<<<< HEAD
from django.utils import timezone
=======
>>>>>>> a09eaf31e0dadc3ab34ee4dcab7ae94320b8033c

from polls.models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
<<<<<<< HEAD
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
=======
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
>>>>>>> a09eaf31e0dadc3ab34ee4dcab7ae94320b8033c


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
<<<<<<< HEAD
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
=======
>>>>>>> a09eaf31e0dadc3ab34ee4dcab7ae94320b8033c


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
	
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

	