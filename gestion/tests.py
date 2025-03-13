from django.test import TestCase
from gestion.models import Productor, Finca, Vivero, Labor, ControlPlagas

class ModelsTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documento="12345678",
            nombre="Juan",
            apellido="Perez",
            telefono="123456789",
            correo="juan@example.com"
        )

        self.finca = Finca.objects.create(
            numero_catastro="A12345",
            municipio="Medellín",
            productor=self.productor  # ✅ Asegurar que self.productor ya existe
        )

        self.vivero = Vivero.objects.create(
            codigo="V001",
            tipo_cultivo="Tomate",
            finca=self.finca
        )

        self.labor = Labor.objects.create(
            fecha="2024-01-01",
            descripcion="Riego de plantas",
            vivero=self.vivero
        )

        self.producto = ControlPlagas.objects.create(
            registro_ICA="ICA1234",
            nombre="Insecticida X",
            frecuencia_aplicacion=15,
            valor=100.0,
            periodo_carencia=10
        )

        self.labor.productos.add(self.producto)

    def test_productor_creation(self):
        self.assertEqual(self.productor.nombre, "Juan")

    def test_finca_association(self):
        self.assertEqual(self.finca.productor, self.productor)

    def test_vivero_association(self):
        self.assertEqual(self.vivero.finca, self.finca)

    def test_labor_association(self):
        self.assertEqual(self.labor.vivero, self.vivero)

    def test_labor_producto_association(self):
        self.assertIn(self.producto, self.labor.productos.all())
