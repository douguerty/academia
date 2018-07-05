from core.models import MyUser

def GetUsuario(id):
    usuario = MyUser.objects.filter(pk=id)
    if usuario:
        return usuario
    else:
        return False