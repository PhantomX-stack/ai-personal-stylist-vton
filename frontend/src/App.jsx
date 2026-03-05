import { useState } from 'react'
import { motion } from 'framer-motion'
import Home from './pages/Home'
import VirtualTryOn from './pages/VirtualTryOn'
import AIStylistChat from './pages/AIStylistChat'
import DatasetInsights from './pages/DatasetInsights'
import About from './pages/About'

function App() {
  const [currentPage, setCurrentPage] = useState('home')

  const pages = {
    home: <Home />,
    tryon: <VirtualTryOn />,
    chat: <AIStylistChat />,
    insights: <DatasetInsights />,
    about: <About />
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-blue-50 to-cyan-50">
      {/* Navigation */}
      <nav className="bg-white shadow-lg">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold bg-gradient-to-r from-purple-600 to-cyan-600 bg-clip-text text-transparent">
            AI Stylist
          </h1>
          <div className="flex gap-4">
            {[
              { id: 'home', label: 'Home' },
              { id: 'tryon', label: 'Try-On' },
              { id: 'chat', label: 'Chat' },
              { id: 'insights', label: 'Insights' },
              { id: 'about', label: 'About' }
            ].map(item => (
              <button
                key={item.id}
                onClick={() => setCurrentPage(item.id)}
                className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                  currentPage === item.id
                    ? 'bg-gradient-to-r from-purple-600 to-cyan-600 text-white'
                    : 'text-gray-700 hover:bg-gray-100'
                }`}
              >
                {item.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Page Content */}
      <motion.div
        key={currentPage}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
        className="max-w-7xl mx-auto px-4 py-8"
      >
        {pages[currentPage]}
      </motion.div>
    </div>
  )
}

export default App
