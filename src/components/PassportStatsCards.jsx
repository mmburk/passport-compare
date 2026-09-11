import React from 'react';
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
