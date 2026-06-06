import React, { useState } from 'react';
import Search from './Search';
import Companies from './Companies';

const Makeup = () => {
  // Navigation state: 'search' or 'results'
  const [currentPage, setCurrentPage] = useState('search');
  
  // Search query state
  const [query, setQuery] = useState('');
  
  // Search results state---multiple results will be there so result state is is array
  const [results, setResults] = useState([]);
  
  // Loading and error states
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Function to handle search logic by querying Flask API
  const handleSearch = async () => {
    setLoading(true);
    setError(null);
    
    try {
      // Fetch matching companies from the backend Flask server
      const response = await fetch(`http://127.0.0.1:5000/api/search?q=${encodeURIComponent(query)}`);
      
      if (!response.ok) {   //checks if flask reponses in 200 or 404/500 etc.
        throw new Error('Failed to fetch data from the server');
      }
      
      const data = await response.json();
      setResults(data);
      setCurrentPage('results');
    } catch (err) {
      console.error(err);
      setError('Could not connect to the backend server. Please make sure the Flask app is running.');
      setCurrentPage('results'); // Show results screen so the error displays
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  // Function to go back to search page
  const handleBack = () => {
    setCurrentPage('search');
    setError(null);
  };

  return (
    <div style={{ width: '100%' }}>
      {currentPage === 'search' ? (
        <Search 
          query={query} 
          setQuery={setQuery} 
          onSearch={handleSearch} 
        />
      ) : (
        <div style={{ width: '100%', position: 'relative' }}>
          {loading && (
            <div className="info-text" style={{ padding: '2rem' }}>
              Loading results...
            </div>
          )}
          
          {!loading && error && (
            <div className="info-text" style={{ padding: '2rem', color: '#ffb7b2' }}>
              <p>{error}</p>
              <button onClick={handleBack} className="back-button">
                &larr; Go Back
              </button>
            </div>
          )}
          
          {!loading && !error && (
            <Companies 
              results={results} 
              query={query} 
              onBack={handleBack} 
            />
          )}
        </div>
      )}
    </div>
  );
};

export default Makeup;