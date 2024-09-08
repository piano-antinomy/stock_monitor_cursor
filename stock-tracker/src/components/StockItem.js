import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const API_KEY = 'LPLN6G19Z4XBOSZI'; // Replace with your actual API key

function StockItem({ symbol, removeStock, days }) {
  const [prices, setPrices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPrices = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await axios.get(
          `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=${symbol}&apikey=${API_KEY}`
        );
        const timeSeries = response.data['Time Series (Daily)'];
        const priceData = Object.entries(timeSeries)
          .slice(0, days)
          .map(([date, values]) => ({
            date,
            price: parseFloat(values['4. close'])
          }))
          .reverse();
        setPrices(priceData);
      } catch (err) {
        console.error('Error fetching stock data:', err);
        setError('Failed to fetch stock data');
      } finally {
        setLoading(false);
      }
    };

    fetchPrices();
  }, [symbol, days]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="stock-item">
      <h2>{symbol}</h2>
      <button onClick={() => removeStock(symbol)}>Remove</button>
      <ResponsiveContainer width="100%" height={200}>
        <LineChart data={prices}>
          <XAxis dataKey="date" />
          <YAxis domain={['auto', 'auto']} />
          <Tooltip />
          <Line type="monotone" dataKey="price" stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default StockItem;
