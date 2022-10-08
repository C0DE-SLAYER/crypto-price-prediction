import './App.css';
import Login from "./components/login";
import Register from "./components/register";
import {
  BrowserRouter as Router,
  Route,
  Routes,
} from "react-router-dom";

function App() {
  return (
  <Router>
    <Routes>
      <Route exact path='/' element={<Login/>}/>
      <Route exact path='/register' element={<Register/>}/>
      </Routes>
  </Router>
  );
}

export default App;
