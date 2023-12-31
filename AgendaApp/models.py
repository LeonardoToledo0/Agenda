from django.db import models



UFS = [
        ('SP','São Paulo'),
        ('MG','Minas Gerais'),
        ('RJ','Rio de Janeiro'),
        ('ES',"Espirito Santo")]


# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=UFS)


    def __str__(self):
        return self.nome

class Interesse(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome




class Contato(models.Model):

# opções de campo estado civil, o primeiro da tupla vai no banco
    ESTADO_CIVIS = [
        ('S','Solteiro'),
        ('C','Casado'),
        ('D','Divorciado'),
        ('V','Viúvo')]
    
    
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(verbose_name= "Data de Nascimento")
    endereco = models.CharField(max_length=200,verbose_name='Endereço')
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50,blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=UFS)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIS, null=True)
    interesse = models.ManyToManyField(Interesse)


    def __str__(self):
        return self.nome
    
# configurar este modelo acima
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Telefone(models.Model):
    TIPOS_TELEFONE = [
        ('RES','Residencial'),
        ('COM','Comercial'),
        ('REC', 'Recado'),
        ('CEL','Celular')
    ]
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    ddd = models.IntegerField( verbose_name='DDD')
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=3, choices= TIPOS_TELEFONE) 
    IsWatsApp = models.BooleanField(verbose_name='Watsapp')

    def __str__(self):
        return f'({self.ddd}){self.numero}'



