"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from student.views import getList, getRow, add, edit, remove

urlpatterns = [
    path('admin/', admin.site.urls),

    #將路徑http://[Domain]/student/getList指向給views.py中的getList
    path('student/getList/', getList),
    #將路徑http://[Domain]/student/getRow指向給views.py中的getRow，<int:pk>指的是將get的值給pk這個變數，變數型態為int
    path('student/getRow/<int:pk>/', getRow),
    #將路徑http://[Domain]/student/add指向給views.py中的add
    path('student/add/', add),
    #將路徑http://[Domain]/student/edit指向給views.py中的edit，<int:pk>指的是將get的值給pk這個變數，變數型態為int
    path('student/edit/<int:pk>', edit),
    #將路徑http://[Domain]/student/remove指向給views.py中的remove，<int:pk>指的是將get的值給pk這個變數，變數型態為int
    path('student/remove/<int:pk>', remove),
]
