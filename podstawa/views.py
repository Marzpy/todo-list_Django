from asyncio import mixins
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Zadanie
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.utils import timezone
# Create your views here.


class Uzytkownik(LoginView):
    template_name='podstawa/login.html'
    fields='__all__'
    redirect_authenticated_user: True
    def pobierz_url(self):
        return reverse_lazy('zadania')
class Zarejestruj(FormView):    
    template_name='podstawa/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user: True
    success_url= reverse_lazy('zadania')
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(Zarejestruj,self).form_valid(form)    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('zadania') 
        return super(Zarejestruj,self).get(*args, **kwargs)       
            
            
class ListaZadan(LoginRequiredMixin,ListView):
    model = Zadanie
    context_object_name= 'zadania'    
    # daje możliwość odczytania tylko przez zweryfikowanego uzytkownika
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['zadania']=context['zadania'].filter(user=self.request.user)
        context['count']=context['zadania'].filter(status=False).count()
        return context
    """def zadania(request):
        zadania = Zadanie.objects.filter(uzytkownik=request.user, status=False).order_by('czas_utworzenia')
        count = zadania.count()
        for zadanie in zadania:
            if zadanie.czas_zakonczenia and zadanie.czas_zakonczenia <= timezone.now():
         
                zadanie.status = True
                zadanie.save()
                return render(request, 'todo/zadania.html', {'zadania': zadania, 'count': count})"""
class ListaSzczegolow(LoginRequiredMixin,DetailView):
    model = Zadanie
    context_object_name = 'zadanie'
    template_name = 'podstawa/zadanie.html'
    
class StworzZadanie(LoginRequiredMixin,CreateView):
    model=Zadanie
    fields=['nazwa','opis','status']
    success_url= reverse_lazy('zadania')
    #sprawdz czy to zostało stworzne przez uzytkownika 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        # Sprawdzenie, czy pole "nazwa" nie jest puste
        if not form.cleaned_data['nazwa']:
            form.add_error('nazwa', 'To pole jest wymagane.')
            return super().form_invalid(form)
        return super().form_valid(form)    
class EdytujZadanie(LoginRequiredMixin,UpdateView):
    model=Zadanie
    fields=['nazwa','opis','status']
    success_url= reverse_lazy('zadania')
    
class UsunZadanie(LoginRequiredMixin,DeleteView):
    model= Zadanie
    fields='__all__'
    success_url= reverse_lazy('zadania')
    template_name = 'podstawa/zadanie_usun.html'



