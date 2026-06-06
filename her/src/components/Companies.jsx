import React from 'react';

//receiving props, where result comes from flask, query comes from user and function to go back
const Companies = ({ results, query, onBack }) => {
  return (
    <div className="page-container">
      <h1 className="brand-title">Her-Search Makeup</h1>
      
      {/*ternery oerator, if condition is True then show thing 1 or else thing 2 */}
      {results.length > 0 ? (
        <div className="results-list">
          {results.map((company, index) => (
            <div key={index} className="result-item">
              {company}
            </div>
          ))}
        </div>
      ) : (
        <div className="info-text">
          <p>No companies found for "{query}".</p>
          <p style={{ marginTop: '0.5rem', fontSize: '0.9rem', opacity: 0.7 }}>
            Try searching for "makeup", "lipstick", "shades", "foundation", or leave it blank to see all!
          </p>
        </div>
      )}
      
      <button onClick={onBack} className="back-button">
        &larr; Search Again
      </button>
    </div>
  );
};

export default Companies;
