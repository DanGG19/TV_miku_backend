# TV Miku Backend

Backend del proyecto TV Miku construido con Django y Django REST Framework.

## Stack
- Python
- Django
- Django REST Framework
- django-filter
- Pillow
- SQLite

## Apps
- core
- accounts
- catalog
- products
- site_config
- cart
- cms

## Funcionalidades actuales
- CRUD administrativo desde Django Admin para:
  - categorías
  - marcas
  - tipos de producto
  - productos
  - imágenes de productos
  - configuración del sitio
  - banners
- API pública para:
  - categorías
  - marcas
  - tipos de producto
  - productos
  - detalle de producto por slug
  - configuración del sitio
  - banners
- Validación de carrito
- Preview de carrito para envío a WhatsApp

## Endpoints principales

### Catálogo
- `GET /api/catalog/categories/`
- `GET /api/catalog/brands/`
- `GET /api/catalog/product-types/`

### Productos
- `GET /api/products/`
- `GET /api/products/<slug>/`

Filtros disponibles:
- `?search=`
- `?category=`
- `?brand=`
- `?product_type=`
- `?min_price=`
- `?max_price=`
- `?available=`
- `?featured=`
- `?ordering=price`
- `?ordering=-price`
- `?ordering=name`
- `?ordering=-created_at`

### Configuración del sitio
- `GET /api/site/`

### CMS
- `GET /api/cms/banners/`

### Carrito
- `POST /api/cart/validate/`
- `POST /api/cart/whatsapp-preview/`

## Instalación

```bash
git clone https://github.com/DanGG19/TV_miku_backend.git
cd TV_miku_backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
