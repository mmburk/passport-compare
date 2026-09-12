import React, { useState, useMemo } from 'react';
import { Search, Trophy, ArrowUpDown, Plus, Check, Globe2, X, ChevronRight } from 'lucide-react';
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
        <span className="w-8 h-8 rounded-xl bg-amber-100 dark:bg-amber-950/40 text-amber-900 dark:text-amber-300 font-bold text-sm flex items-center justify-center border border-amber-300 dark:border-amber-800/60 shadow-xs">
          🥇
        </span>
      );
    }
    if (rank === 2) {
      return (
        <span className="w-8 h-8 rounded-xl bg-zinc-200 dark:bg-zinc-800 text-zinc-800 dark:text-zinc-200 font-bold text-sm flex items-center justify-center border border-zinc-300 dark:border-zinc-700 shadow-xs">
          🥈
        </span>
      );
    }
    if (rank === 3) {
      return (
        <span className="w-8 h-8 rounded-xl bg-amber-50 dark:bg-amber-950/20 text-amber-900 dark:text-amber-400 font-bold text-sm flex items-center justify-center border border-amber-200 dark:border-amber-800/40 shadow-xs">
          🥉
        </span>
      );
    }
    return (
      <span className="w-8 h-8 rounded-xl bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 font-medium text-xs flex items-center justify-center border border-zinc-200 dark:border-zinc-700">
        #{rank}
      </span>
    );
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 sm:py-6 space-y-4 sm:space-y-6">
      {/* Page Title & Hero */}
      <div className="relative overflow-hidden rounded-3xl bg-white dark:bg-zinc-900/80 border border-zinc-200 dark:border-zinc-800 p-5 sm:p-7 shadow-xs">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 relative z-10">
          <div>
            <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700 text-xs font-medium uppercase tracking-wider mb-2">
              <Trophy className="w-3 h-3 text-zinc-500 dark:text-zinc-400" /> Küresel Pasaport Sıralaması
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-zinc-900 dark:text-white tracking-tight">
              Dünya Pasaport Sıralaması (198 Ülke)
            </h2>
            <p className="text-xs sm:text-sm text-zinc-500 dark:text-zinc-400 mt-1 max-w-2xl leading-relaxed">
              Pasaportların küresel vizesiz, kapıda vize ve e-vize erişim gücüne göre hesaplanan güncel sıralaması. İstediğiniz ülkeyi arayabilir ve tek tıkla kıyaslamaya ekleyebilirsiniz.
            </p>
          </div>

          {/* Quick Go to Table button */}
          <div className="shrink-0 flex items-center">
            <button
              onClick={onSwitchToTable}
              className="w-full sm:w-auto px-4 py-2 sm:py-2.5 rounded-xl bg-zinc-900 dark:bg-zinc-100 hover:bg-zinc-800 dark:hover:bg-white text-white dark:text-zinc-900 font-medium text-xs sm:text-sm shadow-xs flex items-center justify-center gap-1.5 transition-all"
            >
              <span>Kıyaslama Tablosuna Dön</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* Search & Filter Controls */}
      <div className="bg-white dark:bg-zinc-900/80 border border-zinc-200 dark:border-zinc-800 rounded-2xl p-3 sm:p-4 shadow-xs space-y-3">
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-2.5">
          {/* Search Input */}
          <div className="relative flex-1">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-400 dark:text-zinc-500" />
            <input
              type="text"
              placeholder="Pasaport veya ülke ara (Türkiye, Almanya, Japonya, ABD)..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-10 pr-10 py-2 sm:py-2 bg-zinc-50 dark:bg-zinc-950/80 border border-zinc-200 dark:border-zinc-800 rounded-xl text-base sm:text-sm text-zinc-900 dark:text-zinc-100 placeholder-zinc-400 dark:placeholder-zinc-500 focus:outline-hidden focus:ring-1 focus:ring-zinc-400 dark:focus:ring-zinc-600 transition-all"
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-200 p-1"
                aria-label="Temizle"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>

          {/* Sort By Dropdown */}
          <div className="flex items-center gap-2 shrink-0">
            <span className="text-xs text-zinc-500 dark:text-zinc-400 flex items-center gap-1 font-medium">
              <ArrowUpDown className="w-3.5 h-3.5" /> Sırala:
            </span>
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="bg-zinc-50 dark:bg-zinc-950/80 border border-zinc-200 dark:border-zinc-800 text-xs text-zinc-900 dark:text-zinc-200 rounded-xl px-2.5 py-2 focus:outline-hidden focus:ring-1 focus:ring-zinc-400 transition-all cursor-pointer font-medium"
            >
              <option value="rank">Küresel Sıralama (#1 ➔ #59)</option>
              <option value="free">En Çok Vizesiz Olanlar</option>
              <option value="name">Ülke Adı (A ➔ Z)</option>
            </select>
          </div>
        </div>

        {/* Region Filter Pills */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2.5 pt-2 border-t border-zinc-100 dark:border-zinc-800/60">
          <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar max-w-full pb-0.5">
            <span className="text-xs text-zinc-500 dark:text-zinc-400 font-medium mr-1 flex items-center gap-1 shrink-0">
              <Globe2 className="w-3.5 h-3.5" /> Bölge:
            </span>
            {regions.map((region) => {
              const isSelected = selectedRegion === region;
              return (
                <button
                  key={region}
                  onClick={() => setSelectedRegion(region)}
                  className={`px-3 py-1 rounded-lg text-xs whitespace-nowrap transition-all ${
                    isSelected
                      ? 'bg-zinc-900 text-white dark:bg-zinc-100 dark:text-zinc-950 font-semibold shadow-xs'
                      : 'bg-zinc-50 dark:bg-zinc-950/80 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-600 dark:text-zinc-400 border border-zinc-200 dark:border-zinc-800'
                  }`}
                >
                  {region}
                </button>
              );
            })}
          </div>

          <div className="text-xs text-zinc-500 dark:text-zinc-400 shrink-0 self-end sm:self-auto">
            <span className="font-semibold text-zinc-900 dark:text-zinc-100">{rankedPassports.length}</span> pasaport listeleniyor
          </div>
        </div>
      </div>

      {/* Ranking List */}
      <div className="space-y-2.5">
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
              className={`p-3.5 sm:p-4 rounded-2xl border transition-all ${
                isSelected
                  ? 'bg-zinc-50/80 dark:bg-zinc-900 border-zinc-400 dark:border-zinc-700 shadow-xs'
                  : 'bg-white dark:bg-zinc-900/60 border-zinc-200 dark:border-zinc-800 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50/50 dark:hover:bg-zinc-900/80'
              }`}
            >
              <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3 sm:gap-4">
                {/* Left: Rank & Passport Info */}
                <div className="flex items-center gap-3">
                  {/* Rank Badge */}
                  <div className="shrink-0 flex items-center justify-center">
                    {getRankBadge(rank)}
                  </div>

                  {/* Passport Mini Cover Graphic */}
                  <div
                    className="w-10 h-14 rounded-md shadow-xs flex flex-col items-center justify-between p-1 text-center shrink-0 border border-white/20 relative"
                    style={{ backgroundColor: passport.coverColor }}
                  >
                    <span className="text-xs">{passport.flag}</span>
                    <span className="text-[6px] font-bold tracking-widest text-amber-200/90 uppercase">
                      PASSPORT
                    </span>
                  </div>

                  {/* Name & Subtitle */}
                  <div className="min-w-0">
                    <div className="flex items-center gap-1.5 flex-wrap">
                      <h3 className="text-sm sm:text-base font-semibold text-zinc-900 dark:text-zinc-100 leading-snug">
                        {passport.name}
                      </h3>
                      {passport.id.startsWith('TR_') && (
                        <span className="text-[9px] font-semibold px-1.5 py-0.2 rounded bg-red-50 dark:bg-red-950/40 text-red-700 dark:text-red-300 border border-red-200 dark:border-red-800/60">
                          TÜRKİYE
                        </span>
                      )}
                      <span className="text-xs text-zinc-400 dark:text-zinc-500 font-normal">
                        ({passport.country})
                      </span>
                    </div>
                    <p className="text-[11px] text-zinc-500 dark:text-zinc-400 mt-0.5 truncate">{passport.fullName}</p>
                    <div className="text-[10px] text-zinc-400 dark:text-zinc-500 mt-0.5">
                      {passport.continent} • {passport.type}
                    </div>
                  </div>
                </div>

                {/* Middle: Progress Bar & 4 Colors Breakdown */}
                <div className="lg:w-80 xl:w-96 shrink-0 space-y-1.5">
                  <div className="flex justify-between text-xs font-medium text-zinc-600 dark:text-zinc-400">
                    <span className="flex items-center gap-1">
                      <span className="text-emerald-700 dark:text-emerald-400 font-semibold">{free + voa}</span> Ülke Kolay Erişim
                    </span>
                    <span>Skor: <strong className="text-zinc-900 dark:text-zinc-100">{score}</strong></span>
                  </div>

                  {/* 4 Colors Segmented Progress Bar */}
                  <div className="h-2 w-full bg-zinc-100 dark:bg-zinc-800 rounded-full overflow-hidden flex">
                    <div
                      style={{ width: `${freePercent}%` }}
                      className="bg-emerald-500 transition-all duration-300"
                      title={`Vizesiz: ${free} ülke (%${freePercent})`}
                    ></div>
                    <div
                      style={{ width: `${evisaPercent}%` }}
                      className="bg-sky-500 transition-all duration-300"
                      title={`e-Vize: ${evisa} ülke (%${evisaPercent})`}
                    ></div>
                    <div
                      style={{ width: `${voaPercent}%` }}
                      className="bg-amber-500 transition-all duration-300"
                      title={`Kapıda Vize: ${voa} ülke (%${voaPercent})`}
                    ></div>
                    <div
                      style={{ width: `${requiredPercent}%` }}
                      className="bg-zinc-300 dark:bg-zinc-700 transition-all duration-300"
                      title={`Vize Gerekli: ${required} ülke (%${requiredPercent})`}
                    ></div>
                  </div>

                  {/* 4 Tiny Status Pills */}
                  <div className="grid grid-cols-4 gap-1 text-center text-[10px]">
                    <div className="bg-emerald-50/70 dark:bg-emerald-950/20 border border-emerald-200/60 dark:border-emerald-800/40 rounded-md py-0.5 text-emerald-800 dark:text-emerald-400 font-semibold">
                      {free} <span className="font-normal text-[9px] block text-emerald-700/80 dark:text-emerald-400/80">Vizesiz</span>
                    </div>
                    <div className="bg-sky-50/70 dark:bg-sky-950/20 border border-sky-200/60 dark:border-sky-800/40 rounded-md py-0.5 text-sky-800 dark:text-sky-400 font-semibold">
                      {evisa} <span className="font-normal text-[9px] block text-sky-700/80 dark:text-sky-400/80">e-Vize</span>
                    </div>
                    <div className="bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200/60 dark:border-amber-800/40 rounded-md py-0.5 text-amber-900 dark:text-amber-400 font-semibold">
                      {voa} <span className="font-normal text-[9px] block text-amber-800/80 dark:text-amber-400/80">Kapıda</span>
                    </div>
                    <div className="bg-zinc-100 dark:bg-zinc-800/40 border border-zinc-200 dark:border-zinc-800 rounded-md py-0.5 text-zinc-700 dark:text-zinc-300 font-semibold">
                      {required} <span className="font-normal text-[9px] block text-zinc-500">Vize</span>
                    </div>
                  </div>
                </div>

                {/* Right: Compare Action Button */}
                <div className="shrink-0 flex items-center justify-end">
                  {isSelected ? (
                    <button
                      onClick={() => onRemovePassport(passport.id)}
                      className="w-full sm:w-auto px-3.5 py-1.5 rounded-xl text-xs font-medium bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-300 dark:border-zinc-700 hover:bg-rose-50 hover:text-rose-600 dark:hover:bg-rose-950/30 dark:hover:text-rose-400 dark:hover:border-rose-800 transition-all flex items-center justify-center gap-1.5 group"
                    >
                      <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 group-hover:hidden" />
                      <X className="w-3.5 h-3.5 text-rose-500 hidden group-hover:block" />
                      <span className="group-hover:hidden">Kıyaslanıyor</span>
                      <span className="hidden group-hover:inline">Kaldır</span>
                    </button>
                  ) : (
                    <button
                      onClick={() => onAddPassport(passport.id)}
                      className="w-full sm:w-auto px-3.5 py-1.5 rounded-xl text-xs font-medium bg-zinc-900 dark:bg-zinc-100 hover:bg-zinc-800 dark:hover:bg-white text-white dark:text-zinc-900 border border-transparent transition-all flex items-center justify-center gap-1.5 shadow-xs"
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

