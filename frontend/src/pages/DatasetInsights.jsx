function DatasetInsights() {
  return (
    <div className="space-y-8">
      <h1 className="text-4xl font-bold text-gray-800">Dataset Insights</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {[
          { title: 'Total Items', value: '50K+' },
          { title: 'Body Types', value: '6' },
          { title: 'Skin Tones', value: '12' }
        ].map((stat, idx) => (
          <div key={idx} className="bg-white rounded-xl p-6 shadow-lg text-center">
            <h3 className="text-gray-600 mb-2">{stat.title}</h3>
            <p className="text-4xl font-bold text-purple-600">{stat.value}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
export default DatasetInsights
