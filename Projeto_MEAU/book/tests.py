from django.test import TestCase

from book.models import Voo, Historico

class CRUD_voo_teste(TestCase):

    @classmethod

    def create_voo(cls):
        Voo.objects.create (
            codigoVoo = 'PCS002GRU',
            rota = 'GRU-SSA',
            horarioPartidaProgramado = '17:35',
            horarioChegadaProgramado = '19:20',
            companhia = 'PCS'
        )

    def read_voo(self):
        voo1 = Voo.objects.get(codigoVoo = 'PCS002GRU')
        self.assertEqual(voo1.codigoVoo, 'PCS002GRU')
        self.assertEqual(voo1.rota, 'GRU-SSA')
        self.assertEqual(voo1.horarioPartidaProgramado, '17:35')
        self.assertEqual(voo1.horarioChegadaProgramado, '19:20')
        self.assertEqual(voo1.companhia, 'PCS')

    def update_voo(self):
        voo1 = Voo.objects.get(codigoVoo = 'PCS002GRU')
        voo1.horarioChegadaProgramado = '16:20'
        voo1.save()
        self.assertEqual(voo1.horarioChegadaProgramado, '16:20')

    def delete_voo(self):
        Voo.objects.filter(codigoVoo = 'PCS002GRU').delete()
        self.assertEqual(Voo.objects.count(),0)

class Historico_test(TestCase):

    @classmethod

    def create_historico(cls):
        Voo.objects.create (
            codigoVoo = 'PCS002GRU',
            rota = 'GRU-SSA',
            horarioPartidaProgramado = '17:35',
            horarioChegadaProgramado = '19:20',
            companhia = 'PCS'
        )
        voo1 = Voo.objects.get(codigoVoo = 'PCS002GRU')
        Historico.objects.create (
            chaveVoo = voo1,
            id_historico = 1,
            horarioPartidaReal = '17:39',
            horarioChegadaReal = '19:42',
            data = '04/02/2020',
            estado = 'embarcando'
        )

    def teste_historico(self):
        historico1 = Historico.objects.get(id_historico = 1)
        self.assertEqual(historico1.chaveVoo.codigoVoo, 'PCS002GRU')