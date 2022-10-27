import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

function Login() {
  const [namee, setNamee] = useState("");

  const [passwe, setPasswe] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const auth = localStorage.getItem("user");
    if (auth) {
      navigate("/liveprice");
    }
  });

  const takee = async () => {
    let result = await fetch("http://localhost:5000/login", {
      method: "post",
      body: JSON.stringify({ namee, passwe }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    result = await result.json();

    if (result.name) {
      localStorage.setItem("user", JSON.stringify(result));
      navigate("/liveprice");
    } else {
      alert("please enter name ");
    }
  };
  const reset = () => {
    setNamee("");

    setPasswe("");
  };
  return (
    <div className="mainreg">
      <div className="reg">
        <h1>Login</h1>
        <input
          type="text"
          placeholder="enter name here"
          className="inpbox"
          value={namee}
          onChange={(e) => {
            setNamee(e.target.value);
          }}
        />
        <input
          type="text"
          placeholder="enter password here "
          className="inpbox"
          value={passwe}
          onChange={(e) => {
            setPasswe(e.target.value);
          }}
        />
        <div className="mb">
          <button className="apbut" type="button" onClick={takee}>
            Login
          </button>
          <button className="apbut" type="button" onClick={reset}>
            Reset
          </button>
        </div>
        <p id="pb">
          Not Have An Account <Link to="/signup">Register</Link>
        </p>
      </div>
    </div>
  );
}

export default Login;
