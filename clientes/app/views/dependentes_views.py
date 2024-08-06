from django.views.generic import CreateView

from app.forms.dependentes_form import DependenteForm
from app.models import Dependente

class DependenteCreateView(CreateView):
    model = Dependente
    form_class = DependenteForm
    template_name = "dependentes/form_dependente.html"
    success_url = "lista_dependentes"