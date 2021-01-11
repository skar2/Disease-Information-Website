from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.index,name="home"),
    path('',views.index,name="home"),
    path('welcome',views.welcome,name="welcome"),
    path('contact',views.contact,name="Contact us"),
    path('about',views.about,name="About us"),
    path('submitcontact',views.submitcontact,name='submitted'),
    path('disease',views.disease,name="disease"),
    path('search',views.search,name="search"),
    path('home1',views.home1,name="home1"),
    path('whatisdisease',views.whatisdisease,name="whatisdisease"),
    path('login',views.loginPage,name="login"),
    path('register',views.registerPage,name="register"),
    path('logout',views.logoutUser,name="logout"),
    path('addnews',views.addnews,name='addnews'),
    path('adddisease',views.adddisease,name='adddisease')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
