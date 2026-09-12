import React, { useState, useMemo, useEffect } from 'react';
import Header from './components/Header';
import PassportStatsCards from './components/PassportStatsCards';
import FilterBar from './components/FilterBar';
import ComparisonTable from './components/ComparisonTable';
import PassportRankingView from './components/PassportRankingView';
import AddPassportModal from './components/AddPassportModal';
import CountryDetailModal from './components/CountryDetailModal';
import { DESTINATIONS, PRESETS } from './data';

export default function App() {
  // Theme state: 'dark' or 'light'
  const [theme, setTheme] = useState(() => {
    const saved = localStorage.getItem('theme');
    if (saved) return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  });

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => (prev === 'dark' ? 'light' : 'dark'));
  };

  // View state: 'table' or 'ranking'
  const [currentView, setCurrentView] = useState('table');

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
    setCurrentView('table');
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
    <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 flex flex-col transition-colors duration-200">
      {/* Header with Nav, Presets and View Switcher */}
      <Header
        onOpenAddModal={() => setIsAddModalOpen(true)}
        activePresetId={activePresetId}
        onApplyPreset={handleApplyPreset}
        selectedCount={selectedPassportIds.length}
        currentView={currentView}
        onViewChange={setCurrentView}
        theme={theme}
        onToggleTheme={toggleTheme}
      />

      {/* Main Content: Table or Ranking */}
      {currentView === 'ranking' ? (
        <main className="flex-1 pb-16">
          <PassportRankingView
            selectedPassportIds={selectedPassportIds}
            onAddPassport={handleAddPassport}
            onRemovePassport={handleRemovePassport}
            onSwitchToTable={() => setCurrentView('table')}
          />
        </main>
      ) : (
        <>
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
        </>
      )}

      {/* Footer */}
      <footer className="border-t border-zinc-200 dark:border-zinc-800 bg-white/60 dark:bg-zinc-950/60 backdrop-blur py-8 text-center text-xs text-zinc-500 dark:text-zinc-400">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
          <p>© 2026 Pasaport Kıyaslama Platformu • Vize serbestliği ve seyahat gereksinimleri</p>
          <div className="flex items-center gap-3 text-zinc-400 dark:text-zinc-500">
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
