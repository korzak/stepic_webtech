from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from qa.models import Question
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

@require_GET
def main_list(request, *args, **kwargs):
  questions = Question.objects.all().order_by('-added_at')
  try:
    page = int(request.GET.get('page', 1))
  except ValueError:
    raise Http404
  limit = request.GET.get('limit', 10)
  paginator = Paginator(questions, limit)
  paginator.baseurl = '/?page='
  try:
    page = paginator.page(page)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)
  return render(request, 'main_list.html', {
    'questions': page.object_list,
    'paginator': paginator,
    'page': page,
  })

@require_GET
def popular_list(request, *args, **kwargs):
  questions = Question.objects.all().order_by('-rating')
  try:
    page = int(request.GET.get('page', 1))
  except ValueError:
    raise Http404
  limit = request.GET.get('limit', 10)
  paginator = Paginator(questions, limit)
  paginator.baseurl = '/popular/?page='
  try:
    page = paginator.page(page)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)
  return render(request, 'popular_list.html', {
    'questions': page.object_list,
    'paginator': paginator,
    'page': page,
    'path': request.path,
  }) 
 
@require_GET
def question_details(request, id):
  try:
    # question = get_object_or_404(Question, id=id)
    question = Question.objects.get(id=id)
  except Question.DoesNotExist:
    raise Http404
  return render(request, 'question.html', {
    'question': question,
  })