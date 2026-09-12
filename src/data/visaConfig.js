export const VISA_STATUS_CONFIG = {
  free: {
    id: 'free',
    label: 'Vizesiz',
    shortLabel: 'Vizesiz',
    color: 'emerald',
    badgeClass: 'bg-emerald-50 text-emerald-700 border-emerald-200/80 hover:bg-emerald-100/80 dark:bg-emerald-950/30 dark:text-emerald-300 dark:border-emerald-800/50 dark:hover:bg-emerald-900/40',
    dotClass: 'bg-emerald-500 dark:bg-emerald-400',
    headerBg: 'bg-emerald-600 dark:bg-emerald-500',
    description: 'Vizesiz doğrudan giriş veya kimlikle giriş hakkı'
  },
  evisa: {
    id: 'evisa',
    label: 'e-Vize / ETA',
    shortLabel: 'e-Vize',
    color: 'sky',
    badgeClass: 'bg-sky-50 text-sky-700 border-sky-200/80 hover:bg-sky-100/80 dark:bg-sky-950/30 dark:text-sky-300 dark:border-sky-800/50 dark:hover:bg-sky-900/40',
    dotClass: 'bg-sky-500 dark:bg-sky-400',
    headerBg: 'bg-sky-600 dark:bg-sky-500',
    description: 'Seyahat öncesi internetten alınan elektronik onay (e-Vize / ETA)'
  },
  voa: {
    id: 'voa',
    label: 'Kapıda Vize',
    shortLabel: 'Kapıda Vize',
    color: 'amber',
    badgeClass: 'bg-amber-50 text-amber-800 border-amber-200/80 hover:bg-amber-100/80 dark:bg-amber-950/30 dark:text-amber-300 dark:border-amber-800/50 dark:hover:bg-amber-900/40',
    dotClass: 'bg-amber-500 dark:bg-amber-400',
    headerBg: 'bg-amber-600 dark:bg-amber-500',
    description: 'Havalimanı veya sınır kapısında harç ödenerek alınan vize'
  },
  required: {
    id: 'required',
    label: 'Vize Gerekli',
    shortLabel: 'Vize Gerekli',
    color: 'rose',
    badgeClass: 'bg-rose-50 text-rose-700 border-rose-200/80 hover:bg-rose-100/80 dark:bg-rose-950/30 dark:text-rose-300 dark:border-rose-800/50 dark:hover:bg-rose-900/40',
    dotClass: 'bg-rose-500 dark:bg-rose-400',
    headerBg: 'bg-rose-600 dark:bg-rose-500',
    description: 'Konsolosluk veya aracı kurumdan vize başvurusu zorunlu'
  }
};
