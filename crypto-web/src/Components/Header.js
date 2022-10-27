import React, { useState } from "react";
import "./Header.css";
import { Link, useNavigate } from "react-router-dom";
export default function Header() {
  const [active, setActive] = useState("nav_menu");
  const [logo, setLogo] = useState("nav_togg");
  const navigate = useNavigate();
  const auth = localStorage.getItem("user");

  const navt = () => {
    active === "nav_menu"
      ? setActive("nav_menu nav_active")
      : setActive("nav_menu");

    logo === "nav_togg" ? setLogo("nav_togg togg") : setLogo("nav_togg");
  };

  const logout = () => {
    localStorage.clear();
    navigate("/signup");
  };

  return (
    <>
      <div className="cont">
        <div className="logo">
          <h1>Crypto-currency-prediction</h1>
        </div>
        <div className="menu">
          <ul className={active}>
            <Link to="/liveprice">
              <li>
                <button className="but">Current Prices</button>
              </li>
            </Link>
            <Link to="/prediction">
              <li>
                <button className="but">Prediction</button>
              </li>
            </Link>
            <li>
              {auth ? (
                <Link to="/signup">
                  <button className="but" onClick={logout}>
                    Logout
                  </button>
                </Link>
              ) : (
                <Link to="/signup">
                  <button className="but">Register / Login</button>
                </Link>
              )}
            </li>
          </ul>

          <div onClick={navt} className={logo}>
            <div className="item1"></div>
            <div className="item2"></div>
            <div className="item3"></div>
          </div>
        </div>
      </div>
    </>
  );
}
