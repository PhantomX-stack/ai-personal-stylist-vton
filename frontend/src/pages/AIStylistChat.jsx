import { useState } from 'react'

const starterMessages = [
  { role: 'assistant', text: 'Hi! I am your AI stylist. Tell me your mood and occasion for a personalized look.' }
]

function AIStylistChat() {
  const [messages, setMessages] = useState(starterMessages)
  const [input, setInput] = useState('')

  const sendMessage = () => {
    if (!input.trim()) return
    const userMessage = { role: 'user', text: input }
    const aiMessage = {
      role: 'assistant',
      text: `Style direction: ${input}. I recommend layering a statement top with tailored bottoms and one accent accessory.`
    }
    setMessages(prev => [...prev, userMessage, aiMessage])
    setInput('')
  }

  return (
    <div className="space-y-4">
      <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">
        <h1 className="text-3xl font-semibold">AI Stylist Chatbot</h1>
        <p className="text-slate-300 mt-1">Conversational style guidance powered by fashion intelligence.</p>
      </div>

      <div className="rounded-2xl border border-white/10 bg-slate-900/60 p-4 h-[480px] flex flex-col">
        <div className="flex-1 overflow-y-auto space-y-3 pr-1">
          {messages.map((msg, idx) => (
            <div key={idx} className={`max-w-[80%] px-4 py-3 rounded-2xl ${msg.role === 'user' ? 'ml-auto bg-cyan-500/20 border border-cyan-300/40' : 'bg-white/10 border border-white/10'}`}>
              {msg.text}
            </div>
          ))}
        </div>
        <div className="flex gap-2 mt-4">
          <input value={input} onChange={e => setInput(e.target.value)} onKeyDown={e => e.key === 'Enter' && sendMessage()} type="text" placeholder="Ask for styling tips..." className="flex-1 border border-white/15 bg-white/5 rounded-xl px-4 py-2 outline-none" />
          <button onClick={sendMessage} className="px-5 py-2 rounded-xl bg-gradient-to-r from-fuchsia-500 to-cyan-400 text-slate-900 font-semibold">Send</button>
        </div>
      </div>
    </div>
  )
}

export default AIStylistChat
