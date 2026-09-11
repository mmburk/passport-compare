import React from 'react';
import { Search, Sparkles, Filter, CheckCircle2, Globe2, X } from 'lucide-react';

const CONTINENTS = ['Tümü', 'Avrupa', 'Asya', 'Amerika', 'Afrika', 'Okyanusya'];

export default function FilterBar({
  searchQuery,
  onSearchChange,
  selectedContinent,
  onContinentChange,
  onlyDifferences,
  onToggleOnlyDifferences,
  statusFilter,
  onStatusFilterChange,
  totalMatching,
  totalDestinations
}) {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2">
      <div className="bg-slate-900/90 border border-slate-800/80 rounded-2xl p-3 sm:p-4 shadow-xl space-y-3">
        {/* Top Controls Row */}
        <div className="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3">
          {/* Search Box */}
          <div className="relative flex-1">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
            <input
              type="text"
              placeholder="Hedef ülke ara (Örn: Almanya, Yunanistan, Japonya, Mısır, Brezilya)..."
              value={searchQuery}
              onChange={(e) => onSearchChange(e.target.value)}
              className="w-full pl-10 pr-10 py-2 bg-slate-950/70 border border-slate-700/70 rounded-xl text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
            />
            {searchQuery && (
              <button
                onClick={() => onSearchChange('')}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>

          {/* Only Differences Toggle Switch */}
          <div className="flex items-center gap-3">
            <button
              onClick={onToggleOnlyDifferences}
              className={`flex items-center gap-2.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold border transition-all ${
                onlyDifferences
                  ? 'bg-amber-500/20 text-amber-300 border-amber-500/50 shadow-md shadow-amber-500/10 ring-1 ring-amber-500/30'
                  : 'bg-slate-950/60 text-slate-400 border-slate-800 hover:border-slate-700 hover:text-slate-200'
              }`}
            >
              <Sparkles className={`w-4 h-4 ${onlyDifferences ? 'text-amber-400 animate-pulse' : 'text-slate-500'}`} />
              <span>Yalnızca Farklılıkları Göster</span>
              <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold uppercase ${
                onlyDifferences ? 'bg-amber-400 text-slate-950' : 'bg-slate-800 text-slate-400'
              }`}>
                {onlyDifferences ? 'Açık' : 'Kapalı'}
              </span>
            </button>
          </div>
        </div>

        {/* Bottom Filters Row: Continents & Status */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2.5 pt-2 border-t border-slate-800/60">
          {/* Continent Pills */}
          <div className="flex items-center gap-1.5 overflow-x-auto max-w-full pb-1">
            <span className="text-xs text-slate-500 font-medium mr-1 flex items-center gap-1 shrink-0">
              <Globe2 className="w-3.5 h-3.5" /> Kıta:
            </span>
            {CONTINENTS.map((continent) => {
              const isSelected = selectedContinent === continent;
              return (
                <button
                  key={continent}
                  onClick={() => onContinentChange(continent)}
                  className={`px-3 py-1 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
                    isSelected
                      ? 'bg-indigo-600 text-white font-semibold shadow-md shadow-indigo-600/30'
                      : 'bg-slate-950/60 hover:bg-slate-800 text-slate-400 hover:text-slate-200 border border-slate-800'
                  }`}
                >
                  {continent}
                </button>
              );
            })}
          </div>

          {/* Results Count Badge */}
          <div className="text-xs text-slate-400 self-end sm:self-auto shrink-0">
            <span className="font-bold text-indigo-400">{totalMatching}</span> / {totalDestinations} ülke listeleniyor
          </div>
        </div>
      </div>
    </div>
  );
}
