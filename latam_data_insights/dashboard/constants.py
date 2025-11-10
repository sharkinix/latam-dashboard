# ====================================================================
# MAPEO DE DATOS ESTÁTICOS PARA ANÁLISIS DE VUELOS
# ====================================================================

# 1. Mapeo de Nombre de Ciudad (como está en la DB) a Código de País (ISO 3166-1 alpha-2)
# Esto es CRUCIAL para mostrar las banderas correctamente en el dashboard.
AIRPORT_COUNTRY_MAP = {
    # 🇨🇱 Chile
    'Santiago': 'cl',
    'Santiago de Chile': 'cl',
    'Valparaiso': 'cl',
    'Antofagasta': 'cl',
    'Concepción': 'cl',
    'Puerto Montt': 'cl',

    # 🇦🇷 Argentina
    'Buenos Aires': 'ar',
    'Córdoba': 'ar',
    'Mendoza': 'ar',
    'Rosario': 'ar',

    # 🇨🇴 Colombia
    'Bogotá': 'co',
    'Medellín': 'co',
    'Cartagena': 'co',
    'Cali': 'co',

    # 🇵🇪 Perú
    'Lima': 'pe',
    'Cusco': 'pe',
    'Arequipa': 'pe',

    # 🇪🇨 Ecuador
    'Quito': 'ec',
    'Guayaquil': 'ec',

    # 🇧🇷 Brasil
    'Rio': 'br',
    'Río de Janeiro': 'br',
    'São Paulo': 'br',
    'Brasilia': 'br',
    'Salvador': 'br',
    'Recife': 'br',
    'Fortaleza': 'br',

    # 🇲🇽 México
    'Ciudad de México': 'mx',
    'Cancún': 'mx',
    'Guadalajara': 'mx',
    'Monterrey': 'mx',
    'Tijuana': 'mx',

    # 🇺🇸 Estados Unidos
    'Los Ángeles': 'us',
    'Miami': 'us',
    'Nueva York': 'us',
    'New York': 'us',
    'Chicago': 'us',
    'Houston': 'us',
    'Dallas': 'us',
    'Atlanta': 'us',
    'San Francisco': 'us',
    'Las Vegas': 'us',

    # 🇨🇦 Canadá
    'Toronto': 'ca',
    'Vancouver': 'ca',
    'Montreal': 'ca',

    # 🇪🇸 España
    'Madrid': 'es',
    'Barcelona': 'es',
    'Sevilla': 'es',
    'Valencia': 'es',
    'Málaga': 'es',

    # 🇫🇷 Francia
    'París': 'fr',
    'Paris': 'fr',
    'Lyon': 'fr',
    'Marsella': 'fr',

    # 🇩🇪 Alemania
    'Berlín': 'de',
    'Berlin': 'de',
    'Múnich': 'de',
    'Frankfurt': 'de',

    # 🇬🇧 Reino Unido
    'Londres': 'gb',
    'Manchester': 'gb',
    'Edimburgo': 'gb',

    # 🇮🇹 Italia
    'Roma': 'it',
    'Milán': 'it',
    'Venecia': 'it',
    'Florencia': 'it',

    # 🇯🇵 Japón
    'Tokyo': 'jp',
    'Osaka': 'jp',
    'Kioto': 'jp',

    # 🇨🇳 China
    'Beijing': 'cn',
    'Pekín': 'cn',
    'Shanghái': 'cn',
    'Hong Kong': 'hk',

    # 🇵🇦 Panamá
    'Ciudad de Panamá': 'pa',

    # 🇺🇾 Uruguay
    'Montevideo': 'uy',

    # 🇵🇾 Paraguay
    'Asunción': 'py',

    # 🇧🇴 Bolivia
    'La Paz': 'bo',
    'Santa Cruz': 'bo',

    # 🇨🇷 Costa Rica
    'San José': 'cr',

    # 🇩🇴 República Dominicana
    'Santo Domingo': 'do',

    # 🇨🇱 Extra Chile (por vuelos internos o variantes)
    'Temuco': 'cl',
    'Iquique': 'cl',
    'La Serena': 'cl',

    # 🇵🇷 Puerto Rico
    'San Juan': 'pr',
}

# 2. Lista de Países para futuros análisis (opcional, pero útil)
COUNTRIES_LIST = [
    {'code': 'cl', 'name': 'Chile', 'cities': ['Santiago', 'Santiago de Chile', 'Valparaiso', 'Antofagasta', 'Concepción', 'Puerto Montt', 'Temuco', 'Iquique', 'La Serena']},
    {'code': 'ar', 'name': 'Argentina', 'cities': ['Buenos Aires', 'Córdoba', 'Mendoza', 'Rosario']},
    {'code': 'co', 'name': 'Colombia', 'cities': ['Bogotá', 'Medellín', 'Cartagena', 'Cali']},
    {'code': 'pe', 'name': 'Perú', 'cities': ['Lima', 'Cusco', 'Arequipa']},
    {'code': 'ec', 'name': 'Ecuador', 'cities': ['Quito', 'Guayaquil']},
    {'code': 'br', 'name': 'Brasil', 'cities': ['Rio', 'Río de Janeiro', 'São Paulo', 'Brasilia', 'Salvador', 'Recife', 'Fortaleza']},
    {'code': 'mx', 'name': 'México', 'cities': ['Ciudad de México', 'Cancún', 'Guadalajara', 'Monterrey', 'Tijuana']},
    {'code': 'us', 'name': 'Estados Unidos', 'cities': ['Los Ángeles', 'Miami', 'Nueva York', 'New York', 'Chicago', 'Houston', 'Dallas', 'Atlanta', 'San Francisco', 'Las Vegas']},
    {'code': 'ca', 'name': 'Canadá', 'cities': ['Toronto', 'Vancouver', 'Montreal']},
    {'code': 'es', 'name': 'España', 'cities': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Málaga']},
    {'code': 'fr', 'name': 'Francia', 'cities': ['París', 'Paris', 'Lyon', 'Marsella']},
    {'code': 'de', 'name': 'Alemania', 'cities': ['Berlín', 'Berlin', 'Múnich', 'Frankfurt']},
    {'code': 'gb', 'name': 'Reino Unido', 'cities': ['Londres', 'Manchester', 'Edimburgo']},
    {'code': 'it', 'name': 'Italia', 'cities': ['Roma', 'Milán', 'Venecia', 'Florencia']},
    {'code': 'jp', 'name': 'Japón', 'cities': ['Tokyo', 'Osaka', 'Kioto']},
    {'code': 'cn', 'name': 'China', 'cities': ['Beijing', 'Pekín', 'Shanghái']},
    {'code': 'hk', 'name': 'Hong Kong', 'cities': ['Hong Kong']},
    {'code': 'pa', 'name': 'Panamá', 'cities': ['Ciudad de Panamá']},
    {'code': 'uy', 'name': 'Uruguay', 'cities': ['Montevideo']},
    {'code': 'py', 'name': 'Paraguay', 'cities': ['Asunción']},
    {'code': 'bo', 'name': 'Bolivia', 'cities': ['La Paz', 'Santa Cruz']},
    {'code': 'cr', 'name': 'Costa Rica', 'cities': ['San José']},
    {'code': 'do', 'name': 'República Dominicana', 'cities': ['Santo Domingo']},
    {'code': 'pr', 'name': 'Puerto Rico', 'cities': ['San Juan']},
]
