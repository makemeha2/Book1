"""firstProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstProj import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('polls/', include('polls.urls')),
    path('books/', include('books.urls')),
    
    # path('polls/', views.index, name='index'),                                # /polls/
    # path('polls/<int:question_id>/', views.detail, name='detail'),            # /polls/5/
    # path('polls/<int:question_id>/results/', views.results, name='results'),  # /polls/5/results/
    # path('polls/<int:question_id>/vote/', views.vote, name='vote'),           # /polls/5/vote/
]
