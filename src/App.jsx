import React from 'react';
import Home from './pages/Home';
import Register from './pages/Register';
import Sidebar from './components/Sidebar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './styles.css';
import Login from './pages/Login';
import Planofcare from './components/Planofcare';

const App = () => {
  return (
    <BrowserRouter>
      <div>
        <nav className='navigation'>
          <div className='logo'>
            <span>in</span>record 🚀
          </div>
          <ul className='list'>
            <li className='list-item'>About us</li>
            <li className='list-item'>Login</li>
          </ul>
        </nav>
        <div className='main-container'>
          <Sidebar />
          <div className='content-wrapper'>
            <Routes>
              <Route path='/' exact element={<Home />} />
              <Route path='/login' element={<Login />} />
              <Route path='/register' element={<Register />} />
              <Route path='/planofcare' element={<Planofcare />} />
            </Routes>
          </div>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default App;
