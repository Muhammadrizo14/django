from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
	model = News


def index(request):
	news = News.objects.order_by('-id')
	context = {
		'news': news,
		'title': 'Список новостей',
		'subtitle': 'Самые свежые новости'
	}
	return render(request, 'news/index.html', context)




def get_category(request, category_id):
	news = News.objects.filter(category_id=category_id)
	category = Category.objects.get(pk=category_id)
	return render(request, 'news/category.html', {'news': news,  'category': category, 'subtitle': 'Самые свежые новости'})

def view_news(request, news_id):
	# news_item = News.objects.get(pk=news_id)
	news_item = get_object_or_404(News, pk=news_id)
	return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			# news = News.objects.create(**form.cleaned_data)
			news = form.save()
			return redirect(news)
	else:
		form = NewsForm()
	return render(request, 'news/add_news.html', {'form': form, 'title': 'Добавление новости'})