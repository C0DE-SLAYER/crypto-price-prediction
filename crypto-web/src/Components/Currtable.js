import React, { useEffect, useState } from "react";
import "./Currtable.css";
function Currtable() {
  const [dataw, setData] = useState([]);
  const getPriceData = async () => {
    const res = await fetch("https://api.coincap.io/v2/assets");
    const actualdata = await res.json();
    setData(actualdata.data);
  };
  useEffect(() => {
    getPriceData();
  }, []);
  return (
    <>
      <div className="baap">
        <div className="mainc">
          <h1>Live prices</h1>
          <div>
            <table>
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Name</th>
                  <th>Price</th>
                  <th>Change% 24HR</th>
                  <th>marketCapUsd</th>
                </tr>
              </thead>
              <tbody>
                {dataw.map((currElem, ind) => {
                  return (
                    <tr key={ind}>
                      <td>{currElem.rank}</td>
                      <td>{currElem.name}</td>
                      <td>{currElem.priceUsd}</td>
                      <td>{currElem.changePercent24Hr}</td>
                      <td>{currElem.marketCapUsd}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
}

export default Currtable;
