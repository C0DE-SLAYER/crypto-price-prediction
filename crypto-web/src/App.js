import "./App.css";
import Header from "./Components/Header";
import Signup from "./Components/Signup";
import Currtable from "./Components/Currtable";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Prediction from "./Components/Prediction";
import Login from "./Components/Login";
import PrivateC from "./Components/PrivateC";
import Logout from "./Components/Logout";

function App() {
  return (
    <>
      <BrowserRouter>
        <Header />
        <Routes>
          <Route element={<PrivateC />}>
            <Route path="/liveprice" element={<Currtable />}></Route>
            <Route path="/prediction" element={<Prediction />}></Route>
          </Route>
          <Route path="/signup" element={<Signup />}></Route>
          <Route path="/signin" element={<Login />}></Route>
          <Route path="/logout" element={<Logout />}></Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
