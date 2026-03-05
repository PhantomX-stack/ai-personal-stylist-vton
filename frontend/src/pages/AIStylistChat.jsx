function AIStylistChat() {
  return (
    <div className="space-y-8">
      <h1 className="text-4xl font-bold text-gray-800">AI Stylist Chat</h1>
      <div className="bg-white rounded-xl p-6 shadow-lg h-96 flex flex-col">
        <div className="flex-1 overflow-y-auto mb-4 space-y-4">
          <div className="bg-gray-100 p-4 rounded-lg max-w-xs">Hi! Ask me about style tips</div>
        </div>
        <div className="flex gap-2">
          <input type="text" placeholder="Ask me anything..." className="flex-1 border rounded-lg px-4 py-2" />
          <button className="bg-purple-600 text-white px-6 py-2 rounded-lg">Send</button>
        </div>
      </div>
    </div>
  )
}
export default AIStylistChat
