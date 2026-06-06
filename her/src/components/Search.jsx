import React from 'react';

//search is recieving 3 things from its parent Makeup----query,setQuery and handleSearch
//this is props destructuring
const Search = ({ query, setQuery, onSearch }) => {
  //e is Event Object
  const handleSubmit = (e) => {  
  // When the user submits the form, 
  // React automatically creates an object containing information about that event.
    e.preventDefault();
    onSearch();
  };
//SVG----Scalable Vector Graphic
//every keystrock updates state

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
            placeholder="Search..."
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
