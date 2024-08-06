from django import template

register = template.Library()

@register.filter(name="remover_caracter")
@register.filter(name="juntar_letras")
def remover_caracter(var, caracter):
    return var.replace(caracter, '')

def juntar_letras(var):
    return var.strip()
    