from django.urls import path
from .views import ListaSzczegolow, ListaZadan, StworzZadanie,EdytujZadanie,UsunZadanie,Uzytkownik,Zarejestruj
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Uzytkownik.as_view(next_page='zadania'),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('zarejestruj/', Zarejestruj.as_view(),name='zarejestruj'),
    path('', ListaZadan.as_view(),name='zadania'),
    path ('zadanie/<int:pk>/', ListaSzczegolow.as_view(),name='zadanie'),
    path('stworz-zadanie/', StworzZadanie.as_view(),name='stworz-zadanie'),
    path('edytuj-zadanie/<int:pk>/', EdytujZadanie.as_view(),name='edytuj-zadanie'),
    path('usun-zadanie/<int:pk>/', UsunZadanie.as_view(),name='usun-zadanie'),

]