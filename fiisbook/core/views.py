from django.shortcuts import render,redirect
from cursos.models import Curso,Interfaz
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cursos.forms import InterfazForm
from django.urls import reverse_lazy
from users.forms import UserRegisterForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout


# Create your views here.

def register(request):
    form = UserRegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            return redirect('cursos')

    return render(request,'users/register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))

            return redirect('cursos')
        else:
            messages.error(request,'Usuario o Contraseña incorrecto')

    return render(request,'users/login.html',{})

def logout_view(request):
    logout(request)
    messages.success(request,'Sesion cerrada exitosamente')
    return redirect('login')

def course(request):
    cursos = Curso.objects.all()
    return render(request,'cursos.html',{'cursos':cursos})

def course_detail(request,pk):
    cursos = Curso.objects.all()
    object_ = get_object_or_404(Curso,pk=pk)
    return render(request,'curso_detail.html',
    {'object':object_,'cursos':cursos}
    )


class CreateViewInterfaz(CreateView):
    model = Interfaz
    template_name = 'interfaz.html'
    form_class = InterfazForm
    success_url = reverse_lazy('cursos')

    def get_success_url(self):
        return reverse_lazy(
            'curso-detail',
            kwargs={
                'pk': self.object.curso.pk
            }
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curso = get_object_or_404(Curso, pk=self.kwargs['pk'])
        context['form'].initial.update({'curso': curso})
        return context


def interface(request):
    return render(request,'interfaz.html',{})


def model_form_upload(request):
    if request.method == 'POST':
        form = InterfazForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InterfazForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })