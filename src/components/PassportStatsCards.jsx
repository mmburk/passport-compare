import React from 'react';
import { X, Trophy, ChevronLeft, ChevronRight, Plus } from 'lucide-react';
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
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 sm:py-4">
      {/* Container: horizontally scrollable on mobile, grid on desktop */}
      <div className="flex overflow-x-auto no-scrollbar sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3.5 pb-1 sm:pb-0">
        {passportList.map((passport, index) => {
          const stats = PASSPORT_STATS[passport.id] || {
            free: 0,
            evisa: 0,
            voa: 0,
            required: 0,
            total: 198,
            score: 0,
            rank: 99
          };

          const freePercent = Math.round((stats.free / stats.total) * 100);
          const evisaPercent = Math.round((stats.evisa / stats.total) * 100);
          const voaPercent = Math.round((stats.voa / stats.total) * 100);
          const requiredPercent = 100 - (freePercent + evisaPercent + voaPercent);

          return (
            <div
              key={passport.id}
              className="min-w-[260px] sm:min-w-0 shrink-0 sm:shrink bg-white dark:bg-zinc-900/80 border border-zinc-200 dark:border-zinc-800/90 rounded-2xl p-3.5 sm:p-4 shadow-xs flex flex-col justify-between transition-all"
            >
              {/* Card Header & Controls */}
              <div className="flex items-start justify-between gap-2 mb-3">
                <div className="flex items-center gap-2.5">
                  {/* Passport Cover Mini Graphic */}
                  <div
                    className="w-10 h-14 rounded-md shadow-xs flex flex-col items-center justify-between p-1 text-center shrink-0 border border-white/20 relative"
                    style={{ backgroundColor: passport.coverColor }}
                  >
                    <span className="text-xs">{passport.flag}</span>
                    <span className="text-[6px] font-bold tracking-widest text-amber-200/90 uppercase">
                      PASSPORT
                    </span>
                  </div>

                  <div>
                    <h4 className="font-semibold text-zinc-900 dark:text-zinc-100 text-sm leading-snug">
                      {passport.name}
                    </h4>
                    <p className="text-[11px] text-zinc-500 dark:text-zinc-400 leading-tight mt-0.5">
                      {passport.type}
                    </p>
                    <div className="flex items-center gap-1.5 mt-1">
                      <span className="text-[10px] font-medium px-2 py-0.5 rounded-full bg-zinc-100 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 border border-zinc-200 dark:border-zinc-700/80 flex items-center gap-1">
                        <Trophy className="w-2.5 h-2.5 text-zinc-500 dark:text-zinc-400" /> #{passport.rank}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Move / Remove controls */}
                <div className="flex items-center gap-0.5">
                  {index > 0 && (
                    <button
                      onClick={() => onMoveLeft(index)}
                      title="Sola Kaydır"
                      className="p-1 rounded-md text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
                    >
                      <ChevronLeft className="w-3.5 h-3.5" />
                    </button>
                  )}
                  {index < passportList.length - 1 && (
                    <button
                      onClick={() => onMoveRight(index)}
                      title="Sağa Kaydır"
                      className="p-1 rounded-md text-zinc-400 hover:text-zinc-700 dark:hover:text-zinc-200 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors"
                    >
                      <ChevronRight className="w-3.5 h-3.5" />
                    </button>
                  )}
                  {passportList.length > 1 && (
                    <button
                      onClick={() => onRemovePassport(passport.id)}
                      title="Bu Pasaportu Kaldır"
                      className="p-1 rounded-md text-zinc-400 hover:text-rose-600 dark:hover:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/30 transition-colors"
                    >
                      <X className="w-3.5 h-3.5" />
                    </button>
                  )}
                </div>
              </div>

              {/* Progress Bar with Soft Colors */}
              <div className="my-2">
                <div className="flex justify-between text-[11px] font-medium text-zinc-600 dark:text-zinc-400 mb-1">
                  <span>Skor: <strong className="text-zinc-900 dark:text-zinc-100">{stats.score}</strong></span>
                  <span className="text-emerald-600 dark:text-emerald-400">%{freePercent} Serbest</span>
                </div>
                <div className="h-2 w-full bg-zinc-100 dark:bg-zinc-800 rounded-full overflow-hidden flex">
                  <div
                    style={{ width: `${freePercent}%` }}
                    className="bg-emerald-500 transition-all duration-300"
                    title={`Vizesiz: %${freePercent}`}
                  ></div>
                  <div
                    style={{ width: `${evisaPercent}%` }}
                    className="bg-sky-500 transition-all duration-300"
                    title={`e-Vize: %${evisaPercent}`}
                  ></div>
                  <div
                    style={{ width: `${voaPercent}%` }}
                    className="bg-amber-500 transition-all duration-300"
                    title={`Kapıda Vize: %${voaPercent}`}
                  ></div>
                  <div
                    style={{ width: `${requiredPercent}%` }}
                    className="bg-zinc-300 dark:bg-zinc-700 transition-all duration-300"
                    title={`Vize Gerekli: %${requiredPercent}`}
                  ></div>
                </div>
              </div>

              {/* 4 Stats Badges */}
              <div className="grid grid-cols-4 gap-1.5 mt-1.5 text-center">
                <div className="bg-emerald-50/60 dark:bg-emerald-950/20 border border-emerald-200/60 dark:border-emerald-800/40 rounded-xl p-1.5">
                  <div className="text-xs sm:text-sm font-semibold text-emerald-700 dark:text-emerald-400">{stats.free}</div>
                  <div className="text-[9px] text-emerald-800/80 dark:text-emerald-400/80 uppercase font-medium">Vizesiz</div>
                </div>
                <div className="bg-sky-50/60 dark:bg-sky-950/20 border border-sky-200/60 dark:border-sky-800/40 rounded-xl p-1.5">
                  <div className="text-xs sm:text-sm font-semibold text-sky-700 dark:text-sky-400">{stats.evisa}</div>
                  <div className="text-[9px] text-sky-800/80 dark:text-sky-400/80 uppercase font-medium">e-Vize</div>
                </div>
                <div className="bg-amber-50/60 dark:bg-amber-950/20 border border-amber-200/60 dark:border-amber-800/40 rounded-xl p-1.5">
                  <div className="text-xs sm:text-sm font-semibold text-amber-800 dark:text-amber-400">{stats.voa}</div>
                  <div className="text-[9px] text-amber-900/80 dark:text-amber-400/80 uppercase font-medium">Kapıda</div>
                </div>
                <div className="bg-zinc-100/70 dark:bg-zinc-800/40 border border-zinc-200 dark:border-zinc-800 rounded-xl p-1.5">
                  <div className="text-xs sm:text-sm font-semibold text-zinc-700 dark:text-zinc-300">{stats.required}</div>
                  <div className="text-[9px] text-zinc-500 uppercase font-medium">Vize</div>
                </div>
              </div>
            </div>
          );
        })}

        {/* Add Passport Quick Card */}
        <button
          onClick={onOpenAddModal}
          className="min-w-[140px] sm:min-w-0 shrink-0 sm:shrink border border-dashed border-zinc-300 dark:border-zinc-800 hover:border-zinc-400 dark:hover:border-zinc-700 rounded-2xl p-4 flex flex-col items-center justify-center text-center group hover:bg-zinc-100/50 dark:hover:bg-zinc-900/50 transition-all"
        >
          <div className="w-9 h-9 rounded-xl bg-zinc-100 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 flex items-center justify-center text-zinc-500 dark:text-zinc-400 group-hover:text-zinc-900 dark:group-hover:text-zinc-100 transition-colors mb-2">
            <Plus className="w-4 h-4" />
          </div>
          <span className="text-xs font-semibold text-zinc-700 dark:text-zinc-300 group-hover:text-zinc-900 dark:group-hover:text-white transition-colors">
            Pasaport Ekle
          </span>
          <span className="text-[10px] text-zinc-400 dark:text-zinc-500 mt-0.5">
            Yan yana kıyasla
          </span>
        </button>
      </div>
    </div>
  );
}

