from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

class CategoryManager(models.Manager):
    def get_queryset(self):
            return super(CategoryManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    title = models.CharField(max_length=400)
    parent = models.ForeignKey("Category",on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    slug = models.SlugField(max_length=500,db_index=True,unique=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # objects = CategoryManager()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Brand(models.Model):
    title = models.CharField(max_length=400)
    parent = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name='brand', null=True, blank=True)
    slug = models.SlugField(max_length=500, db_index=True, unique=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # objects = CategoryManager()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Brand, self).save()


class Product(models.Model):
    title = models.CharField(max_length=400)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    slug = models.SlugField(max_length=500, db_index=True, unique=True)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    price = models.DecimalField(max_digits=8,decimal_places=2)
    rate = models.IntegerField(default=1 , validators=[MinValueValidator(1) , MaxValueValidator(5)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Product, self).save()


class Tag(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=400)
    products = models.ManyToManyField(Product)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Tag, self).save()