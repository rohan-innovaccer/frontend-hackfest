import React from 'react';
import Home from './pages/Home';
import Register from './pages/Register';
import Navigation from './components/Navigation';
import NotFound from './pages/NotFound';
import Sidebar from './components/Sidebar';
import Medication from './pages/Medication';
import ProblemList from './pages/ProblemList';
import PastHistory from './pages/PastHistory';
import PlanOfCare from './pages/PlanOfCare';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Documents from './pages/Documents';
import Login from './pages/Login';
import Prescription from './pages/ePrescription';
import Diagnostic from './pages/Diagnostic';
import './styles.css';



const App = () => {
  const user = false;

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
              <Route path='/planofcare' element={<PlanOfCare />} />
              <Route path='/medication' element={<Medication />} />
              <Route path='/problemList' element={<ProblemList />} />
              <Route path='/past-history' element={<PastHistory />} />
              <Route path='/documents' element={<Documents />} />
              <Route path='/diagnostic' element={<Diagnostic />} />
              <Route path='/pastHistory' element={<PastHistory />} />
              <Route path='/ePrescription' element={<Prescription />} />
              <Route path='/*' element={<NotFound />} />
              
            </Routes>
          </div>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default App;
