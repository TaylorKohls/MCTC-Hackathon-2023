import logo from './logo.svg';
import './App.css';
// import './ui_login_page.html';
import LoginPage from './new_login.js';
import HomePage from './home_page.js';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
//changes made here 

const router = createBrowserRouter([
  {
    path: "/",
    element: < LoginPage />,   
  },
  {
    path: "/home",
    element: < HomePage />,   
  },
]);



function App() {
  return (
    <RouterProvider router={router} />

  );
}

export default App;
