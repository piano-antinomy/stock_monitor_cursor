import React, { useState } from 'react';
import StockList from './components/StockList';
import AddStockForm from './components/AddStockForm';
import './App.css';

function App() {
  const [stocks, setStocks] = useState(['AAPL', 'GOOGL', 'MSFT']);
  const [days, setDays] = useState(30);

  const addStock = (symbol) => {
    if (!stocks.includes(symbol)) {
      setStocks([...stocks, symbol]);
    }
  };

  const removeStock = (symbol) => {
    setStocks(stocks.filter(stock => stock !== symbol));
  };

  return (
    <div className="App">
      <h1>Stock Tracker</h1>
      <AddStockForm addStock={addStock} />
      <div>
        <label>
          Days to show:
          <input
            type="number"
            min="1"
            max="365"
            value={days}
            onChange={(e) => setDays(parseInt(e.target.value))}
          />
        </label>
      </div>
      {StockList && <StockList stocks={stocks} removeStock={removeStock} days={days} />}
    </div>
  );
}

export default App;
