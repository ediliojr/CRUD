class Agenda(object):
    codigo = None
    titulo = None
    horario = None
    data = None
    
    def __init__(self, codigo=None, titulo=None, horario=None, data=None):
        self.codigo = codigo
        self.titulo = titulo
        self.horario = horario
        self.data = data
        
        
lista_agendamento  =[
    Agenda(1, "Dentista", "13:11", "12/05/2022"),
    Agenda(2, "Entrega de Notas Escolares", "8:30", "28/05/2022"),
    Agenda(3, "Aniversario de Ana", "19:30", "15/07/2022"),
    Agenda(4, "Reunião", "15:30", "21/06/2022"),
]


def delete(codigo):
    # TODO: Fazer a iplementação de delete, recebendo o codigo do objeto
    # procurando na lista, e deletar o objeto da lista
    for i in lista_agendamento:
        if codigo == i.codigo:
            lista_agendamento.remove(i)