export const VISA_STATUS_CONFIG = {
  free: {
    id: 'free',
    label: 'Vizesiz',
    shortLabel: 'Vizesiz',
    color: 'emerald',
    badgeClass: 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 hover:bg-emerald-500/25',
    dotClass: 'bg-emerald-400',
    headerBg: 'bg-emerald-500',
    description: 'Vizesiz doğrudan giriş veya kimlikle giriş hakkı'
  },
  evisa: {
    id: 'evisa',
    label: 'e-Vize / ETA',
    shortLabel: 'e-Vize',
    color: 'sky',
    badgeClass: 'bg-sky-500/15 text-sky-400 border border-sky-500/30 hover:bg-sky-500/25',
    dotClass: 'bg-sky-400',
    headerBg: 'bg-sky-500',
    description: 'Seyahat öncesi internetten alınan elektronik onay (e-Vize / ETA)'
  },
  voa: {
    id: 'voa',
    label: 'Kapıda Vize',
    shortLabel: 'Kapıda Vize',
    color: 'amber',
    badgeClass: 'bg-amber-500/15 text-amber-300 border border-amber-500/30 hover:bg-amber-500/25',
    dotClass: 'bg-amber-400',
    headerBg: 'bg-amber-500',
    description: 'Havalimanı veya sınır kapısında harç ödenerek alınan vize'
  },
  required: {
    id: 'required',
    label: 'Vize Gerekli',
    shortLabel: 'Vize Gerekli',
    color: 'rose',
    badgeClass: 'bg-rose-500/15 text-rose-400 border border-rose-500/30 hover:bg-rose-500/25',
    dotClass: 'bg-rose-400',
    headerBg: 'bg-rose-500',
    description: 'Konsolosluk veya aracı kurumdan vize başvurusu zorunlu'
  }
};
