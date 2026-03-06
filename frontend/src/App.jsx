import { useMemo, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import Home from './pages/Home'
import VirtualTryOn from './pages/VirtualTryOn'
import AIStylistChat from './pages/AIStylistChat'
import DatasetInsights from './pages/DatasetInsights'
import About from './pages/About'

function App() {
  const [currentPage, setCurrentPage] = useState('home')

  const pageConfig = useMemo(() => ({
    home: { label: 'Home', component: <Home /> },
    tryon: { label: 'Virtual Try-On', component: <VirtualTryOn /> },
    chat: { label: 'AI Chat', component: <AIStylistChat /> },
    insights: { label: 'Dataset Insights', component: <DatasetInsights /> },
    about: { label: 'About', component: <About /> }
  }), [])

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <div className="fixed inset-0 -z-10 bg-[radial-gradient(circle_at_20%_20%,rgba(168,85,247,0.35),transparent_35%),radial-gradient(circle_at_80%_0%,rgba(34,211,238,0.25),transparent_30%),linear-gradient(#020617,#0f172a)]" />

      {/* Navigation */}
      <nav className="sticky top-0 z-30 backdrop-blur-xl border-b border-white/10 bg-slate-900/50">
        <div className="max-w-7xl mx-auto px-4 py-4 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <span className="text-xs uppercase tracking-[0.3em] text-cyan-300">AI Fashion OS</span>
            <h1 className="text-2xl font-semibold">AI Personal Stylist</h1>
          </div>
          <div className="flex flex-wrap gap-2">
            {Object.entries(pageConfig).map(([id, cfg]) => (
              <button
                key={id}
                onClick={() => setCurrentPage(id)}
                className={`px-4 py-2 rounded-full text-sm transition-all border ${
                  currentPage === id
                    ? 'bg-gradient-to-r from-fuchsia-500 to-cyan-400 text-slate-900 border-transparent shadow-lg shadow-cyan-400/30'
                    : 'bg-white/5 border-white/15 hover:bg-white/10'
                }`}
              >
                {cfg.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Page Content */}
      <div className="max-w-7xl mx-auto px-4 py-8 md:py-12">
        <AnimatePresence mode="wait">
          <motion.div
            key={currentPage}
            initial={{ opacity: 0, y: 20, filter: 'blur(8px)' }}
            animate={{ opacity: 1, y: 0, filter: 'blur(0px)' }}
            exit={{ opacity: 0, y: -12, filter: 'blur(8px)' }}
            transition={{ duration: 0.35 }}
          >
            {pageConfig[currentPage].component}
          </motion.div>
        </AnimatePresence>
      </div>
    </div>
  )
}

export default App
