from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from polls.models import Poll,Choice

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(template.render(context))
def detail(request, poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/detail.html',{'poll':poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	p=get_object_or_404(Poll,pk=poll_id)
	try:
		s=p.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'poll':p,'error_message':"you didn't select choice.",})
	else:
		s.votes+=1
		s.save()
		return HttpResponseRedirect(reverse('polls:results',args={p.id,}))

# Create your views here.
