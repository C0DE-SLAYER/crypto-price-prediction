import React, { useState, useEffect } from "react";
import "./prediction.css";
function Prediction() {
  const [myCar, setMyCar] = useState("");
  const [dataw, setData] = useState([]);
  const [value, setValue] = useState(1);
  const [predic, setPredic] = useState([]);

  const handleChange = (event) => {
    setMyCar(event.target.value);
  };
  const min = 1;
  const max = 365;

  const handleChangee = (event) => {
    const value = Math.max(min, Math.min(max, Number(event.target.value)));
    setValue(value);
    getpridict();
  };

  const getPriceData = async () => {
    const res = await fetch("https://api.coincap.io/v2/assets");
    const actualdata = await res.json();
    setData(actualdata.data);
  };

  const getpridict = async () => {
    console.log(myCar, value);
    const res1 = await fetch(
      `https://cryptopricepredict.herokuapp.com/predict?coin_name=${myCar}&days=${value}`
    );

    const hab = await res1.json();
    console.log(hab.price);
    setPredic(hab.price);
  };

  useEffect(() => {
    getPriceData();
  }, []);

  return (
    <div className="mainco">
      <div className="disp">
        <form className="formm">
          <p className="pre">please select the currency for prediction</p>
          <select className="sel" value={myCar} onChange={handleChange}>
            {dataw.map((cure, ind) => {
              return (
                <option key={ind} value={cure.symbol}>
                  {cure.symbol}
                </option>
              );
            })}
          </select>
          <p className="pre">please enter number of days to predict</p>
          <input
            className="ipo"
            type="number"
            placeholder="Select no of days"
            value={value}
            onChange={handleChangee}
          />

          <p className="mh">
            predicted price is :-
            {predic}
          </p>
        </form>
      </div>
    </div>
  );
}

export default Prediction;
