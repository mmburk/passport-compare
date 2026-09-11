import React from 'react';
import { Plus, Compass, Sparkles, SlidersHorizontal, CheckCircle2, Globe, FileText, AlertCircle } from 'lucide-react';
import { PRESETS } from '../data';

export default function Header({ onOpenAddModal, activePresetId, onApplyPreset, selectedCount }) {
  return (
    <header className="border-b border-slate-800 bg-slate-950/90 backdrop-blur-md sticky top-0 z-30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          {/* Brand & Logo */}
          <div className="flex items-center gap-3">
            <div className="w-11 h-11 rounded-2xl bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 p-0.5 shadow-lg shadow-indigo-500/20 flex items-center justify-center shrink-0">
              <div className="w-full h-full bg-slate-950 rounded-[14px] flex items-center justify-center text-xl">
                🛂
              </div>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-xl sm:text-2xl font-black tracking-tight text-white m-0">
                  Pasaport<span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-pink-400">Kıyasla</span>
                </h1>
                <span className="text-[10px] font-bold tracking-wider px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 uppercase">
                  Global 2026
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                Türkiye (Yeşil, Bordo) ve dünya pasaportlarının vize durumlarını yan yana karşılaştırın
              </p>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex items-center gap-2.5">
            <button
              onClick={onOpenAddModal}
              className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/25 transition-all hover:scale-[1.02] active:scale-[0.98]"
            >
              <Plus className="w-4 h-4" />
              <span>Pasaport Ekle</span>
              <span className="ml-1 px-1.5 py-0.2 rounded-md bg-black/30 text-xs font-mono">
                {selectedCount} Seçili
              </span>
            </button>
          </div>
        </div>

        {/* Quick Presets Bar */}
        <div className="mt-4 pt-3 border-t border-slate-800/80 flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-1.5 text-xs text-slate-400 overflow-x-auto pb-1 max-w-full">
            <span className="font-semibold text-slate-300 shrink-0 flex items-center gap-1">
              <Sparkles className="w-3.5 h-3.5 text-amber-400" /> Hızlı Kıyaslar:
            </span>
            {PRESETS.map((preset) => {
              const isActive = activePresetId === preset.id;
              return (
                <button
                  key={preset.id}
                  onClick={() => onApplyPreset(preset)}
                  title={preset.desc}
                  className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
                    isActive
                      ? 'bg-indigo-600/30 text-indigo-300 border border-indigo-500/50 shadow-sm'
                      : 'bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 hover:border-slate-700'
                  }`}
                >
                  {preset.title}
                </button>
              );
            })}
          </div>

          {/* 4 Colors Legend */}
          <div className="flex items-center gap-3 text-[11px] text-slate-400 bg-slate-900/80 px-3 py-1.5 rounded-xl border border-slate-800 shrink-0">
            <span className="text-slate-500 font-medium">Durum Renkleri:</span>
            <div className="flex items-center gap-1 text-emerald-400 font-medium">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 shadow-sm shadow-emerald-500/50"></span>
              <span>Vizesiz</span>
            </div>
            <div className="flex items-center gap-1 text-sky-400 font-medium">
              <span className="w-2.5 h-2.5 rounded-full bg-sky-500 shadow-sm shadow-sky-500/50"></span>
              <span>e-Vize</span>
            </div>
            <div className="flex items-center gap-1 text-amber-400 font-medium">
              <span className="w-2.5 h-2.5 rounded-full bg-amber-500 shadow-sm shadow-amber-500/50"></span>
              <span>Kapıda Vize</span>
            </div>
            <div className="flex items-center gap-1 text-rose-400 font-medium">
              <span className="w-2.5 h-2.5 rounded-full bg-rose-500 shadow-sm shadow-rose-500/50"></span>
              <span>Vize Gerekli</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
