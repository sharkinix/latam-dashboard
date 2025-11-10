# 🌎 LATAM Dashboard

**LATAM Dashboard** es una aplicación web desarrollada con **Django** que permite visualizar métricas y estadísticas de vuelos en América Latina mediante un panel analítico moderno.  
El sistema cuenta con un **diseño oscuro inspirado en ChatGPT**, componentes personalizables y una estructura adaptable enfocada en la presentación de datos.

---

## 🚀 Características principales

- 🎨 **Modo oscuro persistente** con animaciones suaves.  
- 📊 **Visualización de estadísticas** e indicadores clave de vuelos.  
- 🌍 **Mapeo de países** mediante banderas (ISO 3166-1).  
- ⚙️ **Panel administrativo funcional** de Django.  
- 📱 **Diseño responsive** adaptable a escritorio y móvil.  
- 💾 Integración con base de datos SQLite.

---

## 🧩 Tecnologías utilizadas

- **Python 3.x**
- **Django 5.x**
- **SQLite3**
- **HTML5, CSS3, JavaScript**
- **Font Awesome**
- **Chart.js**

---

## 🛠️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
bash:
git clone https://github.com/sharkinix/latam-dashboard.git
cd latam-dashboard

### 2️⃣ Crear entorno virtual
python -m venv venv

En Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3️⃣ Instalar dependencias
pip install -r requerements.txt

### 4️⃣ Aplicar migraciones y ejecutar

python manage.py migrate
python manage.py runserver

Luego abre tu navegador en 👉 http://127.0.0.1:8000/


