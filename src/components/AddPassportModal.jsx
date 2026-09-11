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
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-fadeIn">
      <div className="relative w-full max-w-2xl bg-slate-900 border border-slate-700/70 rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[85vh]">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-900/90">
          <div>
            <h3 className="text-lg font-bold text-white flex items-center gap-2">
              <span>🛂</span> Karşılaştırmaya Pasaport Ekle
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">
              Listeye eklemek istediğiniz ülkeyi veya pasaport türünü seçin
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Search */}
        <div className="p-4 border-b border-slate-800/80 bg-slate-950/40">
          <div className="relative">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
            <input
              type="text"
              placeholder="Pasaport veya ülke ara (Örn: Almanya, Bordo, Yeşil, ABD, Singapur)..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full pl-10 pr-4 py-2.5 bg-slate-900 border border-slate-700/70 rounded-xl text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
              autoFocus
            />
          </div>
        </div>

        {/* List */}
        <div className="flex-1 overflow-y-auto p-4 space-y-2.5 divide-y divide-slate-800/40">
          {filteredPassports.map((p) => {
            const isSelected = selectedIds.includes(p.id);
            const stats = PASSPORT_STATS[p.id] || { free: 0, evisa: 0, voa: 0 };
            return (
              <div
                key={p.id}
                className={`flex items-center justify-between p-3.5 rounded-xl border transition-all ${
                  isSelected
                    ? 'bg-slate-800/30 border-slate-800 opacity-60'
                    : 'bg-slate-900/50 border-slate-800/80 hover:border-slate-700 hover:bg-slate-800/60'
                }`}
              >
                <div className="flex items-center gap-3.5">
                  <div
                    className="w-11 h-14 rounded-md shadow-md flex flex-col items-center justify-between p-1.5 text-center shrink-0 border"
                    style={{ backgroundColor: p.coverColor, borderColor: 'rgba(255,255,255,0.15)' }}
                  >
                    <span className="text-xs">{p.flag}</span>
                    <span className="text-[7px] font-bold tracking-widest text-amber-300 uppercase">PASSPORT</span>
                  </div>
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="font-semibold text-slate-100">{p.name}</span>
                      <span className="text-xs text-slate-400 font-normal">({p.country})</span>
                      {p.id.startsWith('TR_') && (
                        <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                          TR
                        </span>
                      )}
                    </div>
                    <p className="text-xs text-slate-400 mt-0.5">{p.fullName}</p>
                    <div className="flex items-center gap-3 mt-1.5 text-[11px] text-slate-400">
                      <span className="text-emerald-400 font-medium">{stats.free} Vizesiz</span>
                      <span>•</span>
                      <span className="text-sky-400 font-medium">{stats.evisa} e-Vize</span>
                      <span>•</span>
                      <span className="text-amber-400 font-medium">{stats.voa} Kapıda</span>
                    </div>
                  </div>
                </div>

                <button
                  disabled={isSelected}
                  onClick={() => {
                    onAddPassport(p.id);
                  }}
                  className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                    isSelected
                      ? 'bg-slate-800 text-slate-400 cursor-not-allowed'
                      : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-md shadow-indigo-600/30'
                  }`}
                >
                  {isSelected ? (
                    <>
                      <Check className="w-3.5 h-3.5" /> Eklendi
                    </>
                  ) : (
                    <>
                      <Plus className="w-3.5 h-3.5" /> Karşılaştır
                    </>
                  )}
                </button>
              </div>
            );
          })}
        </div>

        {/* Footer */}
        <div className="px-6 py-3 border-t border-slate-800 bg-slate-900/90 text-right">
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl text-sm font-medium text-slate-300 hover:text-white bg-slate-800 hover:bg-slate-700 transition-colors"
          >
            Kapat
          </button>
        </div>
      </div>
    </div>
  );
}
