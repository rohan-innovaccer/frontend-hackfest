import React from 'react';
import Home from './pages/Home';
import Register from './pages/Register';
import Navigation from './components/Navigation';
import Notfound from './pages/Notfound';
import Sidebar from './components/Sidebar';
import Medication from './components/Medication'
import ProblemList from './components/ProblemList'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './styles.css';
import Login from './pages/Login';
import Planofcare from './components/Planofcare';

const App = () => {
  const user = true;

  return (
    <BrowserRouter>
      <div>
        <Navigation />
        <div className='main-container'>
          {user && <Sidebar />}
          <div className='content-wrapper'>
            <Routes>
              <Route path='/' exact element={<Home />} />
              <Route path='/login' element={<Login />} />
              <Route path='/register' element={<Register />} />
              <Route path='/planofcare' element={<Planofcare />} />
              <Route path='/medication' element={<Medication />} />
              <Route path='/problemList' element={<ProblemList />} />
              <Route path='/*' element={<Notfound />} />

            </Routes>
          </div>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default App;
