from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.IntegerField()


class Genero(models.Model):
    class Meta:
        verbose_name_plural = 'Generos'

    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    telefone = models.IntegerField()
    cpf = models.IntegerField()
    id_livros = models.ManyToManyField('Livro', blank=False)


class Autores(models.Model):
    class Meta:
        verbose_name_plural = 'Autores'
        
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Pedidos(models.Model):
    class Meta:
        verbose_name_plural = 'Pedidos'

    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('EM_PROCESSAMENTO', 'Em Processamento'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]
    data = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Livro(models.Model):
        isbn = models.IntegerField()
        titulo = models.CharField(max_length=150)
        valor = models.FloatField()
        estoque = models.IntegerField()
        descricao = models.CharField(max_length=200)
        editora = models.ForeignKey(Editora, on_delete=models.DO_NOTHING)
        id_genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
        autores = models.ManyToManyField(Autores)

