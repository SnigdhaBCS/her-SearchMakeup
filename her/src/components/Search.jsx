import React from 'react';

const Search = ({ query, setQuery, onSearch }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch();
  };

  return (
    <div className="page-container">
      <h1 className="brand-title">Her-Search Makeup</h1>
      
      <form onSubmit={handleSubmit} className="search-card">
        <div className="search-input-wrapper">
          <svg
            className="search-icon"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            strokeWidth="2"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
          <input
            type="text"
            className="search-input"
            placeholder="Search shades, brands..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </div>
        
        <button type="submit" className="go-button">
          Go &rarr;
        </button>
      </form>
    </div>
  );
};

export default Search;
