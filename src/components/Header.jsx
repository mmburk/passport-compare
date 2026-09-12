import React from 'react';
import { Plus, Sparkles, Sun, Moon, BarChart2, Award } from 'lucide-react';
import { PRESETS } from '../data';

export default function Header({
  onOpenAddModal,
  activePresetId,
  onApplyPreset,
  selectedCount,
  currentView,
  onViewChange,
  theme,
  onToggleTheme
}) {
  return (
    <header className="border-b border-zinc-200 dark:border-zinc-800/80 bg-white/80 dark:bg-zinc-950/80 backdrop-blur-md sticky top-0 z-30 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 sm:py-4">
        {/* Main Row: Logo, Actions & Tabs */}
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 sm:gap-4">
          {/* Brand & Mobile Actions Bar */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-zinc-900 dark:bg-zinc-100 text-white dark:text-zinc-950 flex items-center justify-center font-bold text-base shadow-sm border border-zinc-700/30 dark:border-zinc-300/30 shrink-0">
                <span>🛂</span>
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h1 className="text-lg sm:text-xl font-bold tracking-tight text-zinc-900 dark:text-white m-0">
                    Pasaport<span className="text-zinc-500 dark:text-zinc-400 font-normal">Kıyasla</span>
                  </h1>
                  <span className="text-[10px] font-medium tracking-wide px-2 py-0.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700">
                    198 Ülke
                  </span>
                </div>
                <p className="hidden sm:block text-xs text-zinc-500 dark:text-zinc-400 mt-0.5">
                  Yeşil, Bordo ve dünya pasaportlarının vize durumlarını yan yana karşılaştırın
                </p>
              </div>
            </div>

            {/* Mobile Theme Toggle */}
            <div className="sm:hidden flex items-center gap-2">
              <button
                onClick={onToggleTheme}
                title={theme === 'dark' ? 'Aydınlık Moda Geç' : 'Karanlık Moda Geç'}
                className="p-2 rounded-xl text-zinc-600 dark:text-zinc-300 bg-zinc-100 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 hover:bg-zinc-200 dark:hover:bg-zinc-800 transition-colors"
                aria-label="Toggle Theme"
              >
                {theme === 'dark' ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-zinc-600" />}
              </button>
            </div>
          </div>

          {/* Controls: Segmented View Switcher, Add Button & Desktop Theme Toggle */}
          <div className="flex items-center gap-2 self-stretch sm:self-auto justify-between sm:justify-end">
            {/* View Switcher Tabs */}
            <div className="flex items-center bg-zinc-100 dark:bg-zinc-900 p-1 rounded-xl border border-zinc-200 dark:border-zinc-800 flex-1 sm:flex-initial">
              <button
                onClick={() => onViewChange('table')}
                className={`flex-1 sm:flex-initial flex items-center justify-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  currentView === 'table'
                    ? 'bg-white dark:bg-zinc-800 text-zinc-900 dark:text-zinc-100 shadow-sm'
                    : 'text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100'
                }`}
              >
                <BarChart2 className="w-3.5 h-3.5" />
                <span>Kıyaslama</span>
              </button>
              <button
                onClick={() => onViewChange('ranking')}
                className={`flex-1 sm:flex-initial flex items-center justify-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  currentView === 'ranking'
                    ? 'bg-white dark:bg-zinc-800 text-zinc-900 dark:text-zinc-100 shadow-sm'
                    : 'text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100'
                }`}
              >
                <Award className="w-3.5 h-3.5" />
                <span>Sıralama</span>
              </button>
            </div>

            {/* Add Passport Button */}
            {currentView === 'table' && (
              <button
                onClick={onOpenAddModal}
                className="inline-flex items-center gap-1.5 px-3.5 py-1.5 sm:py-2 rounded-xl bg-zinc-900 dark:bg-zinc-100 hover:bg-zinc-800 dark:hover:bg-white text-white dark:text-zinc-900 text-xs sm:text-sm font-medium transition-all shadow-sm shrink-0"
              >
                <Plus className="w-3.5 h-3.5" />
                <span className="hidden xs:inline">Pasaport</span> Ekle
                <span className="ml-0.5 px-1.5 py-0.2 rounded-md bg-zinc-800 dark:bg-zinc-200 text-zinc-300 dark:text-zinc-800 text-[11px] font-mono">
                  {selectedCount}
                </span>
              </button>
            )}

            {/* Desktop Theme Switcher */}
            <button
              onClick={onToggleTheme}
              title={theme === 'dark' ? 'Aydınlık Moda Geç' : 'Karanlık Moda Geç'}
              className="hidden sm:inline-flex p-2 rounded-xl text-zinc-600 dark:text-zinc-300 bg-zinc-100 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 hover:bg-zinc-200 dark:hover:bg-zinc-800 transition-colors"
              aria-label="Toggle Theme"
            >
              {theme === 'dark' ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4 text-zinc-600" />}
            </button>
          </div>
        </div>

        {/* Quick Presets Bar & Subtle Status Legend */}
        <div className="mt-3 pt-2.5 border-t border-zinc-100 dark:border-zinc-800/60 flex flex-col md:flex-row md:items-center md:justify-between gap-2.5">
          {/* Presets Horizontal Scroll */}
          <div className="flex items-center gap-1.5 text-xs text-zinc-500 dark:text-zinc-400 overflow-x-auto no-scrollbar pb-0.5 max-w-full">
            <span className="font-medium text-zinc-700 dark:text-zinc-300 shrink-0 flex items-center gap-1 text-[11px]">
              <Sparkles className="w-3 h-3 text-zinc-400 dark:text-zinc-500" /> Hızlı:
            </span>
            {PRESETS.map((preset) => {
              const isActive = activePresetId === preset.id;
              return (
                <button
                  key={preset.id}
                  onClick={() => onApplyPreset(preset)}
                  title={preset.desc}
                  className={`px-2.5 py-1 rounded-lg text-xs whitespace-nowrap transition-all ${
                    isActive
                      ? 'bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-950 font-semibold shadow-xs'
                      : 'bg-zinc-100 dark:bg-zinc-900 hover:bg-zinc-200 dark:hover:bg-zinc-800/80 text-zinc-600 dark:text-zinc-300 border border-zinc-200/80 dark:border-zinc-800'
                  }`}
                >
                  {preset.title}
                </button>
              );
            })}
          </div>

          {/* Subdued Status Legend */}
          <div className="flex items-center gap-3 text-[11px] text-zinc-500 dark:text-zinc-400 shrink-0 self-start md:self-auto overflow-x-auto no-scrollbar">
            <div className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-emerald-500"></span>
              <span>Vizesiz</span>
            </div>
            <div className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-sky-500"></span>
              <span>e-Vize</span>
            </div>
            <div className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-amber-500"></span>
              <span>Kapıda Vize</span>
            </div>
            <div className="flex items-center gap-1.5">
              <span className="w-2 h-2 rounded-full bg-rose-500"></span>
              <span>Vize Gerekli</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
