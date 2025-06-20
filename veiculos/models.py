from django.db import models

class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quilometragem = models.PositiveIntegerField()
    cor = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='fotos/')
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano})'
