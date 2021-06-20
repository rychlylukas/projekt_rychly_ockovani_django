from ockovani.models import Vakcina

def vakciny(request):
    return {'vakciny': Vakcina.objects.all()}