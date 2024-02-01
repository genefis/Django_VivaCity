from django.contrib import admin
from .models import Destination, GalleryImage, Testimonio, BlogPost
from .models import evento
from .models import hospedaje
from .models import lugar
from .models import canton
from .models import agenda

admin.site.register(Destination)
admin.site.register(GalleryImage)
admin.site.register(Testimonio)
admin.site.register(BlogPost)
admin.site.register(evento)#, #eventosAdmin)
admin.site.register(hospedaje)#, #eventosAdmin)
admin.site.register(lugar)#, #eventosAdmin)
admin.site.register(canton)#, #eventosAdmin)
admin.site.register(agenda)#, #eventosAdmin)