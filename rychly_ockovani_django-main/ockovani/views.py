from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from ockovani.models import Vakcina, Ockovani, Povolani
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html

    num_ockovani = Ockovani.objects.all().count()
    ockovani = Ockovani.objects.order_by('-id')
    vakciny = Vakcina.objects.order_by('id')

    context = {
        'num_ockovani': num_ockovani,
        'ockovani': ockovani,
        'vakciny': vakciny
    }

    return render(request, 'index.html', context=context)



def seznamvakcin(request):

    vakciny = Vakcina.objects.order_by('id')

    context = {
        'vakciny': vakciny
    }

    return render(request, 'seznam_vakcin.html', context=context)

# def seznam(request):
#     """
#     View function for home page of site.
#     """
#     # Render the HTML template index.html
#     return render(
#         request,
#         'seznam.html',
#     )

class OckovaniListView(ListView):
    model = Ockovani

    context_object_name = 'ockovani_list'   # your own name for the list as a template variable
    template_name = 'ockovany/list.html'  # Specify your own template name/location
    paginate_by = 6

    def get_queryset(self):
        if 'vakcina_nazev_firmy' in self.kwargs:
            return Ockovani.objects.filter(vakcina__nazev_firmy=self.kwargs['vakcina_nazev_firmy']).all() # Get 5 books containing the title war
        else:
            return Ockovani.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_ockovani'] = len(self.get_queryset())
        if 'vakcina_nazev_firmy' in self.kwargs:
            context['view_title'] = f"Vakcíny: {self.kwargs['vakcina_nazev_firmy']}"
            context['view_head'] = f"Vakcíny: {self.kwargs['vakcina_nazev_firmy']}"
        else:
            context['view_title'] = 'Očkovaní'
            context['view_head'] = 'Přehled očkovaných'
        return context


class OckovaniDetailView(DetailView):
    model = Ockovani

    context_object_name = 'osoba_detail'   # your own name for the list as a template variable
    template_name = 'ockovany/detail.html'  # Specify your own template name/location


class OckovaniCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Ockovani
    fields = ['jmeno', 'prijmeni', 'datum_narozeni', 'datum_prvni_ockovani', 'datum_druhe_ockovani', 'kod_ockovaneho', 'kod_pojistovny', 'qr', 'vakcina', 'povolani']
    template_name = 'ockovany/ockovani_form.html'

    permission_required = 'ockovani.add_ockovani'


class OckovaniUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Ockovani
    fields = '__all__'
    template_name = 'ockovany/ockovani_form.html'

    permission_required = 'ockovani.change_ockovani'

class OckovaniDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Ockovani
    success_url = reverse_lazy('index')
    template_name = 'ockovany/ockovani_confirm_delete.html'

    permission_required = 'ockovani.delete_ockovani'
