import { useMemo, useState } from 'react'
import { motion } from 'framer-motion'

const garments = [
  { id: 'navy_shirt', name: 'Navy Signature Shirt', category: 'top', accent: 'from-blue-500 to-cyan-300' },
  { id: 'black_hoodie', name: 'Graphite Structured Hoodie', category: 'top', accent: 'from-zinc-700 to-zinc-500' },
  { id: 'beige_chinos', name: 'Beige Smart Chinos', category: 'bottom', accent: 'from-amber-300 to-orange-200' },
  { id: 'blue_jeans', name: 'Indigo Tapered Denim', category: 'bottom', accent: 'from-indigo-500 to-blue-400' }
]

function VirtualTryOn() {
  const [originalImage, setOriginalImage] = useState(null)
  const [selectedId, setSelectedId] = useState('navy_shirt')
  const [slider, setSlider] = useState(56)
  const selectedGarment = garments.find(item => item.id === selectedId)
  const styledImage = useMemo(() => originalImage, [originalImage])
  const handleUpload = (event) => {
    const file = event.target.files?.[0]
    if (!file) return
    const reader = new FileReader()
    reader.onload = (e) => setOriginalImage(e.target?.result)
    reader.readAsDataURL(file)
  }
  return (
    <div className="space-y-6">
      <div className="rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl p-6 md:p-8">
        <h1 className="text-3xl font-semibold">Virtual Try-On Studio</h1>
        <p className="text-slate-300 mt-2">Upload a selfie, pick a garment, then compare before/after styling with a live slider.</p>
      </div>
      <div className="grid lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 rounded-2xl border border-white/10 bg-slate-900/60 p-5">
          {!originalImage ? (
            <div className="h-[430px] border-2 border-dashed border-white/20 rounded-2xl flex flex-col items-center justify-center text-center cursor-pointer">
              <h3 className="text-xl font-medium">Upload your selfie</h3>
              <p className="text-slate-300 mt-2">PNG / JPG recommended</p>
              <input type="file" accept="image/*" className="hidden" onChange={handleUpload} />
            </div>
          ) : (
            <div className="space-y-4">
              <div className="relative h-[430px] rounded-2xl overflow-hidden border border-white/10">
                <img src={originalImage} alt="Original" className="absolute inset-0 w-full h-full object-cover" />
                <div className="absolute inset-0 overflow-hidden" style={{ width: `${slider}%` }}>
                  <img src={styledImage} alt="Styled" className="w-full h-full object-cover saturate-125 contrast-110" />
                  <div className="absolute inset-0 bg-gradient-to-r from-cyan-400/10 to-fuchsia-400/30" />
                </div>
                <span className="absolute top-3 left-3 text-xs px-2 py-1 rounded-full bg-black/50">After</span>
                <span className="absolute top-3 right-3 text-xs px-2 py-1 rounded-full bg-black/50">Before</span>
              </div>
              <p className="text-sm text-slate-300">Before / After slider: {slider}%</p>
              <input type="range" min="5" max="95" value={slider} onChange={(event) => setSlider(Number(event.target.value))} className="w-full mt-2" />
            </div>
          )}
        </div>
        <div className="space-y-4">
          <div className="rounded-2xl border border-white/10 bg-white/5 p-4">
            <h3 className="font-semibold text-lg">AI Analysis Panel</h3>
            <div className="text-sm mt-3 space-y-2 text-slate-300">
              <p>Skin tone: <span className="text-white">Warm Neutral</span></p>
              <p>Body type: <span className="text-white">Athletic</span></p>
              <p>Trend alignment: <span className="text-white">High (0.88)</span></p>
              <p>Recommended mood: <span className="text-white">Smart casual</span></p>
            </div>
          </div>
          <div className="grid gap-3">
            {garments.map(item => (
              <motion.div key={item.id} whileHover={{ y: -3 }} onClick={() => setSelectedId(item.id)} className={`text-left rounded-xl p-4 border ${selectedId === item.id ? 'border-cyan-300 bg-cyan-400/10' : 'border-white/10 bg-white/5'}`}>
                <div className={`h-2 rounded-full bg-gradient-to-r ${item.accent}`} />
                <h4 className="font-medium mt-3">{item.name}</h4>
                <p className="text-xs text-slate-300 mt-1 uppercase tracking-widest">{item.category}</p>
              </motion.div>
            ))}
          </div>
          {originalImage && (
            <label className="block text-center text-sm py-2 rounded-lg border border-white/20 hover:bg-white/10 cursor-pointer">
              Upload another image
              <input type="file" accept="image/*" className="hidden" onChange={handleUpload} />
            </label>
          )}
          <p className="text-xs text-slate-400">Active garment: {selectedGarment?.name}</p>
        </div>
      </div>
    </div>
  )
}
export default VirtualTryOn
