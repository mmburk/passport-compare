import React from 'react';
import { CheckCircle2, Globe, Ticket, ShieldAlert, Info, Sparkles, ExternalLink, X } from 'lucide-react';
import { PASSPORTS, VISA_STATUS_CONFIG } from '../data';

export default function ComparisonTable({
  destinations,
  selectedIds,
  onSelectCountry,
  onRemovePassport
}) {
  const selectedPassports = selectedIds
    .map(id => PASSPORTS.find(p => p.id === id))
    .filter(Boolean);

  const getStatusIcon = (status) => {
    switch (status) {
      case 'free':
        return <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />;
      case 'evisa':
        return <Globe className="w-4 h-4 text-sky-400 shrink-0" />;
      case 'voa':
        return <Ticket className="w-4 h-4 text-amber-400 shrink-0" />;
      case 'required':
      default:
        return <ShieldAlert className="w-4 h-4 text-rose-400 shrink-0" />;
    }
  };

  const getCellClasses = (status) => {
    switch (status) {
      case 'free':
        return 'bg-emerald-950/40 text-emerald-200 border-emerald-500/30 hover:bg-emerald-900/50 hover:border-emerald-500/50';
      case 'evisa':
        return 'bg-sky-950/40 text-sky-200 border-sky-500/30 hover:bg-sky-900/50 hover:border-sky-500/50';
      case 'voa':
        return 'bg-amber-950/40 text-amber-200 border-amber-500/30 hover:bg-amber-900/50 hover:border-amber-500/50';
      case 'required':
      default:
        return 'bg-rose-950/40 text-rose-200 border-rose-500/30 hover:bg-rose-900/50 hover:border-rose-500/50';
    }
  };

  if (destinations.length === 0) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16 text-center">
        <div className="w-16 h-16 rounded-2xl bg-slate-900 border border-slate-800 flex items-center justify-center mx-auto mb-4 text-3xl">
          🔍
        </div>
        <h3 className="text-lg font-bold text-white mb-1">Eşleşen Ülke Bulunamadı</h3>
        <p className="text-sm text-slate-400 max-w-md mx-auto">
          Arama kriterlerinizi veya filtrelerinizi değiştirerek tekrar deneyebilirsiniz.
        </p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <div className="relative border border-slate-800/80 rounded-2xl overflow-hidden bg-slate-950/80 shadow-2xl backdrop-blur-sm">
        <div className="overflow-x-auto max-w-full">
          <table className="w-full text-left border-collapse">
            {/* Table Header */}
            <thead>
              <tr className="border-b border-slate-800 bg-slate-900/90 text-xs font-semibold text-slate-300">
                {/* Fixed Destination Column Header */}
                <th className="sticky left-0 z-20 bg-slate-900/95 backdrop-blur-md px-5 py-4 w-72 min-w-[240px] shadow-[4px_0_12px_rgba(0,0,0,0.5)] border-r border-slate-800">
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-white uppercase tracking-wider text-[11px]">
                      Hedef Ülke ({destinations.length})
                    </span>
                    <span className="text-[10px] text-slate-400 font-normal">Bayrak & Bölge</span>
                  </div>
                </th>

                {/* Passport Columns Headers */}
                {selectedPassports.map((passport) => (
                  <th
                    key={passport.id}
                    className="px-4 py-3 min-w-[200px] border-r border-slate-800/80 last:border-r-0"
                  >
                    <div className="flex items-center justify-between gap-2">
                      <div className="flex items-center gap-2">
                        <span className="text-base">{passport.flag}</span>
                        <div>
                          <div className="font-bold text-slate-100 leading-snug">
                            {passport.name}
                          </div>
                          <div className="text-[10px] text-slate-400 font-normal leading-tight">
                            {passport.country}
                          </div>
                        </div>
                      </div>

                      {selectedPassports.length > 1 && (
                        <button
                          onClick={() => onRemovePassport(passport.id)}
                          title={`${passport.name} pasaportunu kaldır`}
                          className="p-1 rounded text-slate-500 hover:text-rose-400 hover:bg-slate-800 transition-colors"
                        >
                          <X className="w-3.5 h-3.5" />
                        </button>
                      )}
                    </div>
                  </th>
                ))}
              </tr>
            </thead>

            {/* Table Body */}
            <tbody className="divide-y divide-slate-800/60 text-sm">
              {destinations.map((dest, rowIndex) => (
                <tr
                  key={dest.id}
                  className="hover:bg-slate-900/40 transition-colors group cursor-pointer"
                  onClick={() => onSelectCountry(dest)}
                >
                  {/* Sticky Country Column */}
                  <td className="sticky left-0 z-10 bg-slate-950/95 group-hover:bg-slate-900/95 backdrop-blur-md px-5 py-3.5 shadow-[4px_0_12px_rgba(0,0,0,0.5)] border-r border-slate-800 transition-colors">
                    <div className="flex items-center gap-3">
                      <span className="text-2xl drop-shadow select-none">{dest.flag}</span>
                      <div>
                        <div className="font-bold text-slate-100 flex items-center gap-1.5">
                          <span>{dest.name}</span>
                          {dest.isSchengen && (
                            <span className="text-[9px] font-bold px-1.5 py-0.2 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">
                              Schengen
                            </span>
                          )}
                        </div>
                        <div className="flex items-center gap-2 text-xs text-slate-400 mt-0.5">
                          <span>{dest.nameEn}</span>
                          <span>•</span>
                          <span className="text-[11px] text-slate-500">{dest.continent}</span>
                        </div>
                      </div>
                    </div>
                  </td>

                  {/* Passport Comparison Cells */}
                  {selectedPassports.map((passport) => {
                    const visaInfo = dest.visas[passport.id] || {
                      status: 'required',
                      days: null,
                      note: 'Vize Gerekli'
                    };

                    const statusConfig = VISA_STATUS_CONFIG[visaInfo.status] || VISA_STATUS_CONFIG.required;
                    const cellClasses = getCellClasses(visaInfo.status);

                    return (
                      <td
                        key={passport.id}
                        className="px-4 py-3 border-r border-slate-800/60 last:border-r-0"
                      >
                        <div className={`p-2.5 rounded-xl border transition-all ${cellClasses}`}>
                          <div className="flex items-center justify-between gap-1 mb-1">
                            <div className="flex items-center gap-1.5 font-bold text-xs tracking-tight">
                              {getStatusIcon(visaInfo.status)}
                              <span>{statusConfig.shortLabel}</span>
                            </div>
                            {visaInfo.days && (
                              <span className="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-black/40 text-slate-200 border border-white/10">
                                {visaInfo.days}
                              </span>
                            )}
                          </div>
                          <div className="text-[11px] opacity-80 line-clamp-1 leading-tight mt-0.5">
                            {visaInfo.note || statusConfig.description}
                          </div>
                        </div>
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
