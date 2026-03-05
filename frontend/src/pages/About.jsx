function About() {
  return (
    <div className="space-y-8">
      <h1 className="text-4xl font-bold text-gray-800">About AI Personal Stylist</h1>
      <div className="bg-white rounded-xl p-8 shadow-lg space-y-4">
        <h2 className="text-2xl font-bold text-purple-600 mb-4">Our Mission</h2>
        <p className="text-gray-700 leading-relaxed">
          To revolutionize personal fashion by leveraging AI and computer vision to provide personalized style recommendations and virtual try-on experiences.
        </p>
        <h2 className="text-2xl font-bold text-purple-600 mb-4 mt-6">Technologies</h2>
        <ul className="text-gray-700 space-y-2">
          <li>• OpenCV for computer vision and body pose detection</li>
          <li>• TensorFlow for ML-based outfit recommendations</li>
          <li>• React & TailwindCSS for modern responsive UI</li>
          <li>• FastAPI for scalable backend services</li>
        </ul>
      </div>
    </div>
  )
}
export default About
