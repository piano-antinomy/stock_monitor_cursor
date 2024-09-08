import React, { useState } from 'react';

function AddStockForm({ addStock }) {
  const [symbol, setSymbol] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (symbol.trim()) {
      addStock(symbol.trim().toUpperCase());
      setSymbol('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        placeholder="Enter stock symbol"
      />
      <button type="submit">Add Stock</button>
    </form>
  );
}

export default AddStockForm;
