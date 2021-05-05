from django.db import models
#from Django_countries.fields import CountryField #AGREGADA

# Create your models here.
class Distribuidor(models.Model):
	nombre= models.CharField(max_length=30)
	direccion= models.CharField(max_length=30)
	rut= models.IntegerField(blank=True)
	horario= models.TimeField(default='08:00', verbose_name='Horario de Apertura')
	horariocierre= models.TimeField(default='18:00', verbose_name='Horario de Cierre')
	telefono= models.CharField(max_length=12)
	sitio_web= models.URLField(blank=True, verbose_name='Sitio Web')
	email= models.EmailField(blank=True, verbose_name='Correo electónico')
	class Meta:
		verbose_name_plural = "Distribuidores"
		

	def __str__(self):
		return self.nombre

class Bebida(models.Model):
	whisky='Whisky'
	cerveza= 'Cerveza'
	vino= 'Vino'
	licor= 'Licores'
	categoria_sel= [(whisky,'Whisky'), (cerveza,'Cerveza'), (vino, 'Vino'), (licor,'Licor'),]
	categoria= models.CharField(
		max_length=8,
		choices= categoria_sel,
		default= vino,
		)
	marca=models.CharField(max_length=30, verbose_name='Marca', default='')
	contenido_neto = models.CharField(max_length=6, verbose_name='Cont.Neto')
	stock= models.IntegerField()
	precio=models.DecimalField(max_digits=8, decimal_places=2,default=0)
	distribuidor= models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
	origen= models.CharField(max_length=30)
	imagen= models.ImageField(upload_to='bebida_img')
	class Meta:
		verbose_name_plural = "Bebidas"

	def __str__(self):
		return "%s %s" % (self.categoria, self.marca)
	
