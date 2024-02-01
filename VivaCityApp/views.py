import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render
from .models import BlogPost, Destination, GalleryImage, Testimonio
from .models import agenda as Agenda
from .models import canton, evento, hospedaje, lugar


def index(request):
    destinations = Destination.objects.all()
    gallery_images = GalleryImage.objects.all()
    testimonios = Testimonio.objects.all()
    blog_posts = BlogPost.objects.all()
    return render(request, 'index.html', {"destinations": destinations, "gallery_images": gallery_images, "testimonios": testimonios, "blog_posts": blog_posts})


def login_register(request):
    return render(request, 'login_register.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def eventos_de_usuario(user_id):
    # Obtener la agenda del usuario
    mi_agenda_ids = list(Agenda.objects.filter(
        user=user_id).values_list("evento_id", flat=True))
    mis_eventos = list(evento.objects.filter(id__in=mi_agenda_ids).values())

    for x in mis_eventos:
        x['fecha_inicio'] = x['fecha_inicio'].isoformat()
        x['fecha_fin'] = x['fecha_fin'].isoformat()

    # print([x for x in mis_eventos])

    # Renderizar la vista
    return mis_eventos


def agenda(request):
    # Obtener el usuario logueado
    user = request.user
    # Obtener la agenda del usuario
    mis_eventos = eventos_de_usuario(user)
    # Renderizar la vista
    return render(request, 'eventos.html', {'mi_agenda': mis_eventos})


def rutas(request):
    return render(request, 'rutas.html')


def lugares(request):
    return render(request, 'lugares.html')


def bardisco(request):
    return render(request, 'bardisco.html')


def gastronomia(request):
    return render(request, 'gastronomia.html')


def shopping(request):
    return render(request, 'shopping.html')


def hospedajes(request):
    return render(request, 'hospedaje.html')


def signup(request):
    print('Estoy en el registro')
    if request.method == 'GET':
        return render(request, 'registro.html', {
            "form": UserCreationForm
        })
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                print(request.POST["username"])
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"], email=request.POST["email"])
                user.save()
                login(request, user)
                return redirect('login_register')
            except IntegrityError:
                return render(request, 'registro.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Passwords did not match."})


# Iniciar sesion
def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('dashboard')


def lista_canton(request):
    cantones = canton.objects.all().order_by('nombre_canton')
    return render(request, 'dashboard.html', {'cantones': cantones})


def buscar_eventos(request):
    if request.method == 'GET':
        ciudad_buscada = request.GET.get('buscar')
        try:
            canton_buscado = canton.objects.get(
                nombre_canton__iexact=ciudad_buscada)  # Case-insensitive exact match
            eventos = evento.objects.filter(canton_id=canton_buscado)
            context = {'eventos': eventos}
            return render(request, 'dashboard.html', context)
        except canton.DoesNotExist:
            context = {'error': 'Ciudad no encontrada.'}
            return render(request, 'dashboard.html', context)

    else:
        return render(request, 'dashboard.html')  # Initial rendering


def buscar_hospedajes(request):
    if request.method == 'GET':
        ciudad_buscada = request.GET.get('buscar')

        try:
            canton_buscado = canton.objects.get(
                nombre_canton__iexact=ciudad_buscada)  # Case-insensitive exact match

            hospedajes = hospedaje.objects.filter(canton_id=canton_buscado)
            context = {'hospedajes': hospedajes}
            return render(request, 'hospedaje.html', context)
        except canton.DoesNotExist:
            context = {'error': 'Ciudad no encontrada.'}
            return render(request, 'hospedaje.html', context)

    else:
        return render(request, 'hospedaje.html')  # Initial rendering


def buscar_lugares(request):
    if request.method == 'GET':
        ciudad_buscada = request.GET.get('buscar')

        try:
            canton_buscado = canton.objects.get(
                nombre_canton__iexact=ciudad_buscada)  # Case-insensitive exact match

            lugares = lugar.objects.filter(canton_id=canton_buscado)
            print(lugares)
            context = {'lugares': lugares}
            return render(request, 'lugares.html', context)
        except canton.DoesNotExist:
            context = {'error': 'Ciudad no encontrada.'}
            return render(request, 'lugares.html', context)

    else:
        return render(request, 'lugares.html')  # Initial rendering


def reservar_evento(request):
    mensaje = ""
    error = ""
    if request.method == "POST":
        try:
            # Obtener el usuario logueado
            user_id = request.POST["user"]
            evento_id = request.POST["evento"]
            user = User.objects.get(id=user_id)
            evento_model = evento.objects.get(id=evento_id)

            # Comprobar duplicado
            obj = Agenda.objects.filter(
                user=user, evento_id=evento_model).first()
            if obj != None:
                raise (Agenda.MultipleObjectsReturned)

            # Guardar nuevo
            Agenda(user=user, evento_id=evento_model).save()

            # Renderizar la vista
            mensaje = "Creado correctamente"
        except (Agenda.MultipleObjectsReturned) as e:
            print(e)
            error = "Evento ya reservado"
        except Exception as e:
            print(e)
            error = "Error al reservar el evento"
        finally:
            # Obtener la agenda del usuario
            mis_eventos = eventos_de_usuario(user)
            my_dict = {}
            my_dict['mi_agenda'] = mis_eventos
            if mensaje is not None:
                my_dict["mensaje"] = mensaje
            if error is not None:
                my_dict["error"] = error

            return render(request, 'eventos.html', my_dict)

    else:
        return redirect("agenda")