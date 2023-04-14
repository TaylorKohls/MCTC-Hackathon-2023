import logo from './logo.svg';
import './App.css';
// import './ui_login_page.html';
import LoginPage from './new_login.js';
import HomePage from './home_page.js';
import {BrowserRouter, Routes, Route} from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login_page" element={<LoginPage />}/>
        <Route path="/home_page" element={<HomePage />} /> 
          
      </Routes>
    </BrowserRouter>


  );
}

export default App;
