import React, { useState } from 'react';

const CompassDashboard = ({ efficiency, wasteVolume }) => {
  // Logic to determine zone
  const isParadox = efficiency > 50 && wasteVolume > 100;

  return (
    <div className="dashboard-card">
      <h2>The Jevons Compass</h2>
      <div className="metrics-container">
        <div className="metric">
          <h3>Efficiency Gain</h3>
          <p>{efficiency}%</p>
        </div>
        <div className="metric">
          <h3>Waste Output</h3>
          <p>{wasteVolume} kg</p>
        </div>
      </div>
      
      <div className={`status-banner ${isParadox ? 'red-zone' : 'green-zone'}`}>
        {isParadox ? (
          <span>⚠ WARNING: JEVONS PARADOX DETECTED. Rebound Effect Active.</span>
        ) : (
          <span>✓ SYSTEM OPTIMIZED. Growth Decoupled from Waste.</span>
        )}
      </div>
      
      {isParadox && (
        <button className="btn-solution">
          Deploy Solution: Project LITHOS
        </button>
      )}
    </div>
  );
};

export default CompassDashboard;
