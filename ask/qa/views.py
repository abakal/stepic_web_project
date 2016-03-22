from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.http import require_GET,require_POST

from .models.import Question,Answer

def test(request, *args, **kwargs):
	return HttpResponse('OK')

# Create your views here.

def home_page(request):
	questions=Question.objects.order_by('-id')
	paginator=Paginator(questions,10)
	page=request.GET.get('page')
	try:
		queryset=paginator.page(page)
	except PageNotAnInteger:
		queryset=paginator.page(1)
	except EmptyPage:
		queryset=paginator.page(paginator.num_pages)
	
	context={
	    'questions':    queryset,
	}
	return render(request,'index.html',context)

def question_details(request, id):
	question=get_object_or_404(Question, id=int(id))
	
	if request.method=='POST':
		form=AnswerForm(request.POST,_question=question)
		form._user=request.user
		if form.is_valid():
			answer=form.save()
			answer._user=request.user
			return HttpResponseRedirect('/question/{}'.format(question.id))
	else:
		form=AnswerForm(initial={'question' : question.id})
	return render(request,'question.html',{'question':question,
	    'form':   form,
	    'answers':  question.answer_set.all(),})

def popular_questions(request):
	sorted_questions=Questions.objects.order_by('-rating')
	paginator=Paginator(sorted_questions,10)
	page=request.GET.get('page')
	try:
		queryset=paginator.page(page)
	except PageNotAnInteger:
		queryset=paginator.page(1)
	except EmptyPage:
		queryset=paginator.page(paginator.num_pages)
	
	context={
	    'sorted_questions':    queryset,
	}
	return render(request,'popular.html',context)
