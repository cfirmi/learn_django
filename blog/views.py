from django.shortcuts import render


posts = [
    {
        'author': 'Christian',
        'title': 'Blog Post One',
        'content': "hey what is u this this t lorem content but more scrambled",
        'date_posted': 'May 13 2020'
    },
    {
        'author': 'Michelle',
        'title': 'Blog Post two',
        'content': "hey what is u this this t lorem content but more scrambled",
        'date_posted': 'May 14 2020'
    }
]


def home(request):
  context = {
    'posts': posts,
    'title': "Christians Awesome page"
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')
