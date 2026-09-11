import React from 'react';
import { X, Globe, Calendar, ShieldAlert, CheckCircle2, Ticket, AlertTriangle, ExternalLink } from 'lucide-react';
import { PASSPORTS, VISA_STATUS_CONFIG } from '../data';

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
          bg: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
          dot: 'bg-emerald-400'
        };
      case 'evisa':
        return {
          label: 'e-Vize / Elektronik İzin',
          bg: 'bg-sky-500/20 text-sky-300 border-sky-500/40',
          dot: 'bg-sky-400'
        };
      case 'voa':
        return {
          label: 'Kapıda Vize (VoA)',
          bg: 'bg-amber-500/20 text-amber-300 border-amber-500/40',
          dot: 'bg-amber-400'
        };
      case 'required':
      default:
        return {
          label: 'Vize Gerekli (Konsolosluk)',
          bg: 'bg-rose-500/20 text-rose-300 border-rose-500/40',
          dot: 'bg-rose-400'
        };
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-fadeIn">
      <div className="relative w-full max-w-2xl bg-slate-900 border border-slate-700/70 rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-950/80">
          <div className="flex items-center gap-3.5">
            <span className="text-3xl">{country.flag}</span>
            <div>
              <div className="flex items-center gap-2">
                <h3 className="text-xl font-bold text-white leading-none">{country.name}</h3>
                {country.isSchengen && (
                  <span className="text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">
                    Schengen Ülkesi
                  </span>
                )}
              </div>
              <p className="text-xs text-slate-400 mt-1">
                {country.nameEn} • {country.continent}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Passport Comparisons List */}
        <div className="flex-1 overflow-y-auto p-6 space-y-3">
          <h4 className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">
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
                className="p-4 rounded-xl bg-slate-950/70 border border-slate-800/90 flex flex-col sm:flex-row sm:items-center justify-between gap-3"
              >
                <div className="flex items-center gap-3">
                  <span className="text-xl">{passport.flag}</span>
                  <div>
                    <div className="font-bold text-slate-100 text-sm">{passport.name}</div>
                    <div className="text-xs text-slate-400">{passport.type}</div>
                  </div>
                </div>

                <div className="flex items-center gap-2.5 flex-wrap">
                  <span className={`px-2.5 py-1 rounded-lg text-xs font-bold border flex items-center gap-1.5 ${badge.bg}`}>
                    <span className={`w-2 h-2 rounded-full ${badge.dot}`}></span>
                    <span>{badge.label}</span>
                  </span>

                  {visaInfo.days && (
                    <span className="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-200 border border-slate-700">
                      {visaInfo.days}
                    </span>
                  )}
                </div>

                {visaInfo.note && (
                  <div className="w-full sm:w-auto text-xs text-slate-400 sm:text-right border-t sm:border-t-0 border-slate-800/80 pt-2 sm:pt-0">
                    <span className="text-slate-300 font-medium">{visaInfo.note}</span>
                  </div>
                )}
              </div>
            );
          })}

          {/* Travel Tips Box */}
          <div className="p-4 rounded-xl bg-indigo-950/20 border border-indigo-500/30 text-xs text-indigo-300 space-y-1.5 mt-4">
            <div className="font-bold flex items-center gap-1.5 text-indigo-200">
              <AlertTriangle className="w-4 h-4 text-amber-400" />
              <span>Önemli Seyahat Hatırlatmaları</span>
            </div>
            <ul className="list-disc list-inside space-y-1 text-slate-400 pl-1">
              <li>Pasaportunuzun seyahat tarihinden itibaren en az 6 ay geçerlilik süresi bulunmalıdır.</li>
              <li>Vizesiz olsa dahi sınır kapılarında otel rezervasyonu, dönüş bileti ve yeterli bakiye sorulabilir.</li>
              <li>Hususi (Yeşil) pasaport sahipleri için Schengen bölgesinde 180 günde 90 gün kuralı geçerlidir.</li>
            </ul>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 border-t border-slate-800 bg-slate-950/80 text-right">
          <button
            onClick={onClose}
            className="px-5 py-2 rounded-xl text-sm font-semibold bg-indigo-600 hover:bg-indigo-500 text-white transition-colors"
          >
            Tamam
          </button>
        </div>
      </div>
    </div>
  );
}
