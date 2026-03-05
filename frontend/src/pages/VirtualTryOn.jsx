import { useState } from 'react'

function VirtualTryOn() {
  const [image, setImage] = useState(null)
  const [selected, setSelected] = useState('top')

  const handleUpload = (e) => {
    const file = e.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onload = (e) => setImage(e.target?.result)
      reader.readAsDataURL(file)
    }
  }

  return (
    <div className="space-y-8">
      <h1 className="text-4xl font-bold text-gray-800">Virtual Try-On</h1>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="space-y-4">
          <div className="bg-gray-200 rounded-xl w-full h-96 flex items-center justify-center">
            {image ? (
              <img src={image} alt="Try-on" className="w-full h-full object-cover rounded-xl" />
            ) : (
              <label className="cursor-pointer text-center">
                <p className="text-gray-600 mb-2">Click to upload your photo</p>
                <input type="file" onChange={handleUpload} accept="image/*" className="hidden" />
              </label>
            )}
          </div>
          <div className="flex gap-2">
            {['top', 'bottom', 'dress'].map(type => (
              <button
                key={type}
                onClick={() => setSelected(type)}
                className={`flex-1 py-2 rounded-lg font-semibold ${
                  selected === type ? 'bg-purple-600 text-white' : 'bg-gray-200'
                }`}
              >
                {type.charAt(0).toUpperCase() + type.slice(1)}
              </button>
            ))}
          </div>
        </div>
        <div className="space-y-4">
          <h2 className="text-2xl font-bold">Select Clothing</h2>
          <div className="grid grid-cols-2 gap-4">
            {[1, 2, 3, 4].map(i => (
              <div key={i} className="bg-gray-200 rounded-lg h-40 flex items-center justify-center text-gray-600">
                <p>Clothing {i}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

export default VirtualTryOn
