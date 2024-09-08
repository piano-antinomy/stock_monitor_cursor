import React from 'react';
import StockItem from './StockItem';

function StockList({ stocks, removeStock, days }) {
  return (
    <div className="stock-list">
      {stocks.map(symbol => (
        <StockItem
          key={symbol}
          symbol={symbol}
          removeStock={removeStock}
          days={days}
        />
      ))}
    </div>
  );
}

export default StockList;
