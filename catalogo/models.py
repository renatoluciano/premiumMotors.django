from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Marca")

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    ESTADO_CHOICES = [
        ('NOVO', 'Novo (Zero Km)'),
        ('SEMI', 'Seminovo'),
        ('USADO', 'Usado'),
    ]

    PORTAS_CHOICES = [
        (2, '2 Portas'),
        (4, '4 Portas'),
    ]

    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='veiculos', verbose_name="Marca")
    modelo = models.CharField(max_length=150, verbose_name="Modelo")
    versao = models.CharField(max_length=150, help_text="Ex: 1.0 Turbo Flex Automático", verbose_name="Versão")
    ano_fabricacao = models.PositiveIntegerField(verbose_name="Ano de Fabricação")
    ano_modelo = models.PositiveIntegerField(verbose_name="Ano do Modelo")
    preco = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Preço (R$)")
    quilometragem = models.PositiveIntegerField(default=0, verbose_name="Quilometragem (Km)")
    cor = models.CharField(max_length=50, verbose_name="Cor")
    portas = models.IntegerField(choices=PORTAS_CHOICES, default=4, verbose_name="Quantidade de Portas")
    estado = models.CharField(max_length=5, choices=ESTADO_CHOICES, default='USADO', verbose_name="Estado de Conservação")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição/Opcionais")
    imagem_principal = models.ImageField(upload_to='carros/', blank=True, null=True, verbose_name="Foto Principal")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrado em")

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.marca.nome} {self.modelo} ({self.ano_modelo}) - {self.get_estado_display()}"
