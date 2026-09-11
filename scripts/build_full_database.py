# -*- coding: utf-8 -*-
import json
import os

passports_info = [
    {'id': 'TR_BORDO', 'name': 'Türkiye (Bordo)', 'fullName': 'Türkiye Cumhuriyeti Umuma Mahsus', 'country': 'Türkiye', 'type': 'Bordo (Umuma Mahsus)', 'flag': '🇹🇷', 'coverColor': '#881337', 'continent': 'Avrupa / Asya'},
    {'id': 'TR_YESIL', 'name': 'Türkiye (Yeşil)', 'fullName': 'Türkiye Cumhuriyeti Hususi Damgalı', 'country': 'Türkiye', 'type': 'Yeşil (Hususi)', 'flag': '🇹🇷', 'coverColor': '#064e3b', 'continent': 'Avrupa / Asya'},
    {'id': 'TR_GRI', 'name': 'Türkiye (Gri)', 'fullName': 'Türkiye Cumhuriyeti Hizmet Pasaportu', 'country': 'Türkiye', 'type': 'Gri (Hizmet)', 'flag': '🇹🇷', 'coverColor': '#334155', 'continent': 'Avrupa / Asya'},
    {'id': 'SG', 'name': 'Singapur', 'fullName': 'Republic of Singapore', 'country': 'Singapur', 'type': 'Standart', 'flag': '🇸🇬', 'coverColor': '#7f1d1d', 'continent': 'Asya'},
    {'id': 'JP', 'name': 'Japonya', 'fullName': 'Japan Passport', 'country': 'Japonya', 'type': 'Standart', 'flag': '🇯🇵', 'coverColor': '#7f1d1d', 'continent': 'Asya'},
    {'id': 'DE', 'name': 'Almanya', 'fullName': 'Bundesrepublik Deutschland', 'country': 'Almanya', 'type': 'Standart (AB)', 'flag': '🇩🇪', 'coverColor': '#451a03', 'continent': 'Avrupa'},
    {'id': 'FR', 'name': 'Fransa', 'fullName': 'République Française', 'country': 'Fransa', 'type': 'Standart (AB)', 'flag': '🇫🇷', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'IT', 'name': 'İtalya', 'fullName': 'Repubblica Italiana', 'country': 'İtalya', 'type': 'Standart (AB)', 'flag': '🇮🇹', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'ES', 'name': 'İspanya', 'fullName': 'Reino de España', 'country': 'İspanya', 'type': 'Standart (AB)', 'flag': '🇪🇸', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'FI', 'name': 'Finlandiya', 'fullName': 'Republic of Finland', 'country': 'Finlandiya', 'type': 'Standart (AB)', 'flag': '🇫🇮', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'SE', 'name': 'İsveç', 'fullName': 'Kingdom of Sweden', 'country': 'İsveç', 'type': 'Standart (AB)', 'flag': '🇸🇪', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'NL', 'name': 'Hollanda', 'fullName': 'Kingdom of the Netherlands', 'country': 'Hollanda', 'type': 'Standart (AB)', 'flag': '🇳🇱', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'DK', 'name': 'Danimarka', 'fullName': 'Kingdom of Denmark', 'country': 'Danimarka', 'type': 'Standart (AB)', 'flag': '🇩🇰', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'IE', 'name': 'İrlanda', 'fullName': 'Republic of Ireland', 'country': 'İrlanda', 'type': 'Standart (AB)', 'flag': '🇮🇪', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'AT', 'name': 'Avusturya', 'fullName': 'Republic of Austria', 'country': 'Avusturya', 'type': 'Standart (AB)', 'flag': '🇦🇹', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'BE', 'name': 'Belçika', 'fullName': 'Kingdom of Belgium', 'country': 'Belçika', 'type': 'Standart (AB)', 'flag': '🇧🇪', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'NO', 'name': 'Norveç', 'fullName': 'Kingdom of Norway', 'country': 'Norveç', 'type': 'Standart', 'flag': '🇳🇴', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'CH', 'name': 'İsviçre', 'fullName': 'Swiss Confederation', 'country': 'İsviçre', 'type': 'Standart', 'flag': '🇨🇭', 'coverColor': '#7f1d1d', 'continent': 'Avrupa'},
    {'id': 'PT', 'name': 'Portekiz', 'fullName': 'Portuguese Republic', 'country': 'Portekiz', 'type': 'Standart (AB)', 'flag': '🇵🇹', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'GB', 'name': 'Birleşik Krallık', 'fullName': 'United Kingdom', 'country': 'Birleşik Krallık', 'type': 'Standart', 'flag': '🇬🇧', 'coverColor': '#1e1b4b', 'continent': 'Avrupa'},
    {'id': 'US', 'name': 'ABD', 'fullName': 'United States of America', 'country': 'ABD', 'type': 'Standart', 'flag': '🇺🇸', 'coverColor': '#172554', 'continent': 'Amerika'},
    {'id': 'CA', 'name': 'Kanada', 'fullName': 'Canada Passport', 'country': 'Kanada', 'type': 'Standart', 'flag': '🇨🇦', 'coverColor': '#1e3a8a', 'continent': 'Amerika'},
    {'id': 'AU', 'name': 'Avustralya', 'fullName': 'Australian Passport', 'country': 'Avustralya', 'type': 'Standart', 'flag': '🇦🇺', 'coverColor': '#1e293b', 'continent': 'Okyanusya'},
    {'id': 'NZ', 'name': 'Yeni Zelanda', 'fullName': 'New Zealand Passport', 'country': 'Yeni Zelanda', 'type': 'Standart', 'flag': '🇳🇿', 'coverColor': '#1e293b', 'continent': 'Okyanusya'},
    {'id': 'KR', 'name': 'Güney Kore', 'fullName': 'Republic of Korea', 'country': 'Güney Kore', 'type': 'Standart', 'flag': '🇰🇷', 'coverColor': '#14532d', 'continent': 'Asya'},
    {'id': 'AE', 'name': 'BAE', 'fullName': 'United Arab Emirates', 'country': 'Birleşik Arap Emirlikleri', 'type': 'Standart', 'flag': '🇦🇪', 'coverColor': '#14532d', 'continent': 'Asya'},
    {'id': 'GR', 'name': 'Yunanistan', 'fullName': 'Hellenic Republic', 'country': 'Yunanistan', 'type': 'Standart (AB)', 'flag': '🇬🇷', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'PL', 'name': 'Polonya', 'fullName': 'Republic of Poland', 'country': 'Polonya', 'type': 'Standart (AB)', 'flag': '🇵🇱', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'CZ', 'name': 'Çekya', 'fullName': 'Czech Republic', 'country': 'Çekya', 'type': 'Standart (AB)', 'flag': '🇨🇿', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'HU', 'name': 'Macaristan', 'fullName': 'Hungary', 'country': 'Macaristan', 'type': 'Standart (AB)', 'flag': '🇭🇺', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'HR', 'name': 'Hırvatistan', 'fullName': 'Republic of Croatia', 'country': 'Hırvatistan', 'type': 'Standart (AB)', 'flag': '🇭🇷', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'RO', 'name': 'Romanya', 'fullName': 'Romania', 'country': 'Romanya', 'type': 'Standart (AB)', 'flag': '🇷🇴', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'BG', 'name': 'Bulgaristan', 'fullName': 'Republic of Bulgaria', 'country': 'Bulgaristan', 'type': 'Standart (AB)', 'flag': '🇧🇬', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'CY', 'name': 'Kıbrıs (GKR)', 'fullName': 'Republic of Cyprus', 'country': 'Kıbrıs', 'type': 'Standart (AB)', 'flag': '🇨🇾', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'CL', 'name': 'Şili', 'fullName': 'Republic of Chile', 'country': 'Şili', 'type': 'Standart', 'flag': '🇨🇱', 'coverColor': '#1e3a8a', 'continent': 'Amerika'},
    {'id': 'AR', 'name': 'Arjantin', 'fullName': 'Argentine Republic', 'country': 'Arjantin', 'type': 'Standart', 'flag': '🇦🇷', 'coverColor': '#172554', 'continent': 'Amerika'},
    {'id': 'BR', 'name': 'Brezilya', 'fullName': 'Federative Republic of Brazil', 'country': 'Brezilya', 'type': 'Standart', 'flag': '🇧🇷', 'coverColor': '#172554', 'continent': 'Amerika'},
    {'id': 'MX', 'name': 'Meksika', 'fullName': 'United Mexican States', 'country': 'Meksika', 'type': 'Standart', 'flag': '🇲🇽', 'coverColor': '#14532d', 'continent': 'Amerika'},
    {'id': 'MY', 'name': 'Malezya', 'fullName': 'Malaysia', 'country': 'Malezya', 'type': 'Standart', 'flag': '🇲🇾', 'coverColor': '#7f1d1d', 'continent': 'Asya'},
    {'id': 'TH', 'name': 'Tayland', 'fullName': 'Kingdom of Thailand', 'country': 'Tayland', 'type': 'Standart', 'flag': '🇹🇭', 'coverColor': '#7f1d1d', 'continent': 'Asya'},
    {'id': 'IL', 'name': 'İsrail', 'fullName': 'State of Israel', 'country': 'İsrail', 'type': 'Standart', 'flag': '🇮🇱', 'coverColor': '#1e3a8a', 'continent': 'Asya'},
    {'id': 'QA', 'name': 'Katar', 'fullName': 'State of Qatar', 'country': 'Katar', 'type': 'Standart', 'flag': '🇶🇦', 'coverColor': '#831843', 'continent': 'Asya'},
    {'id': 'KW', 'name': 'Kuveyt', 'fullName': 'State of Kuwait', 'country': 'Kuveyt', 'type': 'Standart', 'flag': '🇰🇼', 'coverColor': '#172554', 'continent': 'Asya'},
    {'id': 'SA', 'name': 'Suudi Arabistan', 'fullName': 'Kingdom of Saudi Arabia', 'country': 'Suudi Arabistan', 'type': 'Standart', 'flag': '🇸🇦', 'coverColor': '#14532d', 'continent': 'Asya'},
    {'id': 'RS', 'name': 'Sırbistan', 'fullName': 'Republic of Serbia', 'country': 'Sırbistan', 'type': 'Standart', 'flag': '🇷🇸', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'ME', 'name': 'Karadağ', 'fullName': 'Montenegro', 'country': 'Karadağ', 'type': 'Standart', 'flag': '🇲🇪', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'BA', 'name': 'Bosna-Hersek', 'fullName': 'Bosnia and Herzegovina', 'country': 'Bosna-Hersek', 'type': 'Standart', 'flag': '🇧🇦', 'coverColor': '#1e3a8a', 'continent': 'Avrupa'},
    {'id': 'MK', 'name': 'Kuzey Makedonya', 'fullName': 'Republic of North Macedonia', 'country': 'Kuzey Makedonya', 'type': 'Standart', 'flag': '🇲🇰', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'AL', 'name': 'Arnavutluk', 'fullName': 'Republic of Albania', 'country': 'Arnavutluk', 'type': 'Standart', 'flag': '🇦🇱', 'coverColor': '#831843', 'continent': 'Avrupa'},
    {'id': 'GE', 'name': 'Gürcistan', 'fullName': 'Georgia (საქართველო)', 'country': 'Gürcistan', 'type': 'Standart', 'flag': '🇬🇪', 'coverColor': '#1e293b', 'continent': 'Avrupa'},
    {'id': 'UA', 'name': 'Ukrayna', 'fullName': 'Ukraine', 'country': 'Ukrayna', 'type': 'Standart', 'flag': '🇺🇦', 'coverColor': '#172554', 'continent': 'Avrupa'},
    {'id': 'MD', 'name': 'Moldova', 'fullName': 'Republic of Moldova', 'country': 'Moldova', 'type': 'Standart', 'flag': '🇲🇩', 'coverColor': '#1e3a8a', 'continent': 'Avrupa'},
    {'id': 'RU', 'name': 'Rusya', 'fullName': 'Russian Federation', 'country': 'Rusya', 'type': 'Standart', 'flag': '🇷🇺', 'coverColor': '#7f1d1d', 'continent': 'Avrupa'},
    {'id': 'CN', 'name': 'Çin', 'fullName': "People's Republic of China", 'country': 'Çin', 'type': 'Standart', 'flag': '🇨🇳', 'coverColor': '#7f1d1d', 'continent': 'Asya'},
    {'id': 'AZ', 'name': 'Azerbaycan', 'fullName': 'Azərbaycan Respublikası', 'country': 'Azerbaycan', 'type': 'Standart', 'flag': '🇦🇿', 'coverColor': '#065f46', 'continent': 'Asya'},
    {'id': 'ID', 'name': 'Endonezya', 'fullName': 'Republic of Indonesia', 'country': 'Endonezya', 'type': 'Standart', 'flag': '🇮🇩', 'coverColor': '#14532d', 'continent': 'Asya'},
    {'id': 'IN', 'name': 'Hindistan', 'fullName': 'Republic of India', 'country': 'Hindistan', 'type': 'Standart', 'flag': '🇮🇳', 'coverColor': '#1e3a8a', 'continent': 'Asya'},
    {'id': 'ZA', 'name': 'Güney Afrika', 'fullName': 'Republic of South Africa', 'country': 'Güney Afrika', 'type': 'Standart', 'flag': '🇿🇦', 'coverColor': '#14532d', 'continent': 'Afrika'},
    {'id': 'EG', 'name': 'Mısır', 'fullName': 'Arab Republic of Egypt', 'country': 'Mısır', 'type': 'Standart', 'flag': '🇪🇬', 'coverColor': '#14532d', 'continent': 'Afrika'}
]

# Destination countries definitions (196 countries)
schengen_destinations = [
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

eu_passports = {'DE', 'FR', 'IT', 'ES', 'FI', 'SE', 'NL', 'DK', 'IE', 'AT', 'BE', 'PT', 'GR', 'PL', 'CZ', 'HU', 'HR', 'RO', 'BG', 'CY'}
top_tier_passports = {'SG', 'JP', 'KR', 'GB', 'US', 'CA', 'AU', 'NZ', 'CH', 'NO', 'AE', 'CL', 'IL', 'MY'}
balkans_passports = {'RS', 'ME', 'BA', 'MK', 'AL'}

destinations = []

# 1. Add Schengen
for code, name_tr, name_en, flag in schengen_destinations:
    visas = {}
    for p in passports_info:
        pid = p['id']
        if pid == 'TR_BORDO':
            visas[pid] = {'status': 'required', 'days': None, 'note': 'Schengen Vizesi Zorunlu (Konsolosluk)'}
        elif pid in ['TR_YESIL', 'TR_GRI']:
            visas[pid] = {'status': 'free', 'days': '90 Gün', 'note': '180 günde 90 gün Vizesiz'}
        elif pid in eu_passports or pid in ['NO', 'CH']:
            visas[pid] = {'status': 'free', 'days': 'Süresiz', 'note': 'AB / Serbest Dolaşım'}
        elif pid in top_tier_passports or pid in ['GE', 'UA', 'MD', 'BR', 'AR', 'MX']:
            visas[pid] = {'status': 'free', 'days': '90 Gün', 'note': 'Vizesiz (ETIAS 90 Gün)'}
        elif pid in balkans_passports:
            visas[pid] = {'status': 'free', 'days': '90 Gün', 'note': 'Vizesiz (90 Gün)'}
        else:
            visas[pid] = {'status': 'required', 'days': None, 'note': 'Schengen Vizesi Gerekli'}
            
    destinations.append({
        'id': code, 'name': name_tr, 'nameEn': name_en, 'flag': flag,
        'continent': 'Avrupa', 'isSchengen': True, 'visas': visas
    })

# Helper to populate other countries with realistic global access rules
def create_country(cid, name_tr, name_en, flag, continent, special_rules, default_type='required'):
    visas = {}
    for p in passports_info:
        pid = p['id']
        
        # 1. Explicit passport rule
        if pid in special_rules:
            st, days, note = special_rules[pid]
        # 2. Turkey specific rule (Bordo, Yeşil, Gri)
        elif 'tr' in special_rules and pid.startswith('TR_'):
            st, days, note = special_rules['tr']
        # 3. EU passports rule
        elif 'eu' in special_rules and (pid in eu_passports or pid in ['CH', 'NO']):
            st, days, note = special_rules['eu']
        # 4. Top tier passports rule (SG, JP, DE, FR, US, GB, etc.)
        elif 'top' in special_rules and pid in top_tier_passports:
            st, days, note = special_rules['top']
        # 5. Fallback rule based on continent/real-world norms for Western / Global Passports:
        elif pid in top_tier_passports or pid in eu_passports:
            if continent in ['Amerika', 'Okyanusya']:
                # Most Americas & Pacific islands give 90 days visa-free to EU / US / JP / SG
                st, days, note = ('free', '90 Gün', '90 Gün Vizesiz')
            elif continent == 'Asya':
                # Most Asian countries give visa-free or e-visa/voa
                if default_type == 'required':
                    st, days, note = ('evisa', '30 Gün', 'Online e-Vize')
                else:
                    st, days, note = ('free', '30-90 Gün', 'Vizesiz')
            elif continent == 'Afrika':
                if default_type == 'free':
                    st, days, note = ('free', '90 Gün', 'Vizesiz')
                else:
                    st, days, note = ('voa', '30 Gün', 'Kapıda Vize / e-Vize')
            else:
                st, days, note = ('free', '90 Gün', 'Vizesiz')
        elif 'default' in special_rules:
            st, days, note = special_rules['default']
        else:
            if default_type == 'free':
                st, days, note = ('free', '90 Gün', '90 Gün Vizesiz')
            elif default_type == 'evisa':
                st, days, note = ('evisa', '30 Gün', 'Online e-Vize')
            elif default_type == 'voa':
                st, days, note = ('voa', '30 Gün', 'Kapıda Vize')
            else:
                st, days, note = ('required', None, 'Vize Gerekli')
                
        visas[pid] = {'status': st, 'days': days, 'note': note}
    
    return {
        'id': cid, 'name': name_tr, 'nameEn': name_en, 'flag': flag,
        'continent': continent, 'isSchengen': False, 'visas': visas
    }


# All other world countries
all_world_list = [
    # Non-Schengen Europe
    ('GB', 'Birleşik Krallık', 'United Kingdom', '🇬🇧', 'Avrupa', {
        'TR_BORDO': ('required', None, 'Standart Ziyaretçi Vizesi'),
        'TR_YESIL': ('required', None, 'Vize Gerekli (Yeşil Pasaporta muafiyet yok)'),
        'TR_GRI': ('required', None, 'Vize Gerekli'),
        'GB': ('free', 'Süresiz', 'Vatandaş'),
        'IE': ('free', 'Süresiz', 'Ortak Seyahat Alanı (CTA)'),
        'eu': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
        'top': ('free', '6 Ay', 'ETA / 6 Ay Vizesiz'),
        'default': ('required', None, 'Ziyaretçi Vizesi Gerekli')
    }),
    ('IE', 'İrlanda', 'Ireland', '🇮🇪', 'Avrupa', {
        'TR_BORDO': ('required', None, 'İrlanda Turist Vizesi'),
        'TR_YESIL': ('required', None, 'Vize Gerekli (Yeşil Pasaporta muafiyet yok)'),
        'TR_GRI': ('required', None, 'Vize Gerekli'),
        'GB': ('free', 'Süresiz', 'CTA'), 'eu': ('free', 'Süresiz', 'AB'), 'top': ('free', '90 Gün', 'Vizesiz'),
        'default': ('required', None, 'Vize Gerekli')
    }),
    ('TRNC', 'Kuzey Kıbrıs (KKTC)', 'Northern Cyprus', '🇹🇷', 'Avrupa', {
        'tr': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('CY', 'Güney Kıbrıs', 'Cyprus', '🇨🇾', 'Avrupa', {
        'tr': ('required', None, 'Vize Gerekli'),
        'eu': ('free', 'Süresiz', 'AB'), 'top': ('free', '90 Gün', 'Vizesiz'),
        'default': ('required', None, 'Vize Gerekli')
    }),
    ('BA', 'Bosna-Hersek', 'Bosnia and Herzegovina', '🇧🇦', 'Avrupa', {
        'tr': ('free', '90 Gün', 'Çipli Kimlik Kartı / Pasaportla Vizesiz'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('RS', 'Sırbistan', 'Serbia', '🇷🇸', 'Avrupa', {
        'tr': ('free', '90 Gün', 'Çipli Kimlik Kartı / Pasaportla Vizesiz'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('ME', 'Karadağ', 'Montenegro', '🇲🇪', 'Avrupa', {
        'tr': ('free', '90 Gün', '180 günde 90 gün Vizesiz'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('AL', 'Arnavutluk', 'Albania', '🇦🇱', 'Avrupa', {
        'tr': ('free', '90 Gün', '90 Gün Vizesiz'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('MK', 'Kuzey Makedonya', 'North Macedonia', '🇲🇰', 'Avrupa', {
        'tr': ('free', '90 Gün', '90 Gün Vizesiz'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('XK', 'Kosova', 'Kosovo', '🇽🇰', 'Avrupa', {
        'tr': ('free', '90 Gün', '90 Gün Vizesiz'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('MD', 'Moldova', 'Moldova', '🇲🇩', 'Avrupa', {
        'tr': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('UA', 'Ukrayna', 'Ukraine', '🇺🇦', 'Avrupa', {
        'tr': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş Mümkün'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('GE', 'Gürcistan', 'Georgia', '🇬🇪', 'Avrupa', {
        'tr': ('free', '1 Yıl', 'Çipli Kimlik Kartı ile Giriş (1 Yıl)'),
        'default': ('free', '1 Yıl', '1 Yıl Vizesiz')
    }),
    ('AZ', 'Azerbaycan', 'Azerbaijan', '🇦🇿', 'Asya', {
        'tr': ('free', '90 Gün', 'Çipli Kimlik Kartı ile Giriş (90 Gün)'),
        'RU': ('free', '90 Gün', '90 Gün Vizesiz'), 'GE': ('free', '90 Gün', '90 Gün Vizesiz'),
        'default': ('evisa', '30 Gün', 'ASAN e-Vize')
    }),
    ('AM', 'Ermenistan', 'Armenia', '🇦🇲', 'Asya', {
        'TR_BORDO': ('evisa', '120 Gün', 'e-Vize / Kapıda Vize'),
        'TR_YESIL': ('evisa', '120 Gün', 'e-Vize / Kapıda Vize'),
        'default': ('free', '180 Gün', '180 Gün Vizesiz')
    }),
    ('RU', 'Rusya', 'Russia', '🇷🇺', 'Avrupa', {
        'TR_BORDO': ('evisa', '16 Gün', 'Elektronik Vize (16 Gün)'),
        'TR_YESIL': ('free', '30 Gün', 'İkili Anlaşma ile 30 Gün Vizesiz'),
        'TR_GRI': ('free', '30 Gün', 'İkili Anlaşma ile 30 Gün Vizesiz'),
        'AZ': ('free', '90 Gün', 'Vizesiz'), 'GE': ('free', '90 Gün', 'Vizesiz'),
        'CN': ('free', '15 Gün', 'Vizesiz'), 'AE': ('free', '90 Gün', 'Vizesiz'),
        'US': ('required', None, 'Vize'), 'GB': ('required', None, 'Vize'),
        'default': ('evisa', '16 Gün', 'Elektronik Vize')
    }),
    ('BY', 'Belarus', 'Belarus', '🇧🇾', 'Avrupa', {
        'tr': ('free', '30 Gün', '30 Gün Vizesiz'),
        'RU': ('free', 'Süresiz', 'Serbest'), 'default': ('free', '30 Gün', 'Minsk Havalimanından')
    }),
    ('AD', 'Andorra', 'Andorra', '🇦🇩', 'Avrupa', {'tr': ('free', '90 Gün', 'Vizesiz (Fransa/İspanya transit)'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('MC', 'Monako', 'Monaco', '🇲🇨', 'Avrupa', {'tr': ('free', '90 Gün', 'Vizesiz (Fransa transit)'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('SM', 'San Marino', 'San Marino', '🇸🇲', 'Avrupa', {'tr': ('free', '90 Gün', 'Vizesiz (İtalya transit)'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('VA', 'Vatikan', 'Vatican City', '🇻🇦', 'Avrupa', {'tr': ('free', '90 Gün', 'Vizesiz (İtalya transit)'), 'default': ('free', '90 Gün', 'Vizesiz')}),

    # Americas
    ('US', 'Amerika Birleşik Devletleri', 'United States', '🇺🇸', 'Amerika', {
        'TR_BORDO': ('required', None, 'B1/B2 Konsolosluk Vizesi'),
        'TR_YESIL': ('required', None, 'Vize Gerekli (Yeşil Pasaporta muafiyet yok)'),
        'TR_GRI': ('required', None, 'Vize Gerekli'),
        'US': ('free', 'Süresiz', 'Vatandaş'), 'CA': ('free', '6 Ay', 'Vizesiz'),
        'eu': ('evisa', '90 Gün', 'ESTA İzni'), 'top': ('evisa', '90 Gün', 'ESTA İzni'),
        'default': ('required', None, 'Konsolosluk Vizesi Gerekli')
    }),
    ('CA', 'Kanada', 'Canada', '🇨🇦', 'Amerika', {
        'tr': ('required', None, 'Kanada Ziyaretçi Vizesi Gerekli'),
        'US': ('free', '6 Ay', 'Vizesiz'), 'CA': ('free', 'Süresiz', 'Vatandaş'),
        'eu': ('evisa', '6 Ay', 'eTA Elektronik Seyahat İzni'), 'top': ('evisa', '6 Ay', 'eTA İzni'),
        'default': ('required', None, 'Ziyaretçi Vizesi Gerekli')
    }),
    ('MX', 'Meksika', 'Mexico', '🇲🇽', 'Amerika', {
        'TR_BORDO': ('evisa', '180 Gün', 'Elektronik Onay (SAE)'),
        'TR_YESIL': ('evisa', '180 Gün', 'SAE / Schengen-ABD Vizesiyle Vizesiz'),
        'TR_GRI': ('evisa', '180 Gün', 'SAE'),
        'US': ('free', '180 Gün', 'Vizesiz'), 'CA': ('free', '180 Gün', 'Vizesiz'),
        'eu': ('free', '180 Gün', 'Vizesiz'), 'top': ('free', '180 Gün', 'Vizesiz'),
        'default': ('free', '180 Gün', '180 Gün Vizesiz')
    }),
    ('BR', 'Brezilya', 'Brazil', '🇧🇷', 'Amerika', {
        'tr': ('free', '90 Gün', '90 Gün Vizesiz'),
        'eu': ('free', '90 Gün', 'Vizesiz'), 'US': ('evisa', '90 Gün', 'e-Visa'),
        'CA': ('evisa', '90 Gün', 'e-Visa'), 'AU': ('evisa', '90 Gün', 'e-Visa'),
        'default': ('free', '90 Gün', '90 Gün Vizesiz')
    }),
    ('AR', 'Arjantin', 'Argentina', '🇦🇷', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('CL', 'Şili', 'Chile', '🇨🇱', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('CO', 'Kolombiya', 'Colombia', '🇨🇴', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('PE', 'Peru', 'Peru', '🇵🇪', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('UY', 'Uruguay', 'Uruguay', '🇺🇾', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('PY', 'Paraguay', 'Paraguay', '🇵🇾', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('EC', 'Ekvador', 'Ecuador', '🇪🇨', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('BO', 'Bolivya', 'Bolivia', '🇧🇴', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'US': ('voa', '90 Gün', 'Kapıda Vize'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('VE', 'Venezuela', 'Venezuela', '🇻🇪', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('GY', 'Guyana', 'Guyana', '🇬🇾', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('SR', 'Surinam', 'Suriname', '🇸🇷', 'Amerika', {'tr': ('evisa', '90 Gün', 'Giriş Ücreti (E-Fee)'), 'default': ('evisa', '90 Gün', 'E-Fee')}),
    ('CR', 'Kosta Rika', 'Costa Rica', '🇨🇷', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('PA', 'Panama', 'Panama', '🇵🇦', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('BZ', 'Belize', 'Belize', '🇧🇿', 'Amerika', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),
    ('GT', 'Guatemala', 'Guatemala', '🇬🇹', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('HN', 'Honduras', 'Honduras', '🇭🇳', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('SV', 'El Salvador', 'El Salvador', '🇸🇻', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz (12 USD Kart)'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('NI', 'Nikaragua', 'Nicaragua', '🇳🇮', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz (10 USD Kart)'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('CU', 'Küba', 'Cuba', '🇨🇺', 'Amerika', {
        'TR_BORDO': ('evisa', '90 Gün', 'Elektronik Turist Kartı (eVisa)'),
        'TR_YESIL': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
        'TR_GRI': ('free', '90 Gün', 'İkili Anlaşma ile Vizesiz'),
        'default': ('evisa', '90 Gün', 'Turist Kartı')
    }),
    ('DO', 'Dominik Cumhuriyeti', 'Dominican Republic', '🇩🇴', 'Amerika', {'tr': ('evisa', '30 Gün', 'E-Ticket Giriş Formu'), 'default': ('evisa', '30 Gün', 'E-Ticket')}),
    ('HT', 'Haiti', 'Haiti', '🇭🇹', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('JM', 'Jamaika', 'Jamaica', '🇯🇲', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('BS', 'Bahamalar', 'Bahamas', '🇧🇸', 'Amerika', {'tr': ('free', '8 Ay', '8 Aya kadar Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('BB', 'Barbados', 'Barbados', '🇧🇧', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('TT', 'Trinidad ve Tobago', 'Trinidad and Tobago', '🇹🇹', 'Amerika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('AG', 'Antigua ve Barbuda', 'Antigua and Barbuda', '🇦🇬', 'Amerika', {'tr': ('free', '180 Gün', 'Vizesiz'), 'default': ('free', '180 Gün', 'Vizesiz')}),
    ('DM', 'Dominika', 'Dominica', '🇩🇲', 'Amerika', {'tr': ('free', '21 Gün', 'Vizesiz'), 'default': ('free', '21 Gün', 'Vizesiz')}),
    ('GD', 'Grenada', 'Grenada', '🇬🇩', 'Amerika', {'tr': ('free', '90 Gün', 'Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('KN', 'Saint Kitts ve Nevis', 'Saint Kitts and Nevis', '🇰🇳', 'Amerika', {'tr': ('free', '90 Gün', 'Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('LC', 'Saint Lucia', 'Saint Lucia', '🇱🇨', 'Amerika', {'tr': ('free', '42 Gün', 'Vizesiz'), 'default': ('free', '42 Gün', 'Vizesiz')}),
    ('VC', 'Saint Vincent', 'Saint Vincent', '🇻🇨', 'Amerika', {'tr': ('free', '30 Gün', 'Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),

    # Asia & Middle East
    ('JP', 'Japonya', 'Japan', '🇯🇵', 'Asya', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'JP': ('free', 'Süresiz', 'Vatandaş'), 'eu': ('free', '90 Gün', 'Vizesiz'), 'top': ('free', '90 Gün', 'Vizesiz'), 'default': ('required', None, 'Vize Gerekli')}),
    ('KR', 'Güney Kore', 'South Korea', '🇰🇷', 'Asya', {'tr': ('evisa', '90 Gün', 'K-ETA İzni (90 Gün)'), 'KR': ('free', 'Süresiz', 'Vatandaş'), 'eu': ('free', '90 Gün', 'K-ETA Muafiyeti'), 'top': ('free', '90 Gün', 'Vizesiz'), 'default': ('evisa', '90 Gün', 'K-ETA')}),
    ('SG', 'Singapur', 'Singapore', '🇸🇬', 'Asya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'SG': ('free', 'Süresiz', 'Vatandaş'), 'eu': ('free', '90 Gün', 'Vizesiz'), 'top': ('free', '90 Gün', 'Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),
    ('TH', 'Tayland', 'Thailand', '🇹🇭', 'Asya', {'tr': ('free', '60 Gün', '60 Gün Vizesiz'), 'eu': ('free', '60 Gün', 'Vizesiz'), 'top': ('free', '60 Gün', 'Vizesiz'), 'default': ('free', '60 Gün', 'Vizesiz')}),
    ('MY', 'Malezya', 'Malaysia', '🇲🇾', 'Asya', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('ID', 'Endonezya', 'Indonesia', '🇮🇩', 'Asya', {'tr': ('voa', '30 Gün', 'Kapıda Vize / e-VoA'), 'SG': ('free', '30 Gün', 'Vizesiz'), 'MY': ('free', '30 Gün', 'Vizesiz'), 'default': ('voa', '30 Gün', 'Kapıda Vize / e-VoA')}),
    ('VN', 'Vietnam', 'Vietnam', '🇻🇳', 'Asya', {'TR_BORDO': ('evisa', '90 Gün', 'e-Visa 90 Gün'), 'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'), 'TR_GRI': ('free', '90 Gün', 'Vizesiz'), 'eu': ('free', '45 Gün', 'Vizesiz'), 'top': ('free', '45 Gün', 'Vizesiz'), 'default': ('evisa', '90 Gün', 'e-Visa')}),
    ('PH', 'Filipinler', 'Philippines', '🇵🇭', 'Asya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),
    ('AE', 'Birleşik Arap Emirlikleri', 'United Arab Emirates', '🇦🇪', 'Asya', {
        'TR_BORDO': ('evisa', '30 Gün', 'Online e-Vize Gerekli'),
        'TR_YESIL': ('free', '90 Gün', '180 Günde 90 Gün Vizesiz'),
        'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
        'AE': ('free', 'Süresiz', 'Vatandaş'), 'eu': ('free', '90 Gün', 'Kapıda Kaşe'), 'top': ('free', '30 Gün', 'Kapıda Kaşe'),
        'AZ': ('free', '90 Gün', 'Vizesiz'), 'GE': ('free', '90 Gün', 'Vizesiz'), 'RU': ('free', '90 Gün', 'Vizesiz'),
        'default': ('evisa', '30 Gün', 'e-Vize')
    }),
    ('SA', 'Suudi Arabistan', 'Saudi Arabia', '🇸🇦', 'Asya', {'tr': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'), 'AE': ('free', 'Süresiz', 'Körfez'), 'eu': ('evisa', '90 Gün', 'e-Vize'), 'top': ('evisa', '90 Gün', 'e-Vize'), 'default': ('evisa', '90 Gün', 'e-Vize')}),
    ('QA', 'Katar', 'Qatar', '🇶🇦', 'Asya', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'AE': ('free', 'Süresiz', 'Körfez'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('OM', 'Umman', 'Oman', '🇴🇲', 'Asya', {'tr': ('free', '14 Gün', '14 Gün Vizesiz'), 'AE': ('free', 'Süresiz', 'Körfez'), 'default': ('free', '14 Gün', 'Vizesiz')}),
    ('BH', 'Bahreyn', 'Bahrain', '🇧🇭', 'Asya', {'tr': ('evisa', '14 Gün', 'e-Vize / Kapıda Vize'), 'AE': ('free', 'Süresiz', 'Körfez'), 'default': ('evisa', '14 Gün', 'e-Vize')}),
    ('KW', 'Kuveyt', 'Kuwait', '🇰🇼', 'Asya', {'TR_BORDO': ('evisa', '90 Gün', 'e-Vize / Kapıda Vize'), 'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'), 'TR_GRI': ('free', '90 Gün', 'Vizesiz'), 'AE': ('free', 'Süresiz', 'Körfez'), 'default': ('evisa', '90 Gün', 'e-Vize')}),
    ('JO', 'Ürdün', 'Jordan', '🇯🇴', 'Asya', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('voa', '30 Gün', 'Kapıda Vize')}),
    ('LB', 'Lübnan', 'Lebanon', '🇱🇧', 'Asya', {'tr': ('voa', '90 Gün', 'Kapıda Vize (Ücretsiz)'), 'default': ('voa', '30 Gün', 'Kapıda Vize')}),
    ('IL', 'İsrail', 'Israel', '🇮🇱', 'Asya', {'TR_BORDO': ('evisa', '90 Gün', 'ETA-IL Elektronik İzin'), 'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'), 'TR_GRI': ('free', '90 Gün', 'Vizesiz'), 'default': ('evisa', '90 Gün', 'ETA-IL')}),
    ('CN', 'Çin', 'China', '🇨🇳', 'Asya', {
        'TR_BORDO': ('required', None, 'Konsolosluk Vizesi Gerekli'),
        'TR_YESIL': ('free', '30 Gün', 'İkili Anlaşma ile 30 Gün Vizesiz'),
        'TR_GRI': ('free', '30 Gün', '30 Gün Vizesiz'),
        'CN': ('free', 'Süresiz', 'Vatandaş'),
        'DE': ('free', '15 Gün', '15 Gün Tek Taraflı Muafiyet'), 'FR': ('free', '15 Gün', '15 Gün Muafiyet'),
        'IT': ('free', '15 Gün', '15 Gün Muafiyet'), 'ES': ('free', '15 Gün', '15 Gün Muafiyet'),
        'SG': ('free', '30 Gün', '30 Gün Vizesiz'), 'AE': ('free', '30 Gün', '30 Gün Vizesiz'),
        'default': ('required', None, 'Konsolosluk Vizesi')
    }),
    ('HK', 'Hong Kong', 'Hong Kong', '🇭🇰', 'Asya', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('MO', 'Makao', 'Macao', '🇲🇴', 'Asya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('TW', 'Tayvan', 'Taiwan', '🇹🇼', 'Asya', {'tr': ('voa', '30 Gün', 'Havalimanında Ücretsiz Kapıda Vize'), 'eu': ('free', '90 Gün', 'Vizesiz'), 'top': ('free', '90 Gün', 'Vizesiz'), 'default': ('evisa', '30 Gün', 'e-Visa')}),
    ('IN', 'Hindistan', 'India', '🇮🇳', 'Asya', {'tr': ('evisa', '30 Gün', 'Online e-Tourist Visa'), 'JP': ('voa', '60 Gün', 'Kapıda Vize'), 'KR': ('voa', '60 Gün', 'Kapıda Vize'), 'AE': ('voa', '60 Gün', 'Kapıda Vize'), 'default': ('evisa', '30 Gün', 'Online e-Tourist Visa')}),
    ('PK', 'Pakistan', 'Pakistan', '🇵🇰', 'Asya', {'tr': ('evisa', '90 Gün', 'Online e-Visa'), 'default': ('evisa', '90 Gün', 'Online e-Visa')}),
    ('BD', 'Bangladeş', 'Bangladesh', '🇧🇩', 'Asya', {'tr': ('voa', '30 Gün', 'Kapıda Vize (50 USD)'), 'default': ('voa', '30 Gün', 'Kapıda Vize')}),
    ('LK', 'Sri Lanka', 'Sri Lanka', '🇱🇰', 'Asya', {'tr': ('evisa', '30 Gün', 'Online ETA / Kapıda Vize'), 'default': ('evisa', '30 Gün', 'Online ETA')}),
    ('NP', 'Nepal', 'Nepal', '🇳🇵', 'Asya', {'tr': ('voa', '90 Gün', 'Kapıda Vize'), 'default': ('voa', '90 Gün', 'Kapıda Vize')}),
    ('BT', 'Butan', 'Bhutan', '🇧🇹', 'Asya', {'default': ('evisa', '30 Gün', 'e-Vize (Günlük 100 USD Sürdürülebilirlik Harcı)')}),
    ('MV', 'Maldivler', 'Maldives', '🇲🇻', 'Asya', {'default': ('voa', '30 Gün', 'Tüm Dünyaya Ücretsiz Kapıda Vize')}),
    ('MM', 'Myanmar', 'Myanmar', '🇲🇲', 'Asya', {'default': ('evisa', '28 Gün', 'Online e-Visa')}),
    ('KH', 'Kamboçya', 'Cambodia', '🇰🇭', 'Asya', {'default': ('voa', '30 Gün', 'Kapıda Vize / e-Vize (30 USD)')}),
    ('LA', 'Laos', 'Laos', '🇱🇦', 'Asya', {'default': ('voa', '30 Gün', 'Kapıda Vize / e-Vize')}),
    ('BN', 'Brunei', 'Brunei', '🇧🇳', 'Asya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('TL', 'Doğu Timor', 'Timor-Leste', '🇹🇱', 'Asya', {'default': ('voa', '30 Gün', 'Kapıda Vize (30 USD)')}),
    ('IR', 'İran', 'Iran', '🇮🇷', 'Asya', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'US': ('required', None, 'Rehber Zorunlu'), 'GB': ('required', None, 'Rehber Zorunlu'), 'default': ('voa', '30 Gün', 'Kapıda Vize / e-Vize')}),
    ('IQ', 'Irak', 'Iraq', '🇮🇶', 'Asya', {'TR_BORDO': ('voa', '60 Gün', 'Havalimanında Kapıda Vize'), 'TR_YESIL': ('voa', '60 Gün', 'Kapıda Vize'), 'default': ('voa', '60 Gün', 'Kapıda Vize')}),
    ('SY', 'Suriye', 'Syria', '🇸🇾', 'Asya', {'default': ('required', None, 'Konsolosluk Vizesi / Güvenlik Onayı')}),
    ('YE', 'Yemen', 'Yemen', '🇾🇪', 'Asya', {'default': ('required', None, 'Vize Gerekli')}),
    ('AF', 'Afganistan', 'Afghanistan', '🇦🇫', 'Asya', {'default': ('required', None, 'Vize Gerekli')}),
    ('PS', 'Filistin', 'Palestine', '🇵🇸', 'Asya', {'tr': ('free', '90 Gün', 'Vizesiz (İsrail kontrol noktasından)'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('KZ', 'Kazakistan', 'Kazakhstan', '🇰🇿', 'Asya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),
    ('UZ', 'Özbekistan', 'Uzbekistan', '🇺🇿', 'Asya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),
    ('KG', 'Kırgızistan', 'Kyrgyzstan', '🇰🇬', 'Asya', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '60 Gün', 'Vizesiz')}),
    ('TJ', 'Tacikistan', 'Tajikistan', '🇹🇯', 'Asya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),
    ('TM', 'Türkmenistan', 'Turkmenistan', '🇹🇲', 'Asya', {'default': ('required', None, 'Davetiye ve Vize Zorunlu')}),
    ('MN', 'Moğolistan', 'Mongolia', '🇲🇳', 'Asya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),

    # Africa
    ('EG', 'Mısır', 'Egypt', '🇪🇬', 'Afrika', {
        'TR_BORDO': ('voa', '30 Gün', 'Kapıda Vize / e-Vize (25 USD - Şarm vizesiz)'),
        'TR_YESIL': ('free', '90 Gün', 'İkili Anlaşma ile 90 Gün Vizesiz'),
        'TR_GRI': ('free', '90 Gün', 'Vizesiz'),
        'default': ('voa', '30 Gün', 'Kapıda Vize / e-Vize')
    }),
    ('MA', 'Fas', 'Morocco', '🇲🇦', 'Afrika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('TN', 'Tunus', 'Tunisia', '🇹🇳', 'Afrika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('DZ', 'Cezayir', 'Algeria', '🇩🇿', 'Afrika', {'TR_BORDO': ('required', None, 'Vize Gerekli'), 'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'), 'TR_GRI': ('free', '90 Gün', 'Vizesiz'), 'default': ('required', None, 'Konsolosluk Vizesi')}),
    ('LY', 'Libya', 'Libya', '🇱🇾', 'Afrika', {'TR_BORDO': ('required', None, 'e-Vize Gerekli'), 'TR_YESIL': ('free', '90 Gün', 'Vizesiz'), 'TR_GRI': ('free', '90 Gün', 'Vizesiz'), 'default': ('required', None, 'e-Vize')}),
    ('SD', 'Sudan', 'Sudan', '🇸🇩', 'Afrika', {'tr': ('voa', '30 Gün', 'Kapıda Vize'), 'default': ('required', None, 'Vize')}),
    ('SS', 'Güney Sudan', 'South Sudan', '🇸🇸', 'Afrika', {'default': ('evisa', '30 Gün', 'Online e-Visa')}),
    ('ET', 'Etiyopya', 'Ethiopia', '🇪🇹', 'Afrika', {'default': ('evisa', '90 Gün', 'Online e-Visa')}),
    ('KE', 'Kenya', 'Kenya', '🇰🇪', 'Afrika', {'default': ('evisa', '90 Gün', 'Elektronik Seyahat İzni (eTA)')}),
    ('TZ', 'Tanzanya (Zanzibar)', 'Tanzania', '🇹🇿', 'Afrika', {'tr': ('voa', '90 Gün', 'Kapıda Vize / e-Vize (50 USD)'), 'default': ('voa', '90 Gün', 'Kapıda Vize')}),
    ('UG', 'Uganda', 'Uganda', '🇺🇬', 'Afrika', {'default': ('evisa', '90 Gün', 'Online e-Visa (50 USD)')}),
    ('RW', 'Ruanda', 'Rwanda', '🇷🇼', 'Afrika', {'default': ('voa', '30 Gün', 'Kapıda Vize (50 USD)')}),
    ('BI', 'Burundi', 'Burundi', '🇧🇮', 'Afrika', {'default': ('voa', '30 Gün', 'Kapıda Vize')}),
    ('SO', 'Somali', 'Somalia', '🇸🇴', 'Afrika', {'default': ('voa', '30 Gün', 'Kapıda Vize')}),
    ('DJ', 'Cibuti', 'Djibouti', '🇩🇯', 'Afrika', {'default': ('evisa', '31 Gün', 'Online e-Visa')}),
    ('ER', 'Eritre', 'Eritrea', '🇪🇷', 'Afrika', {'default': ('required', None, 'Vize Gerekli')}),
    ('SC', 'Seyşeller', 'Seychelles', '🇸🇨', 'Afrika', {'default': ('free', '90 Gün', 'Vizesiz (Online Seyahat Onayı)')}),
    ('MU', 'Mauritius', 'Mauritius', '🇲🇺', 'Afrika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('MG', 'Madagaskar', 'Madagascar', '🇲🇬', 'Afrika', {'default': ('voa', '60 Gün', 'Kapıda Vize / e-Vize')}),
    ('KM', 'Komorlar', 'Comoros', '🇰🇲', 'Afrika', {'default': ('voa', '45 Gün', 'Kapıda Vize (30 EUR)')}),
    ('ZA', 'Güney Afrika', 'South Africa', '🇿🇦', 'Afrika', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'eu': ('free', '90 Gün', 'Vizesiz'), 'top': ('free', '90 Gün', 'Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),
    ('NA', 'Namibya', 'Namibia', '🇳🇦', 'Afrika', {'tr': ('voa', '90 Gün', 'Kapıda Vize'), 'default': ('voa', '90 Gün', 'Kapıda Vize')}),
    ('BW', 'Botsvana', 'Botswana', '🇧🇼', 'Afrika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('ZW', 'Zimbabve', 'Zimbabwe', '🇿🇼', 'Afrika', {'default': ('voa', '30 Gün', 'Kapıda Vize (30 USD)')}),
    ('ZM', 'Zambiya', 'Zambia', '🇿🇲', 'Afrika', {'default': ('free', '90 Gün', 'Turizm Vize Muafiyeti')}),
    ('MZ', 'Mozambik', 'Mozambique', '🇲🇿', 'Afrika', {'default': ('evisa', '30 Gün', 'Online e-Visa')}),
    ('AO', 'Angola', 'Angola', '🇦🇴', 'Afrika', {'default': ('free', '30 Gün', 'Turizm Vizesiz (Yılda 90 Gün)')}),
    ('MW', 'Malavi', 'Malawi', '🇲🇼', 'Afrika', {'default': ('free', '90 Gün', 'Vize Muafiyeti (2024)')}),
    ('LS', 'Lesotho', 'Lesotho', '🇱🇸', 'Afrika', {'default': ('evisa', '44 Gün', 'Online e-Visa')}),
    ('SZ', 'Esvatini', 'Eswatini', '🇸🇿', 'Afrika', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '30 Gün', 'Vizesiz')}),
    ('NG', 'Nijerya', 'Nigeria', '🇳🇬', 'Afrika', {'default': ('evisa', '30 Gün', 'Online e-Visa / VoA')}),
    ('GH', 'Gana', 'Ghana', '🇬🇭', 'Afrika', {'TR_BORDO': ('required', None, 'Konsolosluk Vizesi'), 'TR_YESIL': ('free', '90 Gün', '90 Gün Vizesiz'), 'TR_GRI': ('free', '90 Gün', 'Vizesiz'), 'default': ('required', None, 'Vize')}),
    ('SN', 'Senegal', 'Senegal', '🇸🇳', 'Afrika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('CI', 'Fildişi Sahili', 'Ivory Coast', '🇨🇮', 'Afrika', {'TR_BORDO': ('evisa', '90 Gün', 'e-Visa'), 'TR_YESIL': ('free', '90 Gün', 'Vizesiz'), 'default': ('evisa', '90 Gün', 'e-Visa')}),
    ('CM', 'Kamerun', 'Cameroon', '🇨🇲', 'Afrika', {'default': ('evisa', '90 Gün', 'Online e-Visa')}),
    ('GA', 'Gabon', 'Gabon', '🇬🇦', 'Afrika', {'default': ('evisa', '90 Gün', 'Online e-Visa')}),
    ('CG', 'Kongo Cumhuriyeti', 'Republic of the Congo', '🇨🇬', 'Afrika', {'default': ('required', None, 'Vize Gerekli')}),
    ('CD', 'Demokratik Kongo', 'DR Congo', '🇨🇩', 'Afrika', {'default': ('evisa', '30 Gün', 'Online e-Visa')}),
    ('CF', 'Orta Afrika Cumhuriyeti', 'Central African Republic', '🇨🇫', 'Afrika', {'default': ('required', None, 'Vize Gerekli')}),
    ('TD', 'Çad', 'Chad', '🇹🇩', 'Afrika', {'default': ('required', None, 'Vize Gerekli')}),
    ('NE', 'Nijer', 'Niger', '🇳🇪', 'Afrika', {'default': ('required', None, 'Vize Gerekli')}),
    ('ML', 'Mali', 'Mali', '🇲🇱', 'Afrika', {'default': ('required', None, 'Vize Gerekli')}),
    ('BF', 'Burkina Faso', 'Burkina Faso', '🇧🇫', 'Afrika', {'default': ('evisa', '90 Gün', 'Online e-Visa')}),
    ('GN', 'Gine', 'Guinea', '🇬🇳', 'Afrika', {'default': ('evisa', '90 Gün', 'Online e-Visa')}),
    ('GW', 'Gine-Bissau', 'Guinea-Bissau', '🇬🇼', 'Afrika', {'default': ('voa', '90 Gün', 'Kapıda Vize / e-Visa')}),
    ('SL', 'Sierra Leone', 'Sierra Leone', '🇸🇱', 'Afrika', {'default': ('voa', '30 Gün', 'Kapıda Vize / e-Visa')}),
    ('LR', 'Liberya', 'Liberia', '🇱🇷', 'Afrika', {'default': ('required', None, 'Vize Gerekli')}),
    ('TG', 'Togo', 'Togo', '🇹🇬', 'Afrika', {'default': ('evisa', '15 Gün', 'Online e-Visa')}),
    ('BJ', 'Benin', 'Benin', '🇧🇯', 'Afrika', {'default': ('evisa', '90 Gün', 'Online e-Visa')}),
    ('MR', 'Moritanya', 'Mauritania', '🇲🇷', 'Afrika', {'default': ('voa', '30 Gün', 'Kapıda Vize (55 EUR)')}),
    ('GM', 'Gambiya', 'The Gambia', '🇬🇲', 'Afrika', {'tr': ('free', '90 Gün', '90 Gün Vizesiz'), 'default': ('free', '90 Gün', 'Vizesiz')}),
    ('CV', 'Yeşil Burun (Cabo Verde)', 'Cape Verde', '🇨🇻', 'Afrika', {'default': ('evisa', '30 Gün', 'EASE Kayıt Formu')}),
    ('ST', 'Sao Tome ve Principe', 'Sao Tome and Principe', '🇸🇹', 'Afrika', {'tr': ('free', '15 Gün', '15 Gün Vizesiz'), 'default': ('free', '15 Gün', 'Vizesiz')}),
    ('GQ', 'Ekvator Ginesi', 'Equatorial Guinea', '🇬🇶', 'Afrika', {'default': ('evisa', '90 Gün', 'Online e-Visa')}),

    # Oceania
    ('AU', 'Avustralya', 'Australia', '🇦🇺', 'Okyanusya', {
        'tr': ('evisa', '90 Gün', 'Online Ziyaretçi Vizesi (e600)'),
        'AU': ('free', 'Süresiz', 'Vatandaş'), 'NZ': ('free', 'Süresiz', 'Serbest Yaşama/Çalışma'),
        'eu': ('evisa', '90 Gün', 'eVisitor (Subclass 651)'),
        'top': ('evisa', '90 Gün', 'ETA (Subclass 601)'),
        'default': ('evisa', '90 Gün', 'Online Vize (e600)')
    }),
    ('NZ', 'Yeni Zelanda', 'New Zealand', '🇳🇿', 'Okyanusya', {
        'tr': ('required', None, 'Ziyaretçi Vizesi Gerekli'),
        'AU': ('free', 'Süresiz', 'Serbest Dolaşım'), 'NZ': ('free', 'Süresiz', 'Vatandaş'),
        'eu': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
        'top': ('evisa', '90 Gün', 'NZeTA Elektronik İzin'),
        'default': ('required', None, 'Ziyaretçi Vizesi')
    }),
    ('FJ', 'Fiji', 'Fiji', '🇫🇯', 'Okyanusya', {'tr': ('free', '120 Gün', '120 Gün Vizesiz'), 'default': ('free', '120 Gün', '120 Gün Vizesiz')}),
    ('PG', 'Papua Yeni Gine', 'Papua New Guinea', '🇵🇬', 'Okyanusya', {'default': ('evisa', '60 Gün', 'Online Easy Visitor e-Visa')}),
    ('SB', 'Solomon Adaları', 'Solomon Islands', '🇸🇧', 'Okyanusya', {'default': ('voa', '90 Gün', 'Giriş İzni (Kapıda)')}),
    ('VU', 'Vanuatu', 'Vanuatu', '🇻🇺', 'Okyanusya', {'tr': ('free', '30 Gün', '30 Gün Vizesiz'), 'default': ('free', '30 Gün', '30 Gün Vizesiz')}),
    ('WS', 'Samoa', 'Samoa', '🇼🇸', 'Okyanusya', {'default': ('voa', '60 Gün', 'Giriş İzni (Kapıda 60 Gün)')}),
    ('TO', 'Tonga', 'Tonga', '🇹🇴', 'Okyanusya', {'default': ('voa', '31 Gün', 'Kapıda Vize')}),
    ('KI', 'Kiribati', 'Kiribati', '🇰🇮', 'Okyanusya', {'default': ('free', '90 Gün', 'Vizesiz')}),
    ('FM', 'Mikronezya', 'Micronesia', '🇫🇲', 'Okyanusya', {'default': ('free', '30 Gün', '30 Gün Vizesiz')}),
    ('PW', 'Palau', 'Palau', '🇵🇼', 'Okyanusya', {'default': ('voa', '30 Gün', 'Ücretsiz Kapıda Vize (30 Gün)')}),
    ('MH', 'Marshall Adaları', 'Marshall Islands', '🇲🇭', 'Okyanusya', {'default': ('voa', '90 Gün', 'Kapıda Vize')}),
    ('TV', 'Tuvalu', 'Tuvalu', '🇹🇻', 'Okyanusya', {'default': ('voa', '30 Gün', 'Kapıda Vize')}),
    ('NR', 'Nauru', 'Nauru', '🇳🇷', 'Okyanusya', {'default': ('required', None, 'Vize Gerekli')})
]

for item in all_world_list:
    destinations.append(create_country(item[0], item[1], item[2], item[3], item[4], item[5]))

print(f'Total destinations built: {len(destinations)}')

# Calculate Stats and Rankings dynamically!
stats = {}
scores_list = []

for p in passports_info:
    pid = p['id']
    free_cnt = 0
    evisa_cnt = 0
    voa_cnt = 0
    req_cnt = 0
    for d in destinations:
        st = d['visas'].get(pid, {}).get('status', 'required')
        if st == 'free':
            free_cnt += 1
        elif st == 'evisa':
            evisa_cnt += 1
        elif st == 'voa':
            voa_cnt += 1
        elif st == 'required':
            req_cnt += 1
            
    # Mobility score calculation (Free + VoA count as total visa-free access)
    access_score = free_cnt + voa_cnt
    weighted_score = round(free_cnt * 1.0 + voa_cnt * 0.8 + evisa_cnt * 0.6, 1)
    
    stats[pid] = {
        'free': free_cnt,
        'evisa': evisa_cnt,
        'voa': voa_cnt,
        'required': req_cnt,
        'total': len(destinations),
        'accessScore': access_score,
        'score': weighted_score
    }
    scores_list.append((pid, access_score, free_cnt))

# Rank passports based on accessScore descending
scores_list.sort(key=lambda x: (x[1], x[2]), reverse=True)

rank_map = {}
current_rank = 1
for i, (pid, score, _) in enumerate(scores_list):
    if i > 0 and score < scores_list[i-1][1]:
        current_rank = i + 1
    rank_map[pid] = current_rank
    stats[pid]['rank'] = current_rank

# Assign rank to passports_info
for p in passports_info:
    p['rank'] = rank_map.get(p['id'], 50)
    p['accessScore'] = stats[p['id']]['accessScore']
    p['score'] = stats[p['id']]['score']

# Write destinations.js
dest_json = json.dumps(destinations, ensure_ascii=False, indent=2)
with open('src/data/destinations.js', 'w', encoding='utf-8') as f:
    f.write('// 198 Dunya Ulkesi Vize Veri Tabani\nexport const DESTINATIONS = ' + dest_json + ';\n')

# Write passports.js
passports_content = f"""// Küresel Pasaport Profilleri ve Hızlı Kıyas Ön Ayarları
export const PASSPORTS = {json.dumps(passports_info, ensure_ascii=False, indent=2)};

export const PRESETS = [
  {{
    id: 'tr_compare',
    title: 'Türkiye: Bordo vs Yeşil',
    desc: 'Umuma Mahsus ve Hususi Pasaport farkları (Schengen, Rusya, Çin vb.)',
    passportIds: ['TR_BORDO', 'TR_YESIL']
  }},
  {{
    id: 'tr_all',
    title: 'Türkiye Pasaportları',
    desc: 'Bordo, Yeşil ve Gri Hizmet pasaportlarının yan yana kıyası',
    passportIds: ['TR_BORDO', 'TR_YESIL', 'TR_GRI']
  }},
  {{
    id: 'tr_vs_eu',
    title: 'Türkiye vs Almanya vs ABD',
    desc: 'Türkiye ile dünyanın en güçlü pasaportlarının kıyası',
    passportIds: ['TR_BORDO', 'TR_YESIL', 'DE', 'US']
  }},
  {{
    id: 'global_top',
    title: 'Dünyanın En Güçlü Pasaportları',
    desc: 'Singapur, Japonya, Almanya ve Birleşik Krallık',
    passportIds: ['SG', 'JP', 'DE', 'GB']
  }},
  {{
    id: 'regional_neighbors',
    title: 'Bölgesel Komşular',
    desc: 'Türkiye, Azerbaycan, Gürcistan, Yunanistan ve Rusya',
    passportIds: ['TR_BORDO', 'AZ', 'GE', 'GR', 'RU']
  }}
];
"""
with open('src/data/passports.js', 'w', encoding='utf-8') as f:
    f.write(passports_content)

# Write stats.js
stats_json = json.dumps(stats, ensure_ascii=False, indent=2)
with open('src/data/stats.js', 'w', encoding='utf-8') as f:
    f.write('export const PASSPORT_STATS = ' + stats_json + ';\n')

print(f"Success! {len(destinations)} destination countries and {len(passports_info)} passport rankings generated!")
