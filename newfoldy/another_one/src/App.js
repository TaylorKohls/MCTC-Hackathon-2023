import logo from './logo.svg';
import './App.css';
// import './ui_login_page.html';
import LoginPage from './new_login.js';
import LandingPage from './landing_page.js';
import PieChart  from './piechart';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
//changes made here 

const router = createBrowserRouter([
  {
    path: "/",
    element: < LandingPage />,   
  },
  {
    path: "/login_page",
    element: < LoginPage />,   
  },
  {
    path: "/piechart",
    element: < PieChart />,   
  },

]);



function App() {
  return (
    <RouterProvider router={router} />

  );
}

export default App;
