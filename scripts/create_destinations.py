# Python generator for destinations
import json

passports = [
    'TR_BORDO', 'TR_YESIL', 'TR_GRI', 'DE', 'US', 'GB', 'FR', 'IT', 'ES', 'JP',
    'SG', 'AE', 'AZ', 'GE', 'RU', 'CA', 'AU', 'KR', 'CN', 'GR'
]

schengen_countries = [
    ('DE', 'Almanya', 'Germany', '🇩🇪'),
    ('FR', 'Fransa', 'France', '🇫🇷'),
    ('IT', 'İtalya', 'Italy', '🇮🇹'),
    ('ES', 'İspanya', 'Spain', '🇪🇸'),
    ('NL', 'Hollanda', 'Netherlands', '🇳🇱'),
    ('BE', 'Belçika', 'Belgium', '🇧🇪'),
    ('AT', 'Avusturya', 'Austria', '🇦🇹'),
    ('CH', 'İsviçre', 'Switzerland', '🇨🇭'),
    ('SE', 'İsveç', 'Sweden', '🇸🇪'),
    ('NO', 'Norveç', 'Norway', '🇳🇴'),
    ('DK', 'Danimarka', 'Denmark', '🇩🇰'),
    ('FI', 'Finlandiya', 'Finland', '🇫🇮'),
    ('GR', 'Yunanistan', 'Greece', '🇬🇷'),
    ('PT', 'Portekiz', 'Portugal', '🇵🇹'),
    ('PL', 'Polonya', 'Poland', '🇵🇱'),
    ('CZ', 'Çekya', 'Czechia', '🇨🇿'),
    ('HU', 'Macaristan', 'Hungary', '🇭🇺'),
    ('HR', 'Hırvatistan', 'Croatia', '🇭🇷'),
    ('BG', 'Bulgaristan', 'Bulgaria', '🇧🇬'),
    ('RO', 'Romanya', 'Romania', '🇷🇴'),
    ('SK', 'Slovakya', 'Slovakia', '🇸🇰'),
    ('SI', 'Slovenya', 'Slovenia', '🇸🇮'),
    ('EE', 'Estonya', 'Estonia', '🇪🇪'),
    ('LV', 'Letonya', 'Latvia', '🇱🇻'),
    ('LT', 'Litvanya', 'Lithuania', '🇱🇹'),
    ('IS', 'İzlanda', 'Iceland', '🇮🇸'),
    ('LU', 'Lüksemburg', 'Luxembourg', '🇱🇺'),
    ('MT', 'Malta', 'Malta', '🇲🇹'),
    ('LI', 'Lihtenştayn', 'Liechtenstein', '🇱🇮')
]

destinations = []

for code, name_tr, name_en, flag in schengen_countries:
    visas = {}
    for pid in passports:
        if pid == 'TR_BORDO':
            visas[pid] = {'status': 'required', 'days': None, 'note': 'Schengen Vizesi Zorunlu (Konsolosluk)'}
        elif pid in ['TR_YESIL', 'TR_GRI']:
            visas[pid] = {'status': 'free', 'days': '90 Gün', 'note': '180 günde 90 gün Vizesiz'}
        elif pid in ['DE', 'FR', 'IT', 'ES', 'GR']:
            visas[pid] = {'status': 'free', 'days': 'Süresiz', 'note': 'AB Vatandaşı / Serbest Dolaşım'}
        elif pid in ['US', 'GB', 'JP', 'SG', 'CA', 'AU', 'KR', 'AE', 'GE']:
            visas[pid] = {'status': 'free', 'days': '90 Gün', 'note': 'Vizesiz (ETIAS 90 Gün)'}
        elif pid in ['AZ', 'RU', 'CN']:
            visas[pid] = {'status': 'required', 'days': None, 'note': 'Schengen Vizesi Gerekli'}
        else:
            visas[pid] = {'status': 'free', 'days': '90 Gün', 'note': 'Vizesiz'}
    
    destinations.append({
        'id': code,
        'name': name_tr,
        'nameEn': name_en,
        'flag': flag,
        'continent': 'Avrupa',
        'isSchengen': True,
        'visas': visas
    })

other_countries = [
    # Non-Schengen Europe
    {
        'id': 'GB', 'name': 'Birleşik Krallık', 'nameEn': 'United Kingdom', 'flag': '🇬🇧', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('required', None, 'Standart Ziyaretçi Vizesi'),
            'TR_YESIL': ('required', None, 'Vize Gerekli (Yeşil Pasaporta muafiyet yok)'),
            'TR_GRI': ('required', None, 'Vize Gerekli'),
            'DE': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'FR': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'IT': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'ES': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'GR': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'US': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'CA': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'AU': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'JP': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'SG': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'KR': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
            'AE': ('evisa', '6 Ay', 'Elektronik Seyahat İzni (ETA)'),
            'default': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'IE', 'name': 'İrlanda', 'nameEn': 'Ireland', 'flag': '🇮🇪', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('required', None, 'İrlanda Turist Vizesi'),
            'TR_YESIL': ('required', None, 'Vize Gerekli (Yeşil Pasaporta muafiyet yok)'),
            'TR_GRI': ('required', None, 'Vize Gerekli'),
            'GB': ('free', 'Süresiz', 'Ortak Seyahat Alanı (CTA)'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz'),
            'AZ': ('required', None, 'Vize Gerekli'),
            'GE': ('required', None, 'Vize Gerekli'),
            'RU': ('required', None, 'Vize Gerekli'),
            'CN': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'TRNC', 'name': 'Kuzey Kıbrıs (KKTC)', 'nameEn': 'Northern Cyprus', 'flag': '🇹🇷', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
            'TR_YESIL': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
            'TR_GRI': ('free', '90 Gün', 'Kimlikle Giriş Mümkün'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'BA', 'name': 'Bosna-Hersek', 'nameEn': 'Bosnia and Herzegovina', 'flag': '🇧🇦', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', 'Çipli Kimlik Kartı / Pasaportla Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', 'Çipli Kimlik Kartı / Pasaportla Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Kimlikle Giriş'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'RS', 'name': 'Sırbistan', 'nameEn': 'Serbia', 'flag': '🇷🇸', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', 'Çipli Kimlik Kartı / Pasaportla Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', 'Çipli Kimlik Kartı / Pasaportla Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Kimlikle Giriş'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'ME', 'name': 'Karadağ', 'nameEn': 'Montenegro', 'flag': '🇲🇪', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '180 günde 90 gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '180 günde 90 gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'AL', 'name': 'Arnavutluk', 'nameEn': 'Albania', 'flag': '🇦🇱', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'MK', 'name': 'Kuzey Makedonya', 'nameEn': 'North Macedonia', 'flag': '🇲🇰', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'XK', 'name': 'Kosova', 'nameEn': 'Kosovo', 'flag': '🇽🇰', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'MD', 'name': 'Moldova', 'nameEn': 'Moldova', 'flag': '🇲🇩', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
            'TR_YESIL': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
            'TR_GRI': ('free', '90 Gün', 'Kimlikle Giriş'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'UA', 'name': 'Ukrayna', 'nameEn': 'Ukraine', 'flag': '🇺🇦', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
            'TR_YESIL': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
            'TR_GRI': ('free', '90 Gün', 'Kimlikle Giriş'),
            'RU': ('required', None, 'Vize Gerekli'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'GE', 'name': 'Gürcistan', 'nameEn': 'Georgia', 'flag': '🇬🇪', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '1 Yıl', 'Çipli Kimlik Kartı ile Giriş (1 Yıl)'),
            'TR_YESIL': ('free', '1 Yıl', 'Çipli Kimlik Kartı ile Giriş (1 Yıl)'),
            'TR_GRI': ('free', '1 Yıl', 'Kimlikle Giriş (1 Yıl)'),
            'GE': ('free', 'Süresiz', 'Vatandaş'),
            'default': ('free', '1 Yıl', '1 Yıl Vizesiz')
        }
    },
    {
        'id': 'AZ', 'name': 'Azerbaycan', 'nameEn': 'Azerbaijan', 'flag': '🇦🇿', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş (90 Gün)'),
            'TR_YESIL': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş (90 Gün)'),
            'TR_GRI': ('free', '90 Gün', 'Kimlikle Giriş (90 Gün)'),
            'AZ': ('free', 'Süresiz', 'Vatandaş'),
            'RU': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'default': ('evisa', '30 Gün', 'ASAN e-Vize')
        }
    },
    {
        'id': 'RU', 'name': 'Rusya', 'nameEn': 'Russia', 'flag': '🇷🇺', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('evisa', '16 Gün', 'Elektronik Vize (e-Visa 16 Gün)'),
            'TR_YESIL': ('free', '30 Gün', 'İkili Anlaşma ile 30 Gün Vizesiz'),
            'TR_GRI': ('free', '30 Gün', 'İkili Anlaşma ile 30 Gün Vizesiz'),
            'RU': ('free', 'Süresiz', 'Vatandaş'),
            'AZ': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('free', '15 Gün', 'Grup Turizmi Vizesiz'),
            'AE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'US': ('required', None, 'Konsolosluk Vizesi'),
            'GB': ('required', None, 'Konsolosluk Vizesi'),
            'CA': ('required', None, 'Konsolosluk Vizesi'),
            'AU': ('required', None, 'Konsolosluk Vizesi'),
            'default': ('evisa', '16 Gün', 'Elektronik Vize')
        }
    },
    {
        'id': 'BY', 'name': 'Belarus', 'nameEn': 'Belarus', 'flag': '🇧🇾', 'continent': 'Avrupa',
        'rules': {
            'TR_BORDO': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_YESIL': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_GRI': ('free', '30 Gün', '30 Gün Vizesiz'),
            'RU': ('free', 'Süresiz', 'Birlik Devleti / Serbest'),
            'AZ': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('free', '30 Gün', '30 Gün Vizesiz'),
            'default': ('free', '30 Gün', 'Minsk Havalimanından 30 Gün')
        }
    },
    # Americas
    {
        'id': 'US', 'name': 'Amerika Birleşik Devletleri', 'nameEn': 'United States', 'flag': '🇺🇸', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('required', None, 'B1/B2 Konsolosluk Vizesi'),
            'TR_YESIL': ('required', None, 'Vize Gerekli (Yeşil Pasaporta muafiyet yok)'),
            'TR_GRI': ('required', None, 'Vize Gerekli'),
            'US': ('free', 'Süresiz', 'Vatandaş'),
            'CA': ('free', '6 Ay', 'Vizesiz / 6 Ay'),
            'DE': ('evisa', '90 Gün', 'ESTA İzni'),
            'FR': ('evisa', '90 Gün', 'ESTA İzni'),
            'IT': ('evisa', '90 Gün', 'ESTA İzni'),
            'ES': ('evisa', '90 Gün', 'ESTA İzni'),
            'GR': ('evisa', '90 Gün', 'ESTA İzni'),
            'GB': ('evisa', '90 Gün', 'ESTA İzni'),
            'JP': ('evisa', '90 Gün', 'ESTA İzni'),
            'SG': ('evisa', '90 Gün', 'ESTA İzni'),
            'KR': ('evisa', '90 Gün', 'ESTA İzni'),
            'AU': ('evisa', '90 Gün', 'ESTA İzni'),
            'default': ('required', None, 'Konsolosluk Vizesi Gerekli')
        }
    },
    {
        'id': 'CA', 'name': 'Kanada', 'nameEn': 'Canada', 'flag': '🇨🇦', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('required', None, 'Kanada Ziyaretçi Vizesi'),
            'TR_YESIL': ('required', None, 'Vize Gerekli (Yeşil Pasaporta muafiyet yok)'),
            'TR_GRI': ('required', None, 'Vize Gerekli'),
            'CA': ('free', 'Süresiz', 'Vatandaş'),
            'US': ('free', '6 Ay', 'Vizesiz (Pasaportla)'),
            'DE': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'FR': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'IT': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'ES': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'GR': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'GB': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'JP': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'SG': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'KR': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'AU': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'),
            'default': ('required', None, 'Ziyaretçi Vizesi Gerekli')
        }
    },
    {
        'id': 'MX', 'name': 'Meksika', 'nameEn': 'Mexico', 'flag': '🇲🇽', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('evisa', '180 Gün', 'Elektronik Onay (SAE / Havayoluyla)'),
            'TR_YESIL': ('evisa', '180 Gün', 'SAE / Geçerli Schengen-ABD Vizesiyle Vizesiz'),
            'TR_GRI': ('evisa', '180 Gün', 'SAE'),
            'US': ('free', '180 Gün', '180 Gün Vizesiz'),
            'CA': ('free', '180 Gün', '180 Gün Vizesiz'),
            'default': ('free', '180 Gün', '180 Gün Vizesiz'),
            'AZ': ('evisa', '180 Gün', 'SAE'),
            'RU': ('evisa', '180 Gün', 'SAE'),
            'CN': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'BR', 'name': 'Brezilya', 'nameEn': 'Brazil', 'flag': '🇧🇷', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'US': ('evisa', '90 Gün', 'Elektronik Vize (e-Visa)'),
            'CA': ('evisa', '90 Gün', 'Elektronik Vize (e-Visa)'),
            'AU': ('evisa', '90 Gün', 'Elektronik Vize (e-Visa)'),
            'CN': ('required', None, 'Vize Gerekli'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'AR', 'name': 'Arjantin', 'nameEn': 'Argentina', 'flag': '🇦🇷', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'CN': ('evisa', '90 Gün', 'AVE e-Vize'),
            'AZ': ('required', None, 'Vize Gerekli'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'CL', 'name': 'Şili', 'nameEn': 'Chile', 'flag': '🇨🇱', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz'),
            'AZ': ('required', None, 'Vize Gerekli'),
            'CN': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'CO', 'name': 'Kolombiya', 'nameEn': 'Colombia', 'flag': '🇨🇴', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'PE', 'name': 'Peru', 'nameEn': 'Peru', 'flag': '🇵🇪', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'CU', 'name': 'Küba', 'nameEn': 'Cuba', 'flag': '🇨🇺', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('evisa', '90 Gün', 'Elektronik Turist Kartı (eVisa)'),
            'TR_YESIL': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'İkili Anlaşma ile Vizesiz'),
            'CN': ('free', '90 Gün', '90 Gün Vizesiz'),
            'RU': ('free', '90 Gün', '90 Gün Vizesiz'),
            'default': ('evisa', '90 Gün', 'Turist Kartı (eVisa)')
        }
    },
    {
        'id': 'DO', 'name': 'Dominik Cumhuriyeti', 'nameEn': 'Dominican Republic', 'flag': '🇩🇴', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('evisa', '30 Gün', 'E-Ticket Giriş Formu (30 Gün)'),
            'TR_YESIL': ('evisa', '30 Gün', 'E-Ticket Giriş Formu'),
            'TR_GRI': ('evisa', '30 Gün', 'E-Ticket'),
            'default': ('evisa', '30 Gün', 'E-Ticket Giriş Formu')
        }
    },
    {
        'id': 'CR', 'name': 'Kosta Rika', 'nameEn': 'Costa Rica', 'flag': '🇨🇷', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('required', None, 'Vize Gerekli'),
            'AZ': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'PA', 'name': 'Panama', 'nameEn': 'Panama', 'flag': '🇵🇦', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    # Asia & Middle East
    {
        'id': 'JP', 'name': 'Japonya', 'nameEn': 'Japan', 'flag': '🇯🇵', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'JP': ('free', 'Süresiz', 'Vatandaş'),
            'DE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'FR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'IT': ('free', '90 Gün', '90 Gün Vizesiz'),
            'ES': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'US': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GB': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CA': ('free', '90 Gün', '90 Gün Vizesiz'),
            'AU': ('free', '90 Gün', '90 Gün Vizesiz'),
            'SG': ('free', '90 Gün', '90 Gün Vizesiz'),
            'KR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'AE': ('free', '30 Gün', '30 Gün Vizesiz'),
            'AZ': ('required', None, 'Vize Gerekli'),
            'GE': ('required', None, 'Vize Gerekli'),
            'RU': ('required', None, 'Vize Gerekli'),
            'CN': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'KR', 'name': 'Güney Kore', 'nameEn': 'South Korea', 'flag': '🇰🇷', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '90 Gün', 'K-ETA İzni (90 Gün)'),
            'TR_YESIL': ('evisa', '90 Gün', 'K-ETA İzni (90 Gün)'),
            'TR_GRI': ('evisa', '90 Gün', 'K-ETA'),
            'KR': ('free', 'Süresiz', 'Vatandaş'),
            'DE': ('free', '90 Gün', 'K-ETA Muafiyeti'),
            'FR': ('free', '90 Gün', 'K-ETA Muafiyeti'),
            'IT': ('free', '90 Gün', 'K-ETA Muafiyeti'),
            'ES': ('free', '90 Gün', 'K-ETA Muafiyeti'),
            'US': ('free', '90 Gün', 'K-ETA Muafiyeti'),
            'GB': ('free', '90 Gün', 'K-ETA Muafiyeti'),
            'JP': ('free', '90 Gün', 'K-ETA Muafiyeti'),
            'SG': ('free', '90 Gün', 'K-ETA Muafiyeti'),
            'AZ': ('required', None, 'Vize Gerekli'),
            'GE': ('required', None, 'Vize Gerekli'),
            'RU': ('evisa', '60 Gün', 'K-ETA'),
            'CN': ('required', None, 'Vize Gerekli'),
            'default': ('evisa', '90 Gün', 'K-ETA')
        }
    },
    {
        'id': 'SG', 'name': 'Singapur', 'nameEn': 'Singapore', 'flag': '🇸🇬', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '30 Gün', '30 Gün Vizesiz (SG Arrival Card)'),
            'TR_YESIL': ('free', '30 Gün', '30 Gün Vizesiz (SG Arrival Card)'),
            'TR_GRI': ('free', '30 Gün', '30 Gün Vizesiz'),
            'SG': ('free', 'Süresiz', 'Vatandaş'),
            'DE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'FR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'IT': ('free', '90 Gün', '90 Gün Vizesiz'),
            'ES': ('free', '90 Gün', '90 Gün Vizesiz'),
            'US': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GB': ('free', '90 Gün', '90 Gün Vizesiz'),
            'JP': ('free', '90 Gün', '90 Gün Vizesiz'),
            'KR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('free', '30 Gün', '30 Gün Vizesiz'),
            'AZ': ('evisa', '30 Gün', 'e-Vize'),
            'RU': ('evisa', '30 Gün', 'e-Vize'),
            'default': ('free', '30 Gün', '30 Gün Vizesiz')
        }
    },
    {
        'id': 'TH', 'name': 'Tayland', 'nameEn': 'Thailand', 'flag': '🇹🇭', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '60 Gün', '60 Gün Vizesiz'),
            'TR_YESIL': ('free', '60 Gün', '60 Gün Vizesiz'),
            'TR_GRI': ('free', '60 Gün', '60 Gün Vizesiz'),
            'DE': ('free', '60 Gün', '60 Gün Vizesiz'),
            'FR': ('free', '60 Gün', '60 Gün Vizesiz'),
            'IT': ('free', '60 Gün', '60 Gün Vizesiz'),
            'ES': ('free', '60 Gün', '60 Gün Vizesiz'),
            'US': ('free', '60 Gün', '60 Gün Vizesiz'),
            'GB': ('free', '60 Gün', '60 Gün Vizesiz'),
            'JP': ('free', '60 Gün', '60 Gün Vizesiz'),
            'SG': ('free', '60 Gün', '60 Gün Vizesiz'),
            'KR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('free', '30 Gün', '30 Gün Vizesiz'),
            'RU': ('free', '60 Gün', '60 Gün Vizesiz'),
            'AZ': ('voa', '15 Gün', 'Kapıda Vize (15 Gün)'),
            'GE': ('free', '60 Gün', '60 Gün Vizesiz'),
            'default': ('free', '60 Gün', '60 Gün Vizesiz')
        }
    },
    {
        'id': 'MY', 'name': 'Malezya', 'nameEn': 'Malaysia', 'flag': '🇲🇾', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz (MDAC Giriş Formu)'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz (MDAC)'),
            'TR_GRI': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('free', '30 Gün', '30 Gün Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'ID', 'name': 'Endonezya', 'nameEn': 'Indonesia (Bali)', 'flag': '🇮🇩', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('voa', '30 Gün', 'Kapıda Vize / e-VoA (30 Gün)'),
            'TR_YESIL': ('voa', '30 Gün', 'Kapıda Vize / e-VoA (30 Gün)'),
            'TR_GRI': ('free', '30 Gün', '30 Gün Vizesiz'),
            'SG': ('free', '30 Gün', 'ASEAN / 30 Gün Vizesiz'),
            'default': ('voa', '30 Gün', 'Kapıda Vize / e-VoA (30 Gün)')
        }
    },
    {
        'id': 'VN', 'name': 'Vietnam', 'nameEn': 'Vietnam', 'flag': '🇻🇳', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '90 Gün', 'Elektronik Vize (e-Visa 90 Gün)'),
            'TR_YESIL': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
            'DE': ('free', '45 Gün', '45 Gün Vizesiz'),
            'FR': ('free', '45 Gün', '45 Gün Vizesiz'),
            'IT': ('free', '45 Gün', '45 Gün Vizesiz'),
            'ES': ('free', '45 Gün', '45 Gün Vizesiz'),
            'GB': ('free', '45 Gün', '45 Gün Vizesiz'),
            'JP': ('free', '45 Gün', '45 Gün Vizesiz'),
            'KR': ('free', '45 Gün', '45 Gün Vizesiz'),
            'RU': ('free', '45 Gün', '45 Gün Vizesiz'),
            'SG': ('free', '30 Gün', '30 Gün Vizesiz'),
            'default': ('evisa', '90 Gün', 'Elektronik Vize')
        }
    },
    {
        'id': 'PH', 'name': 'Filipinler', 'nameEn': 'Philippines', 'flag': '🇵🇭', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '30 Gün', '30 Gün Vizesiz (eTravel Formu)'),
            'TR_YESIL': ('free', '30 Gün', '30 Gün Vizesiz (eTravel Formu)'),
            'TR_GRI': ('free', '30 Gün', 'Vizesiz'),
            'CN': ('required', None, 'Vize Gerekli'),
            'default': ('free', '30 Gün', '30 Gün Vizesiz')
        }
    },
    {
        'id': 'AE', 'name': 'Birleşik Arap Emirlikleri', 'nameEn': 'United Arab Emirates (Dubai)', 'flag': '🇦🇪', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '30 Gün', 'Online e-Vize Gerekli'),
            'TR_YESIL': ('free', '90 Gün', '180 Günde 90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', '180 Günde 90 Gün Vizesiz'),
            'AE': ('free', 'Süresiz', 'Vatandaş'),
            'DE': ('free', '90 Gün', 'Kapıda Kaşe / 90 Gün'),
            'FR': ('free', '90 Gün', 'Kapıda Kaşe / 90 Gün'),
            'IT': ('free', '90 Gün', 'Kapıda Kaşe / 90 Gün'),
            'ES': ('free', '90 Gün', 'Kapıda Kaşe / 90 Gün'),
            'GR': ('free', '90 Gün', 'Kapıda Kaşe / 90 Gün'),
            'US': ('free', '30 Gün', 'Kapıda Kaşe / 30 Gün'),
            'GB': ('free', '30 Gün', 'Kapıda Kaşe / 30 Gün'),
            'CA': ('free', '30 Gün', 'Kapıda Kaşe / 30 Gün'),
            'AU': ('free', '30 Gün', 'Kapıda Kaşe / 30 Gün'),
            'JP': ('free', '30 Gün', 'Kapıda Kaşe / 30 Gün'),
            'SG': ('free', '30 Gün', 'Kapıda Kaşe / 30 Gün'),
            'KR': ('free', '90 Gün', 'Kapıda Kaşe / 90 Gün'),
            'AZ': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'RU': ('free', '90 Gün', '90 Gün Vizesiz'),
            'CN': ('free', '30 Gün', '30 Gün Vizesiz')
        }
    },
    {
        'id': 'SA', 'name': 'Suudi Arabistan', 'nameEn': 'Saudi Arabia', 'flag': '🇸🇦', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '90 Gün', 'Elektronik Vize / Kapıda Vize (90 Gün)'),
            'TR_YESIL': ('evisa', '90 Gün', 'Elektronik Vize / Kapıda Vize (90 Gün)'),
            'TR_GRI': ('evisa', '90 Gün', 'e-Vize'),
            'AE': ('free', 'Süresiz', 'Körfez İşbirliği / Serbest'),
            'DE': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'FR': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'IT': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'ES': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'US': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'GB': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'CA': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'AU': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'JP': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'SG': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'KR': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'CN': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'RU': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'AZ': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'),
            'default': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize')
        }
    },
    {
        'id': 'QA', 'name': 'Katar', 'nameEn': 'Qatar', 'flag': '🇶🇦', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', '90 Gün Vizesiz'),
            'AE': ('free', 'Süresiz', 'Körfez İşbirliği / Serbest'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'OM', 'name': 'Umman', 'nameEn': 'Oman', 'flag': '🇴🇲', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '14 Gün', '14 Gün Vizesiz (Daha uzun için e-Vize)'),
            'TR_YESIL': ('free', '14 Gün', '14 Gün Vizesiz'),
            'TR_GRI': ('free', '14 Gün', '14 Gün Vizesiz'),
            'AE': ('free', 'Süresiz', 'Körfez İşbirliği / Serbest'),
            'default': ('free', '14 Gün', '14 Gün Vizesiz')
        }
    },
    {
        'id': 'BH', 'name': 'Bahreyn', 'nameEn': 'Bahrain', 'flag': '🇧🇭', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '14 Gün', 'e-Vize / Kapıda Vize (14 Gün)'),
            'TR_YESIL': ('evisa', '14 Gün', 'e-Vize / Kapıda Vize'),
            'TR_GRI': ('free', '14 Gün', 'Vizesiz'),
            'AE': ('free', 'Süresiz', 'Körfez İşbirliği / Serbest'),
            'default': ('evisa', '14 Gün', 'e-Vize / Kapıda Vize')
        }
    },
    {
        'id': 'KW', 'name': 'Kuveyt', 'nameEn': 'Kuwait', 'flag': '🇰🇼', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize (3 Ay)'),
            'TR_YESIL': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'İkili Anlaşma ile Vizesiz'),
            'AE': ('free', 'Süresiz', 'Körfez İşbirliği / Serbest'),
            'default': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize')
        }
    },
    {
        'id': 'JO', 'name': 'Ürdün', 'nameEn': 'Jordan', 'flag': '🇯🇴', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('voa', '30 Gün', 'Kapıda Vize (40 JOD)')
        }
    },
    {
        'id': 'LB', 'name': 'Lübnan', 'nameEn': 'Lebanon', 'flag': '🇱🇧', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('voa', '90 Gün', 'Havalimanında Ücretsiz Kapıda Vize (90 Gün)'),
            'TR_YESIL': ('voa', '90 Gün', 'Havalimanında Ücretsiz Kapıda Vize (90 Gün)'),
            'TR_GRI': ('voa', '90 Gün', 'Kapıda Vize'),
            'default': ('voa', '30 Gün', 'Kapıda Vize (30 Gün)')
        }
    },
    {
        'id': 'IL', 'name': 'İsrail', 'nameEn': 'Israel', 'flag': '🇮🇱', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '90 Gün', 'ETA-IL Elektronik İzin'),
            'TR_YESIL': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('evisa', '90 Gün', 'ETA-IL Elektronik İzin')
        }
    },
    {
        'id': 'CN', 'name': 'Çin', 'nameEn': 'China', 'flag': '🇨🇳', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('required', None, 'Konsolosluk Vizesi Gerekli'),
            'TR_YESIL': ('free', '30 Gün', 'İkili Anlaşma ile 30 Gün Vizesiz'),
            'TR_GRI': ('free', '30 Gün', 'İkili Anlaşma ile 30 Gün Vizesiz'),
            'CN': ('free', 'Süresiz', 'Vatandaş'),
            'DE': ('free', '15 Gün', '15 Gün Tek Taraflı Vize Muafiyeti'),
            'FR': ('free', '15 Gün', '15 Gün Tek Taraflı Vize Muafiyeti'),
            'IT': ('free', '15 Gün', '15 Gün Tek Taraflı Vize Muafiyeti'),
            'ES': ('free', '15 Gün', '15 Gün Tek Taraflı Vize Muafiyeti'),
            'SG': ('free', '30 Gün', '30 Gün Vizesiz'),
            'AE': ('free', '30 Gün', '30 Gün Vizesiz'),
            'US': ('required', None, 'Konsolosluk Vizesi'),
            'GB': ('required', None, 'Konsolosluk Vizesi'),
            'CA': ('required', None, 'Konsolosluk Vizesi'),
            'AU': ('free', '15 Gün', '15 Gün Vize Muafiyeti'),
            'KR': ('free', '15 Gün', '15 Gün Vize Muafiyeti'),
            'JP': ('free', '15 Gün', '15 Gün Vize Muafiyeti'),
            'default': ('required', None, 'Konsolosluk Vizesi')
        }
    },
    {
        'id': 'HK', 'name': 'Hong Kong', 'nameEn': 'Hong Kong', 'flag': '🇭🇰', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'CN': ('free', '7 Gün', 'Giriş İzni ile'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'IN', 'name': 'Hindistan', 'nameEn': 'India', 'flag': '🇮🇳', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '30 Gün', 'Online e-Tourist Visa (30 Gün / 1 Yıl)'),
            'TR_YESIL': ('evisa', '30 Gün', 'Online e-Tourist Visa'),
            'TR_GRI': ('evisa', '30 Gün', 'e-Vize'),
            'JP': ('voa', '60 Gün', 'Kapıda Vize / e-Vize'),
            'KR': ('voa', '60 Gün', 'Kapıda Vize / e-Vize'),
            'AE': ('voa', '60 Gün', 'Kapıda Vize / e-Vize'),
            'default': ('evisa', '30 Gün', 'Online e-Tourist Visa')
        }
    },
    {
        'id': 'IR', 'name': 'İran', 'nameEn': 'Iran', 'flag': '🇮🇷', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz (Pasaporta damga vurulmuyor)'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'US': ('required', None, 'Rehber Zorunlu / Özel Vize'),
            'GB': ('required', None, 'Rehber Zorunlu / Özel Vize'),
            'CA': ('required', None, 'Rehber Zorunlu / Özel Vize'),
            'default': ('voa', '30 Gün', 'Kapıda Vize / e-Vize')
        }
    },
    {
        'id': 'KZ', 'name': 'Kazakistan', 'nameEn': 'Kazakhstan', 'flag': '🇰🇿', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_YESIL': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_GRI': ('free', '30 Gün', 'Vizesiz'),
            'RU': ('free', '90 Gün', '90 Gün Vizesiz'),
            'AZ': ('free', '30 Gün', '30 Gün Vizesiz'),
            'default': ('free', '30 Gün', '30 Gün Vizesiz')
        }
    },
    {
        'id': 'UZ', 'name': 'Özbekistan', 'nameEn': 'Uzbekistan', 'flag': '🇺🇿', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_YESIL': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_GRI': ('free', '30 Gün', 'Vizesiz'),
            'RU': ('free', '90 Gün', '90 Gün Vizesiz'),
            'AZ': ('free', '90 Gün', '90 Gün Vizesiz'),
            'default': ('free', '30 Gün', '30 Gün Vizesiz')
        }
    },
    {
        'id': 'KG', 'name': 'Kırgızistan', 'nameEn': 'Kyrgyzstan', 'flag': '🇰🇬', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'RU': ('free', '90 Gün', '90 Gün Vizesiz'),
            'default': ('free', '60 Gün', '60 Gün Vizesiz')
        }
    },
    {
        'id': 'MV', 'name': 'Maldivler', 'nameEn': 'Maldives', 'flag': '🇲🇻', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('voa', '30 Gün', 'Tüm Ülkelere Ücretsiz Kapıda Vize (30 Gün)'),
            'TR_YESIL': ('voa', '30 Gün', 'Ücretsiz Kapıda Vize (30 Gün)'),
            'TR_GRI': ('voa', '30 Gün', 'Kapıda Vize'),
            'default': ('voa', '30 Gün', 'Tüm Ülkelere Ücretsiz Kapıda Vize')
        }
    },
    # Africa
    {
        'id': 'EG', 'name': 'Mısır', 'nameEn': 'Egypt', 'flag': '🇪🇬', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('voa', '30 Gün', 'Kapıda Vize / e-Vize (25 USD - Şarm el-Şeyh vizesiz)'),
            'TR_YESIL': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'İkili Anlaşma ile Vizesiz'),
            'default': ('voa', '30 Gün', 'Kapıda Vize / e-Vize (30 Gün)')
        }
    },
    {
        'id': 'MA', 'name': 'Fas', 'nameEn': 'Morocco', 'flag': '🇲🇦', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz'),
            'AZ': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GE': ('evisa', '30 Gün', 'e-Vize')
        }
    },
    {
        'id': 'TN', 'name': 'Tunus', 'nameEn': 'Tunisia', 'flag': '🇹🇳', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'ZA', 'name': 'Güney Afrika', 'nameEn': 'South Africa', 'flag': '🇿🇦', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('free', '30 Gün', '30 Gün Vizesiz (Kapıda Kaşe)'),
            'TR_YESIL': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_GRI': ('free', '30 Gün', 'Vizesiz'),
            'DE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'FR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'US': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GB': ('free', '90 Gün', '90 Gün Vizesiz'),
            'default': ('free', '30 Gün', 'Vizesiz')
        }
    },
    {
        'id': 'KE', 'name': 'Kenya', 'nameEn': 'Kenya', 'flag': '🇰🇪', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('evisa', '90 Gün', 'Elektronik Seyahat İzni (eTA)'),
            'TR_YESIL': ('evisa', '90 Gün', 'Elektronik Seyahat İzni (eTA)'),
            'TR_GRI': ('evisa', '90 Gün', 'eTA'),
            'default': ('evisa', '90 Gün', 'Elektronik Seyahat İzni (eTA)')
        }
    },
    {
        'id': 'TZ', 'name': 'Tanzanya (Zanzibar)', 'nameEn': 'Tanzania', 'flag': '🇹🇿', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('voa', '90 Gün', 'Kapıda Vize / e-Vize (50 USD)'),
            'TR_YESIL': ('voa', '90 Gün', 'Kapıda Vize / e-Vize (50 USD)'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('voa', '90 Gün', 'Kapıda Vize / e-Vize (50 USD)')
        }
    },
    {
        'id': 'SC', 'name': 'Seyşeller', 'nameEn': 'Seychelles', 'flag': '🇸🇨', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', 'Vizesiz (Online Seyahat Onayı / 90 Gün)'),
            'TR_YESIL': ('free', '90 Gün', 'Vizesiz (Online Seyahat Onayı)'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', 'Vizesiz (Online Seyahat Onayı)')
        }
    },
    {
        'id': 'MU', 'name': 'Mauritius', 'nameEn': 'Mauritius', 'flag': '🇲🇺', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'MG', 'name': 'Madagaskar', 'nameEn': 'Madagascar', 'flag': '🇲🇬', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('voa', '60 Gün', 'Kapıda Vize / e-Vize (60 Gün)'),
            'TR_YESIL': ('voa', '60 Gün', 'Kapıda Vize / e-Vize'),
            'TR_GRI': ('voa', '60 Gün', 'Kapıda Vize'),
            'default': ('voa', '60 Gün', 'Kapıda Vize / e-Vize')
        }
    },
    # Oceania
    {
        'id': 'AU', 'name': 'Avustralya', 'nameEn': 'Australia', 'flag': '🇦🇺', 'continent': 'Okyanusya',
        'rules': {
            'TR_BORDO': ('evisa', '90 Gün', 'Online Ziyaretçi Vizesi (e600)'),
            'TR_YESIL': ('evisa', '90 Gün', 'Online Ziyaretçi Vizesi (e600)'),
            'TR_GRI': ('evisa', '90 Gün', 'Online Vize (e600)'),
            'AU': ('free', 'Süresiz', 'Vatandaş'),
            'DE': ('evisa', '90 Gün', 'eVisitor (Subclass 651)'),
            'FR': ('evisa', '90 Gün', 'eVisitor (Subclass 651)'),
            'IT': ('evisa', '90 Gün', 'eVisitor (Subclass 651)'),
            'ES': ('evisa', '90 Gün', 'eVisitor (Subclass 651)'),
            'GR': ('evisa', '90 Gün', 'eVisitor (Subclass 651)'),
            'GB': ('evisa', '90 Gün', 'eVisitor (Subclass 651)'),
            'US': ('evisa', '90 Gün', 'ETA (Subclass 601)'),
            'CA': ('evisa', '90 Gün', 'ETA (Subclass 601)'),
            'JP': ('evisa', '90 Gün', 'ETA (Subclass 601)'),
            'SG': ('evisa', '90 Gün', 'ETA (Subclass 601)'),
            'KR': ('evisa', '90 Gün', 'ETA (Subclass 601)'),
            'default': ('evisa', '90 Gün', 'Online Vize')
        }
    },
    {
        'id': 'NZ', 'name': 'Yeni Zelanda', 'nameEn': 'New Zealand', 'flag': '🇳🇿', 'continent': 'Okyanusya',
        'rules': {
            'TR_BORDO': ('required', None, 'Ziyaretçi Vizesi Gerekli'),
            'TR_YESIL': ('required', None, 'Vize Gerekli (Yeşil Pasaporta muafiyet yok)'),
            'TR_GRI': ('required', None, 'Vize Gerekli'),
            'AU': ('free', 'Süresiz', 'Süresiz Yaşama ve Çalışma'),
            'DE': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'FR': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'IT': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'ES': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'US': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'GB': ('evisa', '6 Ay', 'NZeTA (6 Ay)'),
            'CA': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'JP': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'SG': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'KR': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
            'default': ('required', None, 'Ziyaretçi Vizesi Gerekli')
        }
    },
    {
        'id': 'FJ', 'name': 'Fiji', 'nameEn': 'Fiji', 'flag': '🇫🇯', 'continent': 'Okyanusya',
        'rules': {
            'TR_BORDO': ('free', '120 Gün', '120 Gün Vizesiz'),
            'TR_YESIL': ('free', '120 Gün', '120 Gün Vizesiz'),
            'TR_GRI': ('free', '120 Gün', 'Vizesiz'),
            'default': ('free', '120 Gün', '120 Gün Vizesiz')
        }
    },
    {
        'id': 'AM', 'name': 'Ermenistan', 'nameEn': 'Armenia', 'flag': '🇦🇲', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '120 Gün', 'e-Vize / Kapıda Vize'),
            'TR_YESIL': ('evisa', '120 Gün', 'e-Vize / Kapıda Vize'),
            'TR_GRI': ('free', '180 Gün', 'Vizesiz'),
            'default': ('free', '180 Gün', '180 Gün Vizesiz')
        }
    },
    {
        'id': 'MN', 'name': 'Moğolistan', 'nameEn': 'Mongolia', 'flag': '🇲🇳', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_YESIL': ('free', '30 Gün', '30 Gün Vizesiz'),
            'TR_GRI': ('free', '30 Gün', 'Vizesiz'),
            'default': ('free', '30 Gün', '30 Gün Vizesiz')
        }
    },
    {
        'id': 'LK', 'name': 'Sri Lanka', 'nameEn': 'Sri Lanka', 'flag': '🇱🇰', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('evisa', '30 Gün', 'Online ETA / Kapıda Vize'),
            'TR_YESIL': ('evisa', '30 Gün', 'Online ETA / Kapıda Vize'),
            'TR_GRI': ('free', '30 Gün', 'Vizesiz'),
            'default': ('evisa', '30 Gün', 'Online ETA / Kapıda Vize')
        }
    },
    {
        'id': 'NP', 'name': 'Nepal', 'nameEn': 'Nepal', 'flag': '🇳🇵', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('voa', '90 Gün', 'Kapıda Vize (Online Başvuru)'),
            'TR_YESIL': ('voa', '90 Gün', 'Kapıda Vize (Online Başvuru)'),
            'TR_GRI': ('voa', '90 Gün', 'Kapıda Vize'),
            'default': ('voa', '90 Gün', 'Kapıda Vize')
        }
    },
    {
        'id': 'TW', 'name': 'Tayvan', 'nameEn': 'Taiwan', 'flag': '🇹🇼', 'continent': 'Asya',
        'rules': {
            'TR_BORDO': ('voa', '30 Gün', 'Havalimanında Ücretsiz Kapıda Vize (30 Gün)'),
            'TR_YESIL': ('voa', '30 Gün', 'Havalimanında Ücretsiz Kapıda Vize (30 Gün)'),
            'TR_GRI': ('voa', '30 Gün', 'Kapıda Vize'),
            'DE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'FR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'IT': ('free', '90 Gün', '90 Gün Vizesiz'),
            'ES': ('free', '90 Gün', '90 Gün Vizesiz'),
            'US': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GB': ('free', '90 Gün', '90 Gün Vizesiz'),
            'JP': ('free', '90 Gün', '90 Gün Vizesiz'),
            'SG': ('free', '30 Gün', '30 Gün Vizesiz'),
            'KR': ('free', '90 Gün', '90 Gün Vizesiz'),
            'default': ('evisa', '30 Gün', 'e-Visa')
        }
    },
    {
        'id': 'UY', 'name': 'Uruguay', 'nameEn': 'Uruguay', 'flag': '🇺🇾', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'PY', 'name': 'Paraguay', 'nameEn': 'Paraguay', 'flag': '🇵🇾', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'EC', 'name': 'Ekvador', 'nameEn': 'Ecuador', 'flag': '🇪🇨', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'BO', 'name': 'Bolivya', 'nameEn': 'Bolivia', 'flag': '🇧🇴', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'US': ('voa', '90 Gün', 'Kapıda Vize (160 USD)'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'JM', 'name': 'Jamaika', 'nameEn': 'Jamaica', 'flag': '🇯🇲', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'BS', 'name': 'Bahamalar', 'nameEn': 'Bahamas', 'flag': '🇧🇸', 'continent': 'Amerika',
        'rules': {
            'TR_BORDO': ('free', '8 Ay', '8 Aya kadar Vizesiz'),
            'TR_YESIL': ('free', '8 Ay', '8 Aya kadar Vizesiz'),
            'TR_GRI': ('free', '8 Ay', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'RW', 'name': 'Ruanda', 'nameEn': 'Rwanda', 'flag': '🇷🇼', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('voa', '30 Gün', 'Kapıda Vize (30 Gün 50 USD)'),
            'TR_YESIL': ('voa', '30 Gün', 'Kapıda Vize (30 Gün)'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('voa', '30 Gün', 'Kapıda Vize')
        }
    },
    {
        'id': 'GH', 'name': 'Gana', 'nameEn': 'Ghana', 'flag': '🇬🇭', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('required', None, 'Konsolosluk Vizesi'),
            'TR_YESIL': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'İkili Anlaşma ile Vizesiz'),
            'default': ('required', None, 'Vize Gerekli')
        }
    },
    {
        'id': 'SN', 'name': 'Senegal', 'nameEn': 'Senegal', 'flag': '🇸🇳', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'),
            'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
            'default': ('free', '90 Gün', '90 Gün Vizesiz')
        }
    },
    {
        'id': 'NA', 'name': 'Namibya', 'nameEn': 'Namibia', 'flag': '🇳🇦', 'continent': 'Afrika',
        'rules': {
            'TR_BORDO': ('voa', '90 Gün', 'Kapıda Vize'),
            'TR_YESIL': ('voa', '90 Gün', 'Kapıda Vize'),
            'TR_GRI': ('voa', '90 Gün', 'Kapıda Vize'),
            'DE': ('free', '90 Gün', '90 Gün Vizesiz'),
            'GB': ('free', '90 Gün', '90 Gün Vizesiz'),
            'US': ('free', '90 Gün', '90 Gün Vizesiz'),
            'default': ('voa', '90 Gün', 'Kapıda Vize')
        }
    }
]

for item in other_countries:
    rules = item['rules']
    visas = {}
    default_rule = rules.get('default', ('required', None, 'Vize Gerekli'))
    for pid in passports:
        if pid in rules:
            status, days, note = rules[pid]
        else:
            status, days, note = default_rule
        visas[pid] = {
            'status': status,
            'days': days,
            'note': note
        }
    destinations.append({
        'id': item['id'],
        'name': item['name'],
        'nameEn': item['nameEn'],
        'flag': item['flag'],
        'continent': item['continent'],
        'isSchengen': False,
        'visas': visas
    })

# Compute stats
stats = {}
for pid in passports:
    free_count = 0
    evisa_count = 0
    voa_count = 0
    required_count = 0
    for d in destinations:
        st = d['visas'].get(pid, {}).get('status', 'required')
        if st == 'free':
            free_count += 1
        elif st == 'evisa':
            evisa_count += 1
        elif st == 'voa':
            voa_count += 1
        elif st == 'required':
            required_count += 1
    
    score = free_count * 1.0 + voa_count * 0.8 + evisa_count * 0.6
    stats[pid] = {
        'free': free_count,
        'evisa': evisa_count,
        'voa': voa_count,
        'required': required_count,
        'total': len(destinations),
        'score': round(score, 1)
    }

dest_file_content = f"export const DESTINATIONS = {json.dumps(destinations, ensure_ascii=False, indent=2)};\n"
stats_file_content = f"export const PASSPORT_STATS = {json.dumps(stats, ensure_ascii=False, indent=2)};\n"

with open('src/data/destinations.js', 'w', encoding='utf-8') as f:
    f.write(dest_file_content)

with open('src/data/stats.js', 'w', encoding='utf-8') as f:
    f.write(stats_file_content)

print(f"Generated destinations.js ({len(destinations)} countries) and stats.js successfully!")

