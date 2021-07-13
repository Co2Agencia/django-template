from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic import View
from django.template.loader import get_template
# Static Files ROOT Path
from django.contrib.staticfiles.storage import staticfiles_storage
# Para filtros de busqueda
from django.db.models import Q
# Para Usuarios
from django.contrib.auth import authenticate, login, logout
# Archivos temporales
import tempfile
# Para archivos .csv
import io
# Para Ajax y Json
import json
from django.core import serializers

# Configuracion para Fecha Local
from django.utils import timezone
from django.utils.translation import activate, get_language
import locale
activate("es-ar")
get_language()
locale.setlocale(locale.LC_ALL,("es_AR.utf-8"))



# Create your views here.
