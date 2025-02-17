from django.db import models

## Cadastro de Clientes     
class Cliente(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=15)
    is_ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} - {} - {}".format(self.name, self.phone, self.email)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']