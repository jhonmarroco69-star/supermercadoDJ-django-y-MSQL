from django.db import models
from django.core.validators import RegexValidator


class Cliente(models.Model):
    cedula = models.CharField(
        max_length=10, unique=True,
        validators=[RegexValidator(r'^\d{6,10}$',
                    'La cédula debe tener entre 6 y 10 dígitos.')])
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{7,10}$',
                    'El teléfono debe tener entre 7 y 10 dígitos.')])

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Producto(models.Model):
    codigo = models.CharField(
        max_length=5, unique=True,
        validators=[RegexValidator(r'^P-\d{3}$',
                    'Formato de código inválido. Ejemplo: P-001.')])
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Empleado(models.Model):
    class Cargo(models.TextChoices):
        CAJERO = 'CAJERO', 'Cajero'
        REPONEDOR = 'REPONEDOR', 'Reponedor'
        ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador'

    cedula = models.CharField(
        max_length=10, unique=True,
        validators=[RegexValidator(r'^\d{6,10}$',
                    'La cédula debe tener entre 6 y 10 dígitos.')])
    nombre = models.CharField(max_length=120)
    cargo = models.CharField(
        max_length=15, choices=Cargo.choices, default=Cargo.CAJERO)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'empleado'

    def __str__(self):
        return f"{self.nombre} ({self.get_cargo_display()})"


class Orden(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        PAGADA = 'PAGADA', 'Pagada'
        ENTREGADA = 'ENTREGADA', 'Entregada'
        ANULADA = 'ANULADA', 'Anulada'

    numero_orden = models.CharField(max_length=10, unique=True, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, editable=False)
    estado = models.CharField(
        max_length=25, choices=Estado.choices, default=Estado.PENDIENTE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_actualizacion']
        db_table = 'orden'
        verbose_name = 'Orden'
        verbose_name_plural = 'Órdenes'

    def save(self, *args, **kwargs):
        # Genera el consecutivo OR-001, OR-002... la primera vez que se guarda
        if not self.numero_orden:
            ultima = Orden.objects.order_by('-id').first()
            n = (int(ultima.numero_orden.split('-')[1]) + 1) if ultima else 1
            self.numero_orden = f"OR-{n:03d}"
            self.total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.numero_orden} - {self.cliente.nombre}"
