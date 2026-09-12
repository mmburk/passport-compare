import React from 'react';
import { Search, Sparkles, Globe2, X } from 'lucide-react';

const CONTINENTS = ['Tümü', 'Avrupa', 'Asya', 'Amerika', 'Afrika', 'Okyanusya'];

export default function FilterBar({
  searchQuery,
  onSearchChange,
  selectedContinent,
  onContinentChange,
  onlyDifferences,
  onToggleOnlyDifferences,
  totalMatching,
  totalDestinations
}) {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2">
      <div className="bg-white dark:bg-zinc-900/80 border border-zinc-200 dark:border-zinc-800 rounded-2xl p-3 sm:p-4 shadow-xs space-y-3 transition-colors">
        {/* Top Controls Row */}
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-2.5">
          {/* Search Box with 16px font on mobile to prevent iOS auto-zoom */}
          <div className="relative flex-1">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-400 dark:text-zinc-500" />
            <input
              type="text"
              placeholder="Hedef ülke ara (Almanya, Mısır, Japonya)..."
              value={searchQuery}
              onChange={(e) => onSearchChange(e.target.value)}
              className="w-full pl-10 pr-10 py-2 sm:py-2 bg-zinc-50 dark:bg-zinc-950/80 border border-zinc-200 dark:border-zinc-800 rounded-xl text-base sm:text-sm text-zinc-900 dark:text-zinc-100 placeholder-zinc-400 dark:placeholder-zinc-500 focus:outline-hidden focus:ring-1 focus:ring-zinc-400 dark:focus:ring-zinc-600 transition-all"
            />
            {searchQuery && (
              <button
                onClick={() => onSearchChange('')}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-200 p-1"
                aria-label="Aramayı Temizle"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>

          {/* Only Differences Toggle Switch */}
          <div className="flex items-center">
            <button
              onClick={onToggleOnlyDifferences}
              className={`w-full sm:w-auto flex items-center justify-center gap-2 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-medium border transition-all ${
                onlyDifferences
                  ? 'bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-950 border-zinc-900 dark:border-zinc-100 shadow-xs'
                  : 'bg-zinc-50 dark:bg-zinc-950/80 text-zinc-600 dark:text-zinc-400 border-zinc-200 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-800/80'
              }`}
            >
              <Sparkles className={`w-3.5 h-3.5 ${onlyDifferences ? 'text-amber-300' : 'text-zinc-400 dark:text-zinc-500'}`} />
              <span>Yalnızca Farklılıklar</span>
              <span className={`text-[10px] px-1.5 py-0.2 rounded-md uppercase font-semibold ${
                onlyDifferences
                  ? 'bg-zinc-800 text-zinc-200 dark:bg-zinc-200 dark:text-zinc-900'
                  : 'bg-zinc-200/80 text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400'
              }`}>
                {onlyDifferences ? 'Açık' : 'Kapalı'}
              </span>
            </button>
          </div>
        </div>

        {/* Bottom Filters Row: Continents & Results count */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2.5 pt-2 border-t border-zinc-100 dark:border-zinc-800/60">
          {/* Continent Pills */}
          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar max-w-full pb-0.5">
            <span className="text-xs text-zinc-500 dark:text-zinc-400 font-medium mr-1 flex items-center gap-1 shrink-0">
              <Globe2 className="w-3.5 h-3.5" /> Kıta:
            </span>
            {CONTINENTS.map((continent) => {
              const isSelected = selectedContinent === continent;
              return (
                <button
                  key={continent}
                  onClick={() => onContinentChange(continent)}
                  className={`px-3 py-1 rounded-lg text-xs whitespace-nowrap transition-all ${
                    isSelected
                      ? 'bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-950 font-semibold shadow-xs'
                      : 'bg-zinc-50 dark:bg-zinc-950/80 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-800'
                  }`}
                >
                  {continent}
                </button>
              );
            })}
          </div>

          {/* Results Count Badge */}
          <div className="text-xs text-zinc-500 dark:text-zinc-400 self-end sm:self-auto shrink-0">
            <span className="font-semibold text-zinc-900 dark:text-zinc-100">{totalMatching}</span> / {totalDestinations} ülke
          </div>
        </div>
      </div>
    </div>
  );
}

