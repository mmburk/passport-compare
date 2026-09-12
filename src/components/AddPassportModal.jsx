import React, { useState } from 'react';
import { X, Search, Plus, Check } from 'lucide-react';
import { PASSPORTS, PASSPORT_STATS } from '../data';

export default function AddPassportModal({ isOpen, onClose, selectedIds, onAddPassport }) {
  const [search, setSearch] = useState('');

  if (!isOpen) return null;

  const filteredPassports = PASSPORTS.filter(p => {
    const q = search.toLowerCase();
    return (
      p.name.toLowerCase().includes(q) ||
      p.country.toLowerCase().includes(q) ||
      p.type.toLowerCase().includes(q)
    );
  });

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 bg-black/60 dark:bg-black/80 backdrop-blur-xs animate-fadeIn">
      <div className="relative w-full max-w-2xl bg-white dark:bg-zinc-900 border-t sm:border border-zinc-200 dark:border-zinc-800 rounded-t-3xl sm:rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh] sm:max-h-[85vh] transition-colors">
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-3.5 sm:px-6 sm:py-4 border-b border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/90">
          <div>
            <h3 className="text-base sm:text-lg font-semibold text-zinc-900 dark:text-white flex items-center gap-2">
              <span>🛂</span> Karşılaştırmaya Pasaport Ekle
            </h3>
            <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-0.5">
              Listeye eklemek istediğiniz pasaportu seçin
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 text-zinc-400 hover:text-zinc-700 dark:hover:text-white rounded-lg hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Search Input with 16px font on mobile */}
        <div className="p-3 sm:p-4 border-b border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950/40">
          <div className="relative">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-400 dark:text-zinc-500" />
            <input
              type="text"
              placeholder="Pasaport veya ülke ara (Almanya, Bordo, Yeşil, Singapur)..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full pl-10 pr-4 py-2 sm:py-2.5 bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 rounded-xl text-base sm:text-sm text-zinc-900 dark:text-zinc-100 placeholder-zinc-400 dark:placeholder-zinc-500 focus:outline-hidden focus:ring-1 focus:ring-zinc-400 dark:focus:ring-zinc-600 transition-all"
              autoFocus
            />
          </div>
        </div>

        {/* List */}
        <div className="flex-1 overflow-y-auto p-3 sm:p-4 space-y-2">
          {filteredPassports.map((p) => {
            const isSelected = selectedIds.includes(p.id);
            const stats = PASSPORT_STATS[p.id] || { free: 0, evisa: 0, voa: 0 };
            return (
              <div
                key={p.id}
                className={`flex items-center justify-between p-3 rounded-xl border transition-all ${
                  isSelected
                    ? 'bg-zinc-100/50 dark:bg-zinc-900/40 border-zinc-200 dark:border-zinc-800 opacity-60'
                    : 'bg-white dark:bg-zinc-900/60 border-zinc-200 dark:border-zinc-800/80 hover:border-zinc-300 dark:hover:border-zinc-700'
                }`}
              >
                <div className="flex items-center gap-3 min-w-0">
                  <div
                    className="w-9 h-12 rounded-md shadow-xs flex flex-col items-center justify-between p-1 text-center shrink-0 border border-white/20"
                    style={{ backgroundColor: p.coverColor }}
                  >
                    <span className="text-xs">{p.flag}</span>
                    <span className="text-[6px] font-bold tracking-widest text-amber-200/90 uppercase">PASSPORT</span>
                  </div>
                  <div className="min-w-0">
                    <div className="flex items-center gap-1.5 flex-wrap">
                      <span className="font-semibold text-zinc-900 dark:text-zinc-100 text-sm leading-snug">{p.name}</span>
                      <span className="text-xs text-zinc-400 dark:text-zinc-500 font-normal">({p.country})</span>
                      {p.id.startsWith('TR_') && (
                        <span className="text-[9px] font-semibold px-1.5 py-0.2 rounded bg-red-50 dark:bg-red-950/40 text-red-700 dark:text-red-300 border border-red-200 dark:border-red-800/60">
                          TR
                        </span>
                      )}
                    </div>
                    <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-0.5 truncate">{p.fullName}</p>
                    <div className="flex items-center gap-2 mt-1 text-[11px] text-zinc-500 dark:text-zinc-400">
                      <span className="text-emerald-700 dark:text-emerald-400 font-medium">{stats.free} Vizesiz</span>
                      <span>•</span>
                      <span className="text-sky-700 dark:text-sky-400 font-medium">{stats.evisa} e-Vize</span>
                      <span>•</span>
                      <span className="text-amber-800 dark:text-amber-400 font-medium">{stats.voa} Kapıda</span>
                    </div>
                  </div>
                </div>

                <button
                  disabled={isSelected}
                  onClick={() => {
                    onAddPassport(p.id);
                  }}
                  className={`px-3 py-1.5 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-all shrink-0 ml-2 ${
                    isSelected
                      ? 'bg-zinc-100 dark:bg-zinc-800 text-zinc-400 dark:text-zinc-500 cursor-not-allowed'
                      : 'bg-zinc-900 dark:bg-zinc-100 hover:bg-zinc-800 dark:hover:bg-white text-white dark:text-zinc-900 shadow-xs'
                  }`}
                >
                  {isSelected ? (
                    <>
                      <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" /> Eklendi
                    </>
                  ) : (
                    <>
                      <Plus className="w-3.5 h-3.5" /> Ekle
                    </>
                  )}
                </button>
              </div>
            );
          })}
        </div>

        {/* Footer */}
        <div className="px-5 py-3 border-t border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/90 text-right">
          <button
            onClick={onClose}
            className="w-full sm:w-auto px-4 py-2 rounded-xl text-xs sm:text-sm font-medium text-zinc-700 dark:text-zinc-300 hover:text-zinc-900 dark:hover:text-white bg-zinc-200 dark:bg-zinc-800 hover:bg-zinc-300 dark:hover:bg-zinc-700 transition-colors"
          >
            Kapat
          </button>
        </div>
      </div>
    </div>
  );
}

