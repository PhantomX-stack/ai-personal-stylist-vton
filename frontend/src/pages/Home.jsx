import { motion } from 'framer-motion'

const features = [
  { title: 'AI Skin Tone Detection', desc: 'Computer vision models identify undertones and map ideal palettes in seconds.' },
  { title: 'Body Type Estimation', desc: 'MediaPipe-assisted silhouette cues produce fit-aware style recommendations.' },
  { title: 'Recommendation Intelligence', desc: 'A weighted algorithm balances color match, trends, body fit, and mood context.' },
  { title: 'Virtual Clothing Try-On', desc: 'Upload once and preview curated looks with side-by-side transformations.' }
]

const suggestions = [
  { title: 'Urban Smart Set', style: 'Smart Casual', score: '0.912' },
  { title: 'Soft Weekend Layers', style: 'Streetwear', score: '0.884' },
  { title: 'After-Hours Edit', style: 'Party', score: '0.873' }
]

function Home() {
  return (
    <div className="space-y-10">
      <div className="relative overflow-hidden rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl p-8 md:p-12">
        <motion.div initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }} className="space-y-5">
          <span className="inline-flex px-3 py-1 rounded-full text-xs tracking-[0.2em] uppercase bg-cyan-400/20 text-cyan-200 border border-cyan-300/30">Personalized AI styling studio</span>
          <h1 className="text-4xl md:text-6xl font-bold leading-tight bg-gradient-to-r from-white via-fuchsia-200 to-cyan-200 bg-clip-text text-transparent">Dress with confidence powered by vision + fashion intelligence.</h1>
          <p className="text-slate-200 max-w-3xl text-lg">Discover your best colors, get body-aware outfit rankings, and test looks before checkout with an interactive virtual try-on experience.</p>
        </motion.div>
        <motion.div initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: 0.2 }} className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-4">
          {suggestions.map((item, idx) => (
            <motion.div key={item.title} whileHover={{ y: -6 }} transition={{ type: 'spring', stiffness: 240 }} className="rounded-2xl border border-white/15 bg-slate-900/60 p-5">
              <span className="text-xs uppercase tracking-[0.18em] text-cyan-300">Top pick #{idx + 1}</span>
              <h3 className="font-semibold text-xl mt-2">{item.title}</h3>
              <p className="text-sm text-slate-300 mt-1">{item.style}</p>
              <p className="mt-4 text-fuchsia-300 text-sm">AI Score: {item.score}</p>
            </motion.div>
          ))}
        </motion.div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {features.map((feature, idx) => (
          <motion.div key={feature.title} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: idx * 0.08 }} whileHover={{ scale: 1.02 }} className="rounded-2xl border border-white/10 bg-white/5 backdrop-blur-xl p-5">
            <h3 className="font-semibold text-lg text-fuchsia-200">{feature.title}</h3>
            <p className="text-sm text-slate-300 mt-2">{feature.desc}</p>
          </motion.div>
        ))}
      </div>
    </div>
  )
}

export default Home
