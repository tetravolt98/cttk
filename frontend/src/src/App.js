import "./App.css";
import { useEffect, useState } from "react";
import Address from "./components/Address";
import axios from "axios";
import address from "./components/Address";

function App() {
  const [addresses, setAddresses] = useState([]);
  const [balances, setBalances] = useState({});
  const [newAddress, setNewAddress] = useState("");
  const [errorMsg, setErrorMsg] = useState("");

  const fetchBalance = async (address) => {
    try {
      const response = await axios.get(
        `http://localhost:5000/api/v1/transactions/${address}/balance`,
      );
      setBalances((prevBalances) => ({
        ...prevBalances,
        [address]: response.data.balance,
      }));
    } catch (error) {
      console.error(`Error fetching balance for ${address}:`, error);
    }
  };

  useEffect(() => {
    const fetchAddresses = async () => {
      try {
        const response = await axios.get(
          "http://localhost:5000/api/v1/addresses",
        );
        setAddresses(response.data.addresses);
        await Promise.all(response.data.addresses.map(fetchBalance));
        setErrorMsg("");
      } catch (error) {
        console.error("Error fetching addresses:", error);
        setErrorMsg(error.response.data.error);
      }
    };

    fetchAddresses();
  }, []);

  const handleAddAddress = async () => {
    if (addresses.includes(newAddress)) {
      setErrorMsg("Address already exists");
      return;
    }
    try {
      await axios.post(`http://localhost:5000/api/v1/addresses/${newAddress}`);
      setAddresses([...addresses, newAddress]);
      setNewAddress("");
      setErrorMsg("");
    } catch (error) {
      console.error("Error adding address:", error);
      setErrorMsg(error.response.data.error);
    }
  };

  const handleViewTransactions = (address) => {
    const transactionsUrl = `http://localhost:5000/api/v1/transactions/${address}?page=1`;
    window.open(transactionsUrl, "_blank");
  };

  const handleDeleteAddress = async (address) => {
    try {
      await axios.delete(`http://localhost:5000/api/v1/addresses/${address}`);
      setAddresses(addresses.filter((addr) => addr !== address));
      setBalances((prevBalances) => {
        const { [address]: _, ...rest } = prevBalances;
        return rest;
      });
    } catch (error) {
      console.error("Error deleting address:", error);
    }
  };
  return (
    <div className="App">
      <h1>Addresses</h1>

      <input
        type={"text"}
        placeholder={"Add a new address"}
        value={newAddress}
        onChange={(e) => setNewAddress(e.target.value)}
      />

      <button onClick={handleAddAddress}>Add</button>

      <p style={{ color: "red" }}>{errorMsg}</p>
      <p>List of addresses:</p>
      <ul>
        {addresses.map((address, index) => (
          <Address
            address={address}
            balance={balances[address]}
            delete={handleDeleteAddress}
            transactions={handleViewTransactions}
          />
        ))}
      </ul>
    </div>
  );
}

export default App;
