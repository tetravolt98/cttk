import "./Address.css";
import { useState } from "react";

function Address(props) {
  return (
    <div className={"address-box"}>
      <p>
        {props.address} ({props.balance ? `${props.balance} BTC` : "Loading..."}
        ) <button onClick={() => props.delete(props.address)}>delete</button>
        <button onClick={() => props.transactions(props.address)}>
          transactions
        </button>
      </p>
    </div>
  );
}

export default Address;
