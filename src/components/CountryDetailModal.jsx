import React from 'react';
import { X, AlertTriangle } from 'lucide-react';
import { PASSPORTS } from '../data';

export default function CountryDetailModal({ country, selectedIds, onClose }) {
  if (!country) return null;

  const selectedPassports = selectedIds
    .map(id => PASSPORTS.find(p => p.id === id))
    .filter(Boolean);

  const getStatusBadge = (status) => {
    switch (status) {
      case 'free':
        return {
          label: 'Vizesiz Giriş',
          bg: 'bg-emerald-50 text-emerald-800 border-emerald-200/80 dark:bg-emerald-950/30 dark:text-emerald-300 dark:border-emerald-800/40',
          dot: 'bg-emerald-500'
        };
      case 'evisa':
        return {
          label: 'e-Vize / Elektronik İzin',
          bg: 'bg-sky-50 text-sky-800 border-sky-200/80 dark:bg-sky-950/30 dark:text-sky-300 dark:border-sky-800/40',
          dot: 'bg-sky-500'
        };
      case 'voa':
        return {
          label: 'Kapıda Vize (VoA)',
          bg: 'bg-amber-50 text-amber-900 border-amber-200/80 dark:bg-amber-950/30 dark:text-amber-300 dark:border-amber-800/40',
          dot: 'bg-amber-500'
        };
      case 'required':
      default:
        return {
          label: 'Vize Gerekli (Konsolosluk)',
          bg: 'bg-zinc-100 text-zinc-700 border-zinc-200 dark:bg-zinc-800/60 dark:text-zinc-300 dark:border-zinc-700',
          dot: 'bg-zinc-400'
        };
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 bg-black/60 dark:bg-black/80 backdrop-blur-xs animate-fadeIn">
      <div className="relative w-full max-w-2xl bg-white dark:bg-zinc-900 border-t sm:border border-zinc-200 dark:border-zinc-800 rounded-t-3xl sm:rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh] sm:max-h-[85vh] transition-colors">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-3.5 sm:px-6 sm:py-4 border-b border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/90">
          <div className="flex items-center gap-3">
            <span className="text-3xl">{country.flag}</span>
            <div>
              <div className="flex items-center gap-2">
                <h3 className="text-lg sm:text-xl font-bold text-zinc-900 dark:text-white leading-none">{country.name}</h3>
                {country.isSchengen && (
                  <span className="text-[10px] sm:text-xs font-semibold px-2 py-0.5 rounded-full bg-blue-50 dark:bg-blue-950/50 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800/60">
                    Schengen
                  </span>
                )}
              </div>
              <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-1">
                {country.nameEn} • {country.continent}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 text-zinc-400 hover:text-zinc-700 dark:hover:text-white rounded-lg hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Passport Comparisons List */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-3">
          <h4 className="text-xs font-medium text-zinc-500 dark:text-zinc-400 uppercase tracking-wider">
            Seçili Pasaportların Vize Durumları ({selectedPassports.length})
          </h4>

          {selectedPassports.map((passport) => {
            const visaInfo = country.visas[passport.id] || {
              status: 'required',
              days: null,
              note: 'Vize Gerekli'
            };
            const badge = getStatusBadge(visaInfo.status);

            return (
              <div
                key={passport.id}
                className="p-3.5 sm:p-4 rounded-xl bg-zinc-50/70 dark:bg-zinc-950/60 border border-zinc-200 dark:border-zinc-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 sm:gap-3"
              >
                <div className="flex items-center gap-2.5">
                  <span className="text-xl">{passport.flag}</span>
                  <div>
                    <div className="font-semibold text-zinc-900 dark:text-zinc-100 text-sm">{passport.name}</div>
                    <div className="text-xs text-zinc-400 dark:text-zinc-500">{passport.type}</div>
                  </div>
                </div>

                <div className="flex items-center gap-2 flex-wrap">
                  <span className={`px-2.5 py-1 rounded-lg text-xs font-medium border flex items-center gap-1.5 ${badge.bg}`}>
                    <span className={`w-1.5 h-1.5 rounded-full ${badge.dot}`}></span>
                    <span>{badge.label}</span>
                  </span>

                  {visaInfo.days && (
                    <span className="px-2 py-0.5 rounded-md text-xs font-medium bg-white dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700">
                      {visaInfo.days}
                    </span>
                  )}
                </div>

                {visaInfo.note && (
                  <div className="w-full sm:w-auto text-xs text-zinc-500 dark:text-zinc-400 sm:text-right border-t sm:border-t-0 border-zinc-200 dark:border-zinc-800 pt-1.5 sm:pt-0">
                    <span className="text-zinc-700 dark:text-zinc-300 font-normal">{visaInfo.note}</span>
                  </div>
                )}
              </div>
            );
          })}

          {/* Travel Tips Box */}
          <div className="p-3.5 sm:p-4 rounded-xl bg-zinc-50 dark:bg-zinc-800/40 border border-zinc-200 dark:border-zinc-800 text-xs space-y-1.5 mt-3">
            <div className="font-semibold flex items-center gap-1.5 text-zinc-800 dark:text-zinc-200">
              <AlertTriangle className="w-4 h-4 text-amber-500" />
              <span>Önemli Seyahat Hatırlatmaları</span>
            </div>
            <ul className="list-disc list-inside space-y-1 text-zinc-500 dark:text-zinc-400 pl-1">
              <li>Pasaportunuzun seyahat tarihinden itibaren en az 6 ay geçerlilik süresi bulunmalıdır.</li>
              <li>Vizesiz seyahatlerde dahi dönüş bileti ve konaklama rezervasyonu sınır kapısında talep edilebilir.</li>
              <li>Yeşil (Hususi) pasaport için Schengen bölgesinde 180 günde maksimum 90 gün kuralı geçerlidir.</li>
            </ul>
          </div>
        </div>

        {/* Footer */}
        <div className="px-5 py-3 border-t border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/90 text-right">
          <button
            onClick={onClose}
            className="w-full sm:w-auto px-5 py-2 rounded-xl text-xs sm:text-sm font-medium bg-zinc-900 dark:bg-zinc-100 hover:bg-zinc-800 dark:hover:bg-white text-white dark:text-zinc-900 transition-colors shadow-xs"
          >
            Kapat
          </button>
        </div>
      </div>
    </div>
  );
}

