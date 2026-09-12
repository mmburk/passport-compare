import React from 'react';
import { CheckCircle2, Globe, Ticket, ShieldAlert, X } from 'lucide-react';
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
        return <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />;
      case 'evisa':
        return <Globe className="w-3.5 h-3.5 text-sky-600 dark:text-sky-400 shrink-0" />;
      case 'voa':
        return <Ticket className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400 shrink-0" />;
      case 'required':
      default:
        return <ShieldAlert className="w-3.5 h-3.5 text-zinc-400 dark:text-zinc-500 shrink-0" />;
    }
  };

  const getCellClasses = (status) => {
    switch (status) {
      case 'free':
        return 'bg-emerald-50/70 text-emerald-900 border-emerald-200/70 dark:bg-emerald-950/25 dark:text-emerald-300 dark:border-emerald-800/40 hover:bg-emerald-100/70 dark:hover:bg-emerald-950/40';
      case 'evisa':
        return 'bg-sky-50/70 text-sky-900 border-sky-200/70 dark:bg-sky-950/25 dark:text-sky-300 dark:border-sky-800/40 hover:bg-sky-100/70 dark:hover:bg-sky-950/40';
      case 'voa':
        return 'bg-amber-50/70 text-amber-900 border-amber-200/70 dark:bg-amber-950/25 dark:text-amber-300 dark:border-amber-800/40 hover:bg-amber-100/70 dark:hover:bg-amber-950/40';
      case 'required':
      default:
        return 'bg-zinc-50 text-zinc-700 border-zinc-200/80 dark:bg-zinc-900/40 dark:text-zinc-400 dark:border-zinc-800/60 hover:bg-zinc-100/60 dark:hover:bg-zinc-900/70';
    }
  };

  if (destinations.length === 0) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16 text-center">
        <div className="w-14 h-14 rounded-2xl bg-zinc-100 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 flex items-center justify-center mx-auto mb-3 text-2xl">
          🔍
        </div>
        <h3 className="text-base font-semibold text-zinc-900 dark:text-zinc-100 mb-1">Eşleşen Ülke Bulunamadı</h3>
        <p className="text-xs text-zinc-500 dark:text-zinc-400 max-w-sm mx-auto">
          Arama kriterlerinizi veya filtrelerinizi değiştirerek tekrar deneyebilirsiniz.
        </p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
      <div className="relative border border-zinc-200 dark:border-zinc-800 rounded-2xl overflow-hidden bg-white dark:bg-zinc-900/90 shadow-xs transition-colors">
        <div className="overflow-x-auto max-w-full">
          <table className="w-full text-left border-collapse">
            {/* Table Header */}
            <thead>
              <tr className="border-b border-zinc-200 dark:border-zinc-800 bg-zinc-100/80 dark:bg-zinc-900/90 text-xs font-semibold text-zinc-600 dark:text-zinc-400">
                {/* Fixed Destination Column Header: Responsive width (140px on mobile, 240px on desktop) */}
                <th className="sticky left-0 z-20 bg-zinc-100/95 dark:bg-zinc-900/95 backdrop-blur-md px-3.5 sm:px-5 py-3.5 w-36 sm:w-64 min-w-[130px] sm:min-w-[220px] shadow-[2px_0_8px_rgba(0,0,0,0.06)] dark:shadow-[2px_0_8px_rgba(0,0,0,0.4)] border-r border-zinc-200 dark:border-zinc-800">
                  <div className="flex items-center justify-between">
                    <span className="font-semibold text-zinc-900 dark:text-zinc-100 uppercase tracking-wider text-[10px] sm:text-[11px]">
                      Hedef ({destinations.length})
                    </span>
                    <span className="hidden sm:inline text-[10px] text-zinc-400 font-normal">Bayrak & Bölge</span>
                  </div>
                </th>

                {/* Passport Columns Headers */}
                {selectedPassports.map((passport) => (
                  <th
                    key={passport.id}
                    className="px-3.5 sm:px-4 py-3 min-w-[150px] sm:min-w-[180px] border-r border-zinc-200 dark:border-zinc-800/80 last:border-r-0"
                  >
                    <div className="flex items-center justify-between gap-1.5">
                      <div className="flex items-center gap-2 min-w-0">
                        <span className="text-base shrink-0">{passport.flag}</span>
                        <div className="min-w-0">
                          <div className="font-semibold text-zinc-900 dark:text-zinc-100 leading-snug truncate text-xs sm:text-sm">
                            {passport.name}
                          </div>
                          <div className="text-[10px] text-zinc-400 dark:text-zinc-500 font-normal leading-tight truncate">
                            {passport.country}
                          </div>
                        </div>
                      </div>

                      {selectedPassports.length > 1 && (
                        <button
                          onClick={() => onRemovePassport(passport.id)}
                          title={`${passport.name} pasaportunu kaldır`}
                          className="p-1 rounded-md text-zinc-400 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-zinc-200 dark:hover:bg-zinc-800 transition-colors shrink-0"
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
            <tbody className="divide-y divide-zinc-200/80 dark:divide-zinc-800/60 text-sm">
              {destinations.map((dest) => (
                <tr
                  key={dest.id}
                  className="hover:bg-zinc-50 dark:hover:bg-zinc-800/40 transition-colors group cursor-pointer"
                  onClick={() => onSelectCountry(dest)}
                >
                  {/* Sticky Country Column */}
                  <td className="sticky left-0 z-10 bg-white dark:bg-zinc-950 group-hover:bg-zinc-50 dark:group-hover:bg-zinc-900/90 backdrop-blur-md px-3 sm:px-4 py-2.5 sm:py-3 shadow-[2px_0_8px_rgba(0,0,0,0.05)] dark:shadow-[2px_0_8px_rgba(0,0,0,0.4)] border-r border-zinc-200 dark:border-zinc-800 transition-colors">
                    <div className="flex items-center gap-2 sm:gap-3 min-w-0">
                      <span className="text-xl sm:text-2xl drop-shadow-xs select-none shrink-0">{dest.flag}</span>
                      <div className="min-w-0 flex-1">
                        <div className="font-semibold text-zinc-900 dark:text-zinc-100 flex items-center gap-1 leading-snug truncate text-xs sm:text-sm">
                          <span className="truncate">{dest.name}</span>
                          {dest.isSchengen && (
                            <span className="hidden sm:inline-block text-[9px] font-semibold px-1.5 py-0.2 rounded bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800/60 shrink-0">
                              Schengen
                            </span>
                          )}
                        </div>
                        <div className="flex items-center gap-1.5 text-[10px] sm:text-xs text-zinc-400 dark:text-zinc-500 mt-0.5 truncate">
                          <span className="truncate">{dest.nameEn}</span>
                          <span className="hidden xs:inline">•</span>
                          <span className="hidden xs:inline truncate text-[10px] text-zinc-400">{dest.continent}</span>
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
                        className="px-2.5 sm:px-3.5 py-2 sm:py-2.5 border-r border-zinc-200/80 dark:border-zinc-800/60 last:border-r-0"
                      >
                        <div className={`p-2 rounded-xl border transition-all ${cellClasses}`}>
                          <div className="flex items-center justify-between gap-1 mb-0.5">
                            <div className="flex items-center gap-1.5 font-medium text-xs tracking-tight">
                              {getStatusIcon(visaInfo.status)}
                              <span>{statusConfig.shortLabel}</span>
                            </div>
                            {visaInfo.days && (
                              <span className="text-[10px] font-medium px-1.5 py-0.2 rounded-md bg-white/70 dark:bg-zinc-800/80 text-zinc-700 dark:text-zinc-300 border border-zinc-200/80 dark:border-zinc-700/60">
                                {visaInfo.days}
                              </span>
                            )}
                          </div>
                          <div className="text-[10px] sm:text-[11px] opacity-75 line-clamp-1 leading-tight mt-0.5">
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

