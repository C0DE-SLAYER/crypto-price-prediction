import React, { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./style.css";
function Signup() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [passw, setPassw] = useState("");
  const nevigate = useNavigate();

  useEffect(() => {
    const auth = localStorage.getItem("user");
    if (auth) {
      nevigate("/liveprice");
    }
  });

  const take = async () => {
    console.log(name, email, passw);
    let result = await fetch("http://localhost:5000/register", {
      method: "post",
      body: JSON.stringify({ name, email, passw }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    result = await result.json();
    console.log(result);
    localStorage.setItem("user", JSON.stringify(result));
    if (result) {
      nevigate("/liveprice");
    }
  };

  const reset = () => {
    setName("");
    setEmail("");
    setPassw("");
  };

  return (
    <div className="mainreg">
      <div className="reg">
        <h1>Register</h1>
        <input
          type="text"
          placeholder="enter name here"
          className="inpbox"
          value={name}
          onChange={(e) => {
            setName(e.target.value);
          }}
        />
        <input
          type="text"
          placeholder="enter email here"
          className="inpbox"
          value={email}
          onChange={(e) => {
            setEmail(e.target.value);
          }}
        />
        <input
          type="text"
          placeholder="enter password here "
          className="inpbox"
          value={passw}
          onChange={(e) => {
            setPassw(e.target.value);
          }}
        />
        <div className="mb">
          <button className="apbut" type="button" onClick={take}>
            Sign up
          </button>
          <button className="apbut" type="button" onClick={reset}>
            Reset
          </button>
        </div>
        <p id="pb">
          Already have an account <Link to="/signin">Login</Link>
        </p>
      </div>
    </div>
  );
}

export default Signup;
