const topColors = [
  { name: 'Black', score: 94 },
  { name: 'White', score: 92 },
  { name: 'Navy', score: 86 },
  { name: 'Grey', score: 84 },
  { name: 'Olive', score: 81 }
]

const combinations = [
  { combo: 'Shirt + Trousers', popularity: 90 },
  { combo: 'Blazer + Trousers', popularity: 86 },
  { combo: 'Hoodie + Cargo', popularity: 82 },
  { combo: 'Top + Skirt', popularity: 80 }
]

const seasonal = [
  { season: 'Spring', smartCasual: 84, streetwear: 75, relaxed: 88 },
  { season: 'Summer', smartCasual: 80, streetwear: 67, relaxed: 95 },
  { season: 'Fall', smartCasual: 89, streetwear: 90, relaxed: 70 },
  { season: 'Winter', smartCasual: 91, streetwear: 92, relaxed: 51 }
]

function ProgressRow({ label, value, color }) {
  return (
    <div>
      <div className="flex justify-between text-sm mb-1">
        <span>{label}</span>
        <span>{value}%</span>
      </div>
      <div className="h-2 rounded-full bg-white/10 overflow-hidden">
        <div className={`h-full ${color}`} style={{ width: `${value}%` }} />
      </div>
    </div>
  )
}

function DatasetInsights() {
  return (
    <div className="space-y-6">
      <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">
        <h1 className="text-3xl font-semibold">Dataset Insights</h1>
        <p className="text-slate-300 mt-2">Analytics blended from DeepFashion, Fashion-MNIST, and Polyvore derived trend signals.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {[
          { label: 'DeepFashion items', value: '800K+' },
          { label: 'Fashion-MNIST items', value: '70K' },
          { label: 'Polyvore outfits', value: '21K+' }
        ].map(item => (
          <div key={item.label} className="rounded-2xl border border-white/10 bg-slate-900/60 p-5">
            <p className="text-sm text-slate-300">{item.label}</p>
            <p className="text-3xl font-semibold mt-2 text-cyan-200">{item.value}</p>
          </div>
        ))}
      </div>

      <div className="grid lg:grid-cols-2 gap-6">
        <div className="rounded-2xl border border-white/10 bg-slate-900/60 p-4 space-y-4">
          <h2 className="font-semibold">Top Fashion Colors</h2>
          {topColors.map(item => (
            <ProgressRow key={item.name} label={item.name} value={item.score} color="bg-cyan-400" />
          ))}
        </div>

        <div className="rounded-2xl border border-white/10 bg-slate-900/60 p-4 space-y-4">
          <h2 className="font-semibold">Popular Outfit Combinations</h2>
          {combinations.map(item => (
            <ProgressRow key={item.combo} label={item.combo} value={item.popularity} color="bg-fuchsia-400" />
          ))}
        </div>
      </div>

      <div className="rounded-2xl border border-white/10 bg-slate-900/60 p-4 overflow-x-auto">
        <h2 className="font-semibold mb-4">Seasonal Style Trends</h2>
        <table className="w-full text-sm min-w-[420px]">
          <thead>
            <tr className="text-slate-300 border-b border-white/10">
              <th className="text-left py-2">Season</th>
              <th className="text-left py-2">Smart Casual</th>
              <th className="text-left py-2">Streetwear</th>
              <th className="text-left py-2">Relaxed</th>
            </tr>
          </thead>
          <tbody>
            {seasonal.map(row => (
              <tr key={row.season} className="border-b border-white/5">
                <td className="py-2">{row.season}</td>
                <td className="py-2">{row.smartCasual}%</td>
                <td className="py-2">{row.streetwear}%</td>
                <td className="py-2">{row.relaxed}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default DatasetInsights
