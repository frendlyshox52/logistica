# Logistica — nimalarni to'g'irlash kerak

Loyiha ishga tushyapti, lekin hozircha faqat bosh sahifa bor va u to'liq chiqmayapti. Pastda hammasini yozib qo'ydim.
Tartib bilan, birinchi punktdan boshlab qil. Har bir qismdan keyin `python manage.py runserver` qilib tekshirib tur.

Eslatma: loyiha tuzilishini o'zgartirdim.
- `config` bu **loyiha** (settings, urls), `blog` esa **app** (models, views).
- Hamma sahifalar `templates/` papkada, CSS, JS va rasmlar `static/` papkada.
- `base.html` tayyor: unda menyu, footer, CSS va JS bor. `index.html` undan foydalanyapti (`{% extends "base.html" %}`).

Ishni boshlashdan oldin (Windows terminal):
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```
Agar PowerShell `activate` da xato bersa, avval shuni yoz:
```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## 1-qism. Static fayllar

**1. `base.html` da qolgan yo'llar**
CSS ning bir qismi `{% static %}` bilan yozilgan, lekin hammasi emas. Shularni ham `{% static %}` ga o'tkaz:
- 13-qator: `img/favicon.ico`
- 148–152-qatorlar: `lib/wow`, `lib/easing`, `lib/waypoints`, `lib/counterup`, `lib/owlcarousel` skriptlari

Misol:
```html
<script src="{% static 'lib/wow/wow.min.js' %}"></script>
```

**2. `index.html` dagi rasmlar**
`index.html` da 18 ta rasm `src="img/..."` deb yozilgan, ular chiqmaydi.
- `{% extends "base.html" %}` dan keyin `{% load static %}` yoz. Bu `base.html` dan o'tmaydi, har bir faylda alohida yoziladi.
- Hamma `src="img/carousel-1.jpg"` larni `src="{% static 'img/carousel-1.jpg' %}"` qil.

Tekshir: sahifa ochilganda rasmlar, slayder va animatsiyalar ishlashi kerak.

---

## 2-qism. Sahifalar

**3. View lar**
Hozir faqat `home` bor. `blog/views.py` da qolgan sahifalar uchun ham funksiya yoz:
`about`, `service`, `price`, `feature`, `quote`, `team`, `testimonial`, `contact`.

**4. `blog/urls.py`**
- `blog` papkada `urls.py` yarat, hamma sahifalar uchun `path(...)` yoz. Har biriga `name=` ber.
- `config/urls.py` da `from blog.views import home` ni o'chir, o'rniga `path('', include('blog.urls'))` yoz.

**5. Menyu linklari**
`base.html` da linklar `href="about.html"` deb yozilgan — bu ishlamaydi.
Hammasini `{% url %}` ga o'tkaz: `href="{% url 'about' %}"`.
- menyu: 47–69-qatorlar
- footer: 99–111 va 127-qatorlar

**6. Qolgan sahifalar `base.html` dan foydalansin**
`about.html`, `service.html`, `price.html`, `feature.html`, `quote.html`, `team.html`, `testimonial.html`, `contact.html`, `404.html` — bular hali to'liq sahifa.
Har birida `index.html` dagidek qil:
- tepasiga `{% extends "base.html" %}` va `{% load static %}` yoz;
- `<head>`, Spinner, Navbar, Footer va skriptlarni o'chir;
- qolgan o'rtadagi qismni `{% block content %}` ... `{% endblock %}` ichiga ol;
- rasmlarni `{% static %}` ga o'tkaz.

Bu sahifalar inglizcha. Vaqting bo'lsa, `index.html` dagidek o'zbekchaga tarjima qil.

---

## 3-qism. Model va admin

**7. Migratsiya**
`models.py` dagi `Meta` o'zgargan, lekin migratsiya qilinmagan. `python manage.py makemigrations` va `python manage.py migrate` qil.

**8. `Maxsulot` modeli**
- `__str__` qo'sh, admin panelda nomi ko'rinsin.
- Rasm yuklash uchun `settings.py` ga `MEDIA_URL = 'media/'` va `MEDIA_ROOT = BASE_DIR / 'media'` qo'sh,
  `config/urls.py` da media fayllarni ulab qo'y.
- `admin.py` da `from .models import *` emas, `from .models import Maxsulot` yoz.

**9. Ma'lumotni sahifaga chiqar**
Admin orqali 3–4 ta mahsulot qo'sh. Keyin view da `Maxsulot.objects.all()` ni shablonga yubor
va `price.html` da `{% for item in items %}` bilan chiqar.

**10. Formalar**
`contact.html`, `quote.html`, `price.html` dagi `<form>` larga `method="post"` va `{% csrf_token %}` qo'sh.
`index.html` va `base.html` dagi formalarda `method="post"` bor, lekin `{% csrf_token %}` yo'q — qo'sh.

---

## 4-qism. Kodni tozalash

**11.** `blog/views.py` dagi izohga olingan (`#`) eski kodni va ikkinchi `from django.shortcuts import render` ni o'chir.

**12.** `README.md` ga loyihani qanday ishga tushirishni yoz (yuqoridagi 4 ta buyruq).

---

Hammasini qilib bo'lgach, menga yoz — tekshirib beraman.
