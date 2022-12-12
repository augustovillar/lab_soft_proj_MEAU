from django.test import TestCase
from datetime import time
from book.models import Voo, Historico

# Create your tests here.

class CRUD_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(
            codigoVoo = 'PCS001_SSA-GRU', #companhia, numero do voo, origem e destino
            origem = 'SSA',
            destino = 'GRU',
            horarioPartidaProgramado = '17:35',
            horarioChegadaProgramado = '19:20',
            companhia = 'PCS'
        )

    def test_criacao_id(self):
        voo_1 = Voo.objects.get(codigoVoo='PCS001_SSA-GRU')
        self.assertEqual(voo_1.id, 1)

    def test_read_voo(self):
        voo_1 = Voo.objects.get(codigoVoo = 'PCS001_SSA-GRU')
        self.assertEqual(voo_1.codigoVoo, 'PCS001_SSA-GRU')
        self.assertEqual(voo_1.origem, 'SSA')
        self.assertEqual(voo_1.destino, 'GRU')
        self.assertEqual(voo_1.horarioPartidaProgramado, time(17,35))
        self.assertEqual(voo_1.horarioChegadaProgramado, time(19,20))
        self.assertEqual(voo_1.companhia, 'PCS')

    def test_update_voo(self):
        voo_1 = Voo.objects.get(codigoVoo='PCS001_SSA-GRU')
        voo_1.horarioChegadaProgramado = '16:20'
        voo_1.save()
        self.assertEqual(voo_1.horarioChegadaProgramado, '16:20')

    def test_delete_voo(self):
        Voo.objects.filter(codigoVoo='PCS001_SSA-GRU').delete()
        self.assertEqual(Voo.objects.count(),0)


class Historico_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(
            codigoVoo = 'PCS001_SSA-GRU', #companhia, numero do voo, origem e destino
            origem = 'SSA',
            destino = 'GRU',
            horarioPartidaProgramado = '17:35',
            horarioChegadaProgramado = '19:20',
            companhia = 'PCS'
        )
        voo_1 = Voo.objects.get(codigoVoo='PCS001_SSA-GRU')

        Historico.objects.create (
            voo = voo_1,
            horarioPartidaReal = '17:39',
            horarioChegadaReal = '19:42',
            data = '2020-02-04',
            status = 'aterrissado'
        )

    def teste_criacao_historico_id(self):
        historico_1 = Historico.objects.get(id = 1)
        self.assertEqual(historico_1.voo.codigoVoo, 'PCS001_SSA-GRU')