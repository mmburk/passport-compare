# Python script to generate React components
import os

components = {}

# 1. AddPassportModal.jsx
components['src/components/AddPassportModal.jsx'] = '''import React, { useState } from 'react';
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
'''

# 2. Header.jsx
components['src/components/Header.jsx'] = '''import React from 'react';
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
'''

# 3. PassportStatsCards.jsx
components['src/components/PassportStatsCards.jsx'] = '''import React from 'react';
import { X, ArrowLeftRight, Trophy, ShieldCheck, Check, Sparkles, ChevronLeft, ChevronRight } from 'lucide-react';
import { PASSPORTS, PASSPORT_STATS } from '../data';

export default function PassportStatsCards({
  selectedIds,
  onRemovePassport,
  onMoveLeft,
  onMoveRight,
  onOpenAddModal
}) {
  const passportList = selectedIds.map(id => PASSPORTS.find(p => p.id === id)).filter(Boolean);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {passportList.map((passport, index) => {
          const stats = PASSPORT_STATS[passport.id] || {
            free: 0,
            evisa: 0,
            voa: 0,
            required: 0,
            total: 108,
            score: 0
          };

          const freePercent = Math.round((stats.free / stats.total) * 100);
          const evisaPercent = Math.round((stats.evisa / stats.total) * 100);
          const voaPercent = Math.round((stats.voa / stats.total) * 100);
          const requiredPercent = 100 - (freePercent + evisaPercent + voaPercent);

          return (
            <div
              key={passport.id}
              className="relative bg-gradient-to-b from-slate-900/90 to-slate-950/90 border border-slate-800 hover:border-slate-700/80 rounded-2xl p-4 shadow-xl shadow-black/40 flex flex-col justify-between transition-all group"
            >
              {/* Card Header & Controls */}
              <div className="flex items-start justify-between gap-2 mb-3">
                <div className="flex items-center gap-3">
                  {/* Passport Cover Mini Graphic */}
                  <div
                    className="w-12 h-16 rounded-lg shadow-lg flex flex-col items-center justify-between p-1.5 text-center shrink-0 border relative overflow-hidden"
                    style={{
                      backgroundColor: passport.coverColor,
                      borderColor: 'rgba(255,255,255,0.2)',
                      boxShadow: '0 8px 16px -4px rgba(0,0,0,0.5)'
                    }}
                  >
                    <div className="absolute inset-x-0 top-0 h-1 bg-gradient-to-r from-transparent via-white/30 to-transparent"></div>
                    <span className="text-sm drop-shadow">{passport.flag}</span>
                    <div className="w-5 h-5 rounded-full border border-amber-400/40 flex items-center justify-center my-auto">
                      <span className="text-[7px] text-amber-300">★</span>
                    </div>
                    <span className="text-[6px] font-black tracking-widest text-amber-300/90 uppercase">
                      PASSPORT
                    </span>
                  </div>

                  <div>
                    <div className="flex items-center gap-1.5 flex-wrap">
                      <h4 className="font-bold text-slate-100 text-sm sm:text-base leading-tight">
                        {passport.name}
                      </h4>
                    </div>
                    <p className="text-[11px] text-slate-400 leading-tight mt-0.5">
                      {passport.type}
                    </p>
                    <div className="flex items-center gap-1.5 mt-1">
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 border border-amber-500/20 flex items-center gap-1">
                        <Trophy className="w-2.5 h-2.5" /> Sıralama: #{passport.rank}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Move / Remove controls */}
                <div className="flex items-center gap-1">
                  {index > 0 && (
                    <button
                      onClick={() => onMoveLeft(index)}
                      title="Sola Kaydır"
                      className="p-1 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
                    >
                      <ChevronLeft className="w-3.5 h-3.5" />
                    </button>
                  )}
                  {index < passportList.length - 1 && (
                    <button
                      onClick={() => onMoveRight(index)}
                      title="Sağa Kaydır"
                      className="p-1 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
                    >
                      <ChevronRight className="w-3.5 h-3.5" />
                    </button>
                  )}
                  {passportList.length > 1 && (
                    <button
                      onClick={() => onRemovePassport(passport.id)}
                      title="Bu Pasaportu Kaldır"
                      className="p-1 rounded-md text-slate-400 hover:text-rose-400 hover:bg-rose-950/40 transition-colors"
                    >
                      <X className="w-3.5 h-3.5" />
                    </button>
                  )}
                </div>
              </div>

              {/* Progress Bar with the 4 Colors */}
              <div className="my-2">
                <div className="flex justify-between text-[11px] font-semibold text-slate-300 mb-1">
                  <span>Erişim Skoru: {stats.score}</span>
                  <span className="text-emerald-400">{freePercent}% Serbest</span>
                </div>
                <div className="h-2.5 w-full bg-slate-800 rounded-full overflow-hidden flex shadow-inner">
                  <div
                    style={{ width: `${freePercent}%` }}
                    className="bg-emerald-500 transition-all duration-500"
                    title={`Vizesiz: %${freePercent}`}
                  ></div>
                  <div
                    style={{ width: `${evisaPercent}%` }}
                    className="bg-sky-500 transition-all duration-500"
                    title={`e-Vize: %${evisaPercent}`}
                  ></div>
                  <div
                    style={{ width: `${voaPercent}%` }}
                    className="bg-amber-500 transition-all duration-500"
                    title={`Kapıda Vize: %${voaPercent}`}
                  ></div>
                  <div
                    style={{ width: `${requiredPercent}%` }}
                    className="bg-rose-500 transition-all duration-500"
                    title={`Vize Gerekli: %${requiredPercent}`}
                  ></div>
                </div>
              </div>

              {/* 4 Stats Badges */}
              <div className="grid grid-cols-4 gap-1.5 mt-2 text-center">
                <div className="bg-emerald-950/40 border border-emerald-500/30 rounded-xl p-1.5">
                  <div className="text-xs sm:text-sm font-bold text-emerald-400">{stats.free}</div>
                  <div className="text-[9px] text-emerald-300/80 uppercase font-semibold">Vizesiz</div>
                </div>
                <div className="bg-sky-950/40 border border-sky-500/30 rounded-xl p-1.5">
                  <div className="text-xs sm:text-sm font-bold text-sky-400">{stats.evisa}</div>
                  <div className="text-[9px] text-sky-300/80 uppercase font-semibold">e-Vize</div>
                </div>
                <div className="bg-amber-950/40 border border-amber-500/30 rounded-xl p-1.5">
                  <div className="text-xs sm:text-sm font-bold text-amber-400">{stats.voa}</div>
                  <div className="text-[9px] text-amber-300/80 uppercase font-semibold">Kapıda</div>
                </div>
                <div className="bg-rose-950/40 border border-rose-500/30 rounded-xl p-1.5">
                  <div className="text-xs sm:text-sm font-bold text-rose-400">{stats.required}</div>
                  <div className="text-[9px] text-rose-300/80 uppercase font-semibold">Vize</div>
                </div>
              </div>
            </div>
          );
        })}

        {/* Add Passport Quick Card */}
        <button
          onClick={onOpenAddModal}
          className="border-2 border-dashed border-slate-800 hover:border-indigo-500/60 rounded-2xl p-6 flex flex-col items-center justify-center text-center group hover:bg-indigo-500/5 transition-all min-h-[160px]"
        >
          <div className="w-11 h-11 rounded-2xl bg-slate-900 group-hover:bg-indigo-600/20 border border-slate-800 group-hover:border-indigo-500/40 flex items-center justify-center text-slate-400 group-hover:text-indigo-400 transition-colors mb-2">
            <X className="w-5 h-5 rotate-45" />
          </div>
          <span className="text-sm font-bold text-slate-300 group-hover:text-white transition-colors">
            + Başka Pasaport Ekle
          </span>
          <span className="text-xs text-slate-500 mt-1">
            Almanya, ABD, Singapur veya diğerlerini yan yana ekle
          </span>
        </button>
      </div>
    </div>
  );
}
'''

# 4. FilterBar.jsx
components['src/components/FilterBar.jsx'] = '''import React from 'react';
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
'''

# 5. ComparisonTable.jsx
components['src/components/ComparisonTable.jsx'] = '''import React from 'react';
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
'''

# 6. CountryDetailModal.jsx
components['src/components/CountryDetailModal.jsx'] = '''import React from 'react';
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
'''

# 7. App.jsx
components['src/App.jsx'] = '''import React, { useState, useMemo } from 'react';
import Header from './components/Header';
import PassportStatsCards from './components/PassportStatsCards';
import FilterBar from './components/FilterBar';
import ComparisonTable from './components/ComparisonTable';
import AddPassportModal from './components/AddPassportModal';
import CountryDetailModal from './components/CountryDetailModal';
import { DESTINATIONS, PRESETS } from './data';

export default function App() {
  // Defaults: Türkiye Bordo, Türkiye Yeşil, Almanya (3 sütun)
  const [selectedPassportIds, setSelectedPassportIds] = useState(['TR_BORDO', 'TR_YESIL', 'DE']);
  const [activePresetId, setActivePresetId] = useState('tr_vs_eu');
  
  // Filters
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedContinent, setSelectedContinent] = useState('Tümü');
  const [onlyDifferences, setOnlyDifferences] = useState(false);
  const [statusFilter, setStatusFilter] = useState('all');

  // Modals
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [selectedCountryDetail, setSelectedCountryDetail] = useState(null);

  // Passport Management
  const handleAddPassport = (passportId) => {
    if (!selectedPassportIds.includes(passportId)) {
      setSelectedPassportIds([...selectedPassportIds, passportId]);
      setActivePresetId(null);
    }
  };

  const handleRemovePassport = (passportId) => {
    if (selectedPassportIds.length > 1) {
      setSelectedPassportIds(selectedPassportIds.filter(id => id !== passportId));
      setActivePresetId(null);
    }
  };

  const handleMoveLeft = (index) => {
    if (index > 0) {
      const copy = [...selectedPassportIds];
      const temp = copy[index - 1];
      copy[index - 1] = copy[index];
      copy[index] = temp;
      setSelectedPassportIds(copy);
      setActivePresetId(null);
    }
  };

  const handleMoveRight = (index) => {
    if (index < selectedPassportIds.length - 1) {
      const copy = [...selectedPassportIds];
      const temp = copy[index + 1];
      copy[index + 1] = copy[index];
      copy[index] = temp;
      setSelectedPassportIds(copy);
      setActivePresetId(null);
    }
  };

  const handleApplyPreset = (preset) => {
    setSelectedPassportIds(preset.passportIds);
    setActivePresetId(preset.id);
  };

  // Filter destinations
  const filteredDestinations = useMemo(() => {
    return DESTINATIONS.filter((dest) => {
      // 1. Search Query
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase().trim();
        const matchName = dest.name.toLowerCase().includes(q);
        const matchEn = dest.nameEn.toLowerCase().includes(q);
        if (!matchName && !matchEn) return false;
      }

      // 2. Continent
      if (selectedContinent !== 'Tümü' && dest.continent !== selectedContinent) {
        return false;
      }

      // 3. Only Differences
      if (onlyDifferences && selectedPassportIds.length > 1) {
        const statuses = selectedPassportIds.map(
          pid => (dest.visas[pid] ? dest.visas[pid].status : 'required')
        );
        const allSame = statuses.every(s => s === statuses[0]);
        if (allSame) return false;
      }

      return true;
    });
  }, [DESTINATIONS, searchQuery, selectedContinent, onlyDifferences, selectedPassportIds]);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      {/* Header with Nav, Presets and Color Legend */}
      <Header
        onOpenAddModal={() => setIsAddModalOpen(true)}
        activePresetId={activePresetId}
        onApplyPreset={handleApplyPreset}
        selectedCount={selectedPassportIds.length}
      />

      {/* Top Passport Stats & Progress Summary Cards */}
      <PassportStatsCards
        selectedIds={selectedPassportIds}
        onRemovePassport={handleRemovePassport}
        onMoveLeft={handleMoveLeft}
        onMoveRight={handleMoveRight}
        onOpenAddModal={() => setIsAddModalOpen(true)}
      />

      {/* Filter and Search Bar */}
      <FilterBar
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        selectedContinent={selectedContinent}
        onContinentChange={setSelectedContinent}
        onlyDifferences={onlyDifferences}
        onToggleOnlyDifferences={() => setOnlyDifferences(!onlyDifferences)}
        statusFilter={statusFilter}
        onStatusFilterChange={setStatusFilter}
        totalMatching={filteredDestinations.length}
        totalDestinations={DESTINATIONS.length}
      />

      {/* Main Comparison Table */}
      <main className="flex-1 pb-16">
        <ComparisonTable
          destinations={filteredDestinations}
          selectedIds={selectedPassportIds}
          onSelectCountry={setSelectedCountryDetail}
          onRemovePassport={handleRemovePassport}
        />
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-800 bg-slate-950 py-8 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
          <p>© 2026 Pasaport Kıyaslama Platformu • Vize serbestliği ve seyahat gereksinimleri</p>
          <div className="flex items-center gap-4 text-slate-400">
            <span>Türkiye (Bordo & Yeşil)</span>
            <span>•</span>
            <span>Schengen Bölgesi</span>
            <span>•</span>
            <span>Global Karşılaştırma</span>
          </div>
        </div>
      </footer>

      {/* Modals */}
      <AddPassportModal
        isOpen={isAddModalOpen}
        onClose={() => setIsAddModalOpen(false)}
        selectedIds={selectedPassportIds}
        onAddPassport={handleAddPassport}
      />

      <CountryDetailModal
        country={selectedCountryDetail}
        selectedIds={selectedPassportIds}
        onClose={() => setSelectedCountryDetail(null)}
      />
    </div>
  );
}
'''

# Write all components
for path, content in components.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Wrote: {path}')

print('All components built successfully!')
