from django.test import TestCase

# Create your tests here.
from book.models import Voo, Historico, Relacao

class CadastraVooTeste(TestCase):

    @classmethod

    def criaVoo(cls):
        Voo.objects.create (
            id_voo = '1',
            codigoVoo = 'PCS002GRU',
            rota = 'GRU-SSA',
            horarioPartidaProgramado = datetime.datetime(hour = 17; minute = 35).from,
            horarioChegadaProgramado = 19:20,
            companhia = 'PCS'
        )

    def testaVoo(self):
        voo1 = Voo.objects.get(codigoVoo = 'Os Irmãos Karamazov')
        self.assertEqual(livro_1.id, 1)
    def test_update_titulo(self):
        livro_1 = Livro.objects.get(titulo='Os Irmãos Karamazov')
        livro_1.titulo = "Outro nome"
        livro_1.save()
        self.assertEqual(livro_1.titulo, "Outro nome")
class UsuarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(nome="Michelet")

    def test_criacao_id(self):
        usuario_1 = Usuario.objects.get(nome="Michelet")
        self.assertEqual(usuario_1.id, 1)

class EmprestimoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(nome="Michelet")
        Livro.objects.create(titulo='Os Irmãos Karamazov')
        livro_1 = Livro.objects.get(titulo='Os Irmãos Karamazov')
        usuario_1 = Usuario.objects.get(nome="Michelet")
        Emprestimo.objects.create(livro=livro_1, usuario=usuario_1)
    def test_criacao_emprestimo_id(self):
        emprestimo_1 = Emprestimo.objects.get(id=1)
        
        self.assertEqual(emprestimo_1.usuario.id,1)
    
    def test_delete_emprestimo(self):
        Emprestimo.objects.filter(id=1).delete()
        self.assertEqual(Emprestimo.objects.count(),0)