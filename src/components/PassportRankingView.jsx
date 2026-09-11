import React, { useState, useMemo } from 'react';
import { Search, Trophy, Medal, ArrowUpDown, Plus, Check, Globe2, Sparkles, X, ChevronRight } from 'lucide-react';
import { PASSPORTS, PASSPORT_STATS } from '../data';

export default function PassportRankingView({
  selectedPassportIds,
  onAddPassport,
  onRemovePassport,
  onSwitchToTable
}) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedRegion, setSelectedRegion] = useState('Tümü');
  const [sortBy, setSortBy] = useState('rank'); // 'rank' | 'free' | 'name'

  const regions = ['Tümü', 'Avrupa', 'Asya', 'Amerika', 'Afrika', 'Okyanusya'];

  // Process and sort all passports with their stats
  const rankedPassports = useMemo(() => {
    let list = PASSPORTS.map((p) => {
      const stats = PASSPORT_STATS[p.id] || {
        free: 0,
        evisa: 0,
        voa: 0,
        required: 0,
        total: 198,
        accessScore: 0,
        score: 0,
        rank: 99
      };
      return {
        ...p,
        stats
      };
    });

    // 1. Search Filter
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase().trim();
      list = list.filter(
        (p) =>
          p.name.toLowerCase().includes(q) ||
          p.country.toLowerCase().includes(q) ||
          p.fullName.toLowerCase().includes(q) ||
          p.type.toLowerCase().includes(q)
      );
    }

    // 2. Region Filter
    if (selectedRegion !== 'Tümü') {
      list = list.filter((p) => p.continent && p.continent.includes(selectedRegion));
    }

    // 3. Sorting
    list.sort((a, b) => {
      if (sortBy === 'free') {
        return b.stats.free - a.stats.free;
      }
      if (sortBy === 'name') {
        return a.name.localeCompare(b.name, 'tr');
      }
      // default: rank ascending
      return a.stats.rank - b.stats.rank;
    });

    return list;
  }, [searchQuery, selectedRegion, sortBy]);

  const getRankBadge = (rank) => {
    if (rank === 1) {
      return (
        <span className="w-8 h-8 rounded-full bg-gradient-to-tr from-amber-500 to-yellow-300 text-slate-950 font-black text-sm flex items-center justify-center shadow-lg shadow-amber-500/30 ring-2 ring-yellow-300/50">
          🥇
        </span>
      );
    }
    if (rank === 2) {
      return (
        <span className="w-8 h-8 rounded-full bg-gradient-to-tr from-slate-300 to-slate-100 text-slate-950 font-black text-sm flex items-center justify-center shadow-lg shadow-slate-300/30 ring-2 ring-slate-200/50">
          🥈
        </span>
      );
    }
    if (rank === 3) {
      return (
        <span className="w-8 h-8 rounded-full bg-gradient-to-tr from-amber-700 to-amber-500 text-white font-black text-sm flex items-center justify-center shadow-lg shadow-amber-700/30 ring-2 ring-amber-600/50">
          🥉
        </span>
      );
    }
    return (
      <span className="w-8 h-8 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs flex items-center justify-center border border-slate-700">
        #{rank}
      </span>
    );
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
      {/* Page Title & Hero */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 border border-slate-800 p-6 sm:p-8 shadow-2xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 relative z-10">
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-xs font-bold uppercase tracking-wider mb-3">
              <Trophy className="w-3.5 h-3.5 text-amber-400" /> Küresel Pasaport Güç Endeksi
            </div>
            <h2 className="text-2xl sm:text-3xl font-black text-white tracking-tight">
              Dünya Pasaport Sıralaması (198 Ülke)
            </h2>
            <p className="text-sm text-slate-400 mt-2 max-w-2xl leading-relaxed">
              Tüm pasaportların dünya çapında vizesiz, kapıda vize ve e-vize erişim haklarına göre hesaplanan gerçek zamanlı sıralaması. İstediğiniz pasaportu arayabilir ve tek tıkla kıyaslamaya ekleyebilirsiniz.
            </p>
          </div>

          {/* Quick Go to Table button */}
          <div className="shrink-0 flex items-center gap-3">
            <button
              onClick={onSwitchToTable}
              className="px-5 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm shadow-xl shadow-indigo-600/30 flex items-center gap-2 transition-all hover:scale-[1.02] active:scale-[0.98]"
            >
              <span>Karşılaştırma Tablosuna Dön</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* Search & Filter Controls */}
      <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-4">
        <div className="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3">
          {/* Search Input */}
          <div className="relative flex-1">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
            <input
              type="text"
              placeholder="Pasaport veya ülke ara (Örn: Türkiye, Yeşil, Almanya, Japonya, Singapur, ABD)..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-10 pr-10 py-2.5 bg-slate-950/80 border border-slate-700/80 rounded-xl text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>

          {/* Sort By Dropdown */}
          <div className="flex items-center gap-2 shrink-0">
            <span className="text-xs text-slate-400 flex items-center gap-1 font-medium">
              <ArrowUpDown className="w-3.5 h-3.5 text-indigo-400" /> Sırala:
            </span>
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="bg-slate-950/80 border border-slate-700/80 text-xs text-slate-200 rounded-xl px-3 py-2.5 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all cursor-pointer font-medium"
            >
              <option value="rank">Küresel Sıralamaya Göre (#1 ➔ #59)</option>
              <option value="free">En Çok Vizesiz Ülke Sayısına Göre</option>
              <option value="name">Ülke Adına Göre (A ➔ Z)</option>
            </select>
          </div>
        </div>

        {/* Region Filter Pills */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 pt-3 border-t border-slate-800/80">
          <div className="flex items-center gap-1.5 overflow-x-auto max-w-full pb-1">
            <span className="text-xs text-slate-500 font-medium mr-1 flex items-center gap-1 shrink-0">
              <Globe2 className="w-3.5 h-3.5" /> Bölge:
            </span>
            {regions.map((region) => {
              const isSelected = selectedRegion === region;
              return (
                <button
                  key={region}
                  onClick={() => setSelectedRegion(region)}
                  className={`px-3 py-1 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
                    isSelected
                      ? 'bg-indigo-600 text-white font-semibold shadow-md shadow-indigo-600/30'
                      : 'bg-slate-950/60 hover:bg-slate-800 text-slate-400 hover:text-slate-200 border border-slate-800'
                  }`}
                >
                  {region}
                </button>
              );
            })}
          </div>

          <div className="text-xs text-slate-400 shrink-0">
            <span className="font-bold text-indigo-400">{rankedPassports.length}</span> pasaport listeleniyor
          </div>
        </div>
      </div>

      {/* Ranking List */}
      <div className="space-y-3">
        {rankedPassports.map((passport) => {
          const isSelected = selectedPassportIds.includes(passport.id);
          const { free, evisa, voa, required, total, score, rank } = passport.stats;

          const freePercent = Math.round((free / total) * 100);
          const evisaPercent = Math.round((evisa / total) * 100);
          const voaPercent = Math.round((voa / total) * 100);
          const requiredPercent = 100 - (freePercent + evisaPercent + voaPercent);

          return (
            <div
              key={passport.id}
              className={`p-4 sm:p-5 rounded-2xl border transition-all ${
                isSelected
                  ? 'bg-slate-900/90 border-indigo-500/40 shadow-lg shadow-indigo-500/5'
                  : 'bg-slate-950/70 border-slate-800/90 hover:border-slate-700/80 hover:bg-slate-900/40'
              }`}
            >
              <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
                {/* Left: Rank & Passport Info */}
                <div className="flex items-center gap-4">
                  {/* Rank Badge */}
                  <div className="shrink-0 flex items-center justify-center">
                    {getRankBadge(rank)}
                  </div>

                  {/* Passport Mini Cover Graphic */}
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
                    <span className="text-[6px] font-black tracking-widest text-amber-300/90 uppercase">
                      PASSPORT
                    </span>
                  </div>

                  {/* Name & Subtitle */}
                  <div>
                    <div className="flex items-center gap-2 flex-wrap">
                      <h3 className="text-base sm:text-lg font-bold text-white leading-snug">
                        {passport.name}
                      </h3>
                      {passport.id.startsWith('TR_') && (
                        <span className="text-[10px] font-black px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                          TÜRKİYE ÖZEL
                        </span>
                      )}
                      <span className="text-xs text-slate-400 font-normal">
                        ({passport.country})
                      </span>
                    </div>
                    <p className="text-xs text-slate-400 mt-0.5">{passport.fullName}</p>
                    <div className="text-[11px] text-slate-500 mt-1">
                      {passport.continent} • {passport.type}
                    </div>
                  </div>
                </div>

                {/* Middle: Progress Bar & 4 Colors Breakdown */}
                <div className="lg:w-80 xl:w-96 shrink-0 space-y-2">
                  <div className="flex justify-between text-xs font-semibold text-slate-300">
                    <span className="flex items-center gap-1.5">
                      <span className="text-emerald-400 font-bold text-sm">{free + voa}</span> Ülke Kolay Erişim
                    </span>
                    <span className="text-slate-400">Skor: {score}</span>
                  </div>

                  {/* 4 Colors Segmented Progress Bar */}
                  <div className="h-3 w-full bg-slate-800 rounded-full overflow-hidden flex shadow-inner">
                    <div
                      style={{ width: `${freePercent}%` }}
                      className="bg-emerald-500 hover:opacity-90 transition-all"
                      title={`Vizesiz: ${free} ülke (%${freePercent})`}
                    ></div>
                    <div
                      style={{ width: `${evisaPercent}%` }}
                      className="bg-sky-500 hover:opacity-90 transition-all"
                      title={`e-Vize: ${evisa} ülke (%${evisaPercent})`}
                    ></div>
                    <div
                      style={{ width: `${voaPercent}%` }}
                      className="bg-amber-500 hover:opacity-90 transition-all"
                      title={`Kapıda Vize: ${voa} ülke (%${voaPercent})`}
                    ></div>
                    <div
                      style={{ width: `${requiredPercent}%` }}
                      className="bg-rose-500 hover:opacity-90 transition-all"
                      title={`Vize Gerekli: ${required} ülke (%${requiredPercent})`}
                    ></div>
                  </div>

                  {/* 4 Tiny Status Pills */}
                  <div className="grid grid-cols-4 gap-1.5 text-center text-[10px]">
                    <div className="bg-emerald-950/40 border border-emerald-500/30 rounded-lg py-1 px-1 text-emerald-400 font-bold">
                      {free} <span className="font-normal text-[9px] block text-emerald-300/80">Vizesiz</span>
                    </div>
                    <div className="bg-sky-950/40 border border-sky-500/30 rounded-lg py-1 px-1 text-sky-400 font-bold">
                      {evisa} <span className="font-normal text-[9px] block text-sky-300/80">e-Vize</span>
                    </div>
                    <div className="bg-amber-950/40 border border-amber-500/30 rounded-lg py-1 px-1 text-amber-400 font-bold">
                      {voa} <span className="font-normal text-[9px] block text-amber-300/80">Kapıda</span>
                    </div>
                    <div className="bg-rose-950/40 border border-rose-500/30 rounded-lg py-1 px-1 text-rose-400 font-bold">
                      {required} <span className="font-normal text-[9px] block text-rose-300/80">Vize</span>
                    </div>
                  </div>
                </div>

                {/* Right: Compare Action Button */}
                <div className="shrink-0 flex items-center justify-end">
                  {isSelected ? (
                    <button
                      onClick={() => onRemovePassport(passport.id)}
                      className="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 hover:bg-rose-500/20 hover:text-rose-300 hover:border-rose-500/40 transition-all flex items-center gap-1.5 group"
                    >
                      <Check className="w-3.5 h-3.5 text-indigo-400 group-hover:hidden" />
                      <X className="w-3.5 h-3.5 text-rose-400 hidden group-hover:block" />
                      <span className="group-hover:hidden">Kıyaslanıyor</span>
                      <span className="hidden group-hover:inline">Kaldır</span>
                    </button>
                  ) : (
                    <button
                      onClick={() => onAddPassport(passport.id)}
                      className="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-indigo-600 text-slate-200 hover:text-white border border-slate-700 hover:border-transparent transition-all flex items-center gap-1.5 shadow-md"
                    >
                      <Plus className="w-3.5 h-3.5" />
                      <span>Kıyaslamaya Ekle</span>
                    </button>
                  )}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
