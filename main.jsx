import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './src/App'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import 'react-toastify/dist/ReactToastify.css';


import { ToastContainer } from 'react-toastify'
import Chat from './src/Chat'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    
    <div className='container'>
    <ToastContainer/>
    <Chat />
    
    </div>
  </React.StrictMode>,
)
