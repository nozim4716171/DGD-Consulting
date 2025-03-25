🌍 DGD Consulting - Geologik Tadqiqotlar Platformasi

DGD Consulting - bu geologik tadqiqotlar**, resurslarni boshqarish** va innovatsion kartografiya xizmatlarini taqdim etuvchi platforma. Sayt geologiya sohasida ishlovchi mutaxassislarga va tashkilotlarga aniq ma'lumotlar va samarali echimlarni taqdim etishga qaratilgan.

🚀 Loyiha Xususiyatlari

✅ Geologik Izlanishlar - Tabiiy resurslarni aniq baholash va kartografiya qilish  
✅ Foydali Qazilma Tahlillari - Xomashyo bazasini kengaytirish uchun yuqori sifatli tahlillar  
✅ Geofizik Tadqiqotlar- Raqamli xaritalar va yer osti tadqiqotlari  
✅ Resurslarni Boshqarish - Barqaror rivojlanish va tabiiy resurslardan foydalanish  

---

📺 O‘rnatish va Ishga Tushirish

Django asosida ishlab chiqilgan ushbu platformani ishga tushirish uchun quyidagi bosqichlarni bajaring:

1️⃣ Muhitni tayyorlash
Python va kerakli kutubxonalarni o‘rnating:


pip install -r requirements.txt


2️⃣ Ma’lumotlar Bazasini Sozlash
Django uchun migratsiyalarni bajaring:


python manage.py migrate


3️⃣ Tarjimani Yangilash
Agar O‘zbekcha yoki Ruscha tarjimalar noto‘g‘ri chiqayotgan bo‘lsa:


python manage.py compilemessages


4️⃣ Serverni Ishga Tushirish

python manage.py runserver

Keyin http://127.0.0.1:8000/ ga kiring va saytdan foydalaning!

---

📁 Loyiha Tuzilishi


DGD_Consulting/
│── config/             # Django sozlamalari
│── core/               # Asosiy backend logikasi
│── templates/          # HTML shablonlar
│── static/             # CSS, JS, va tasvirlar
│── locale/             # Tarjima fayllari (O'zbekcha & Ruscha)
│── manage.py           # Django boshqaruv skripti
│── requirements.txt    # Kerakli kutubxonalar
│── README.md           # Loyiha hujjati
│── .env                # Muhit sozlamalari (maxfiy)


---

🔧 Texnologiyalar

- Backend: Django, Python  
- Frontend: HTML, CSS, JavaScript (Bootstrap)  
- Ma’lumotlar Bazasi: PostgreSQL / SQLite  
- Tarjima: `gettext` bilan O‘zbekcha va Ruscha qo‘llab-quvvatlanadi  

---

⚠️ Xatoliklarni Tuzatish

Agar `gettext` tarjima tizimi xatolik bersa (`struct.error: unpack requires a buffer of 4 bytes`), quyidagilarni bajaring:


find . -name "*.mo" -delete
python manage.py compilemessages


Agar sayt ishlamay qolsa**, `debug.log` faylini tekshiring yoki quyidagilarni bajaring:


python manage.py runserver --noreload


---

👥 Bog‘lanish

Agar loyihaga oid savollaringiz bo‘lsa, quyidagi manzillar orqali bog‘laning:

📧 Email: dgdconsulting2011@gmail.com       
🌐 Veb-sayt: [dgdconsulting.uz](http://dgdconsulting.uz)  
📍 Manzil: Toshkent, O‘zbekiston  

---

📝 Litsenziya

Ushbu loyiha DGD Consulting tomonidan yaratilgan va foydalanish shartlariga muvofiq taqdim etiladi.

