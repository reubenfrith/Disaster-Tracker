import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
// import App from './App.jsx'
import DisasterMap from './components/disaster-map.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <DisasterMap />
  </StrictMode>,
)
