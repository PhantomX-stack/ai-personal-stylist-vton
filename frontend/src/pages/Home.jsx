import { motion } from 'framer-motion'

function Home() {
  return (
    <div className="space-y-12">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center py-12"
      >
        <h1 className="text-5xl font-bold bg-gradient-to-r from-purple-600 via-pink-600 to-cyan-600 bg-clip-text text-transparent mb-4">
          AI Personal Stylist
        </h1>
        <p className="text-2xl text-gray-600 mb-8">
          Your AI-powered virtual fashion consultant
        </p>
        <p className="text-lg text-gray-500 max-w-2xl mx-auto">
          Analyze your style, get personalized outfit recommendations, and try clothes virtually before you buy.
        </p>
      </motion.div>

      {/* Features Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {[
          { title: 'Skin Tone Analysis', desc: 'AI detects your skin tone and recommends colors' },
          { title: 'Body Type Estimation', desc: 'Smart pose analysis for outfit fit' },
          { title: 'Mood Recognition', desc: 'Personalized suggestions based on occasion' },
          { title: 'Virtual Try-On', desc: '3D rendering of outfits on your body' }
        ].map((feature, idx) => (
          <motion.div
            key={idx}
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: idx * 0.1 }}
            className="bg-white rounded-xl p-6 shadow-lg hover:shadow-xl transition-shadow"
          >
            <h3 className="text-lg font-bold text-purple-600 mb-2">{feature.title}</h3>
            <p className="text-gray-600">{feature.desc}</p>
          </motion.div>
        ))}
      </div>

      {/* CTA Section */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="bg-gradient-to-r from-purple-600 to-cyan-600 rounded-2xl p-12 text-white text-center"
      >
        <h2 className="text-3xl font-bold mb-4">Ready to Get Styled?</h2>
        <p className="text-lg mb-6">Upload your photo and let AI help you find your perfect style</p>
      </motion.div>
    </div>
  )
}

export default Home
