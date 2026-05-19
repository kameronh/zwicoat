import React from 'react';

const FCOI = () => {
  return (
    <div style={{ height: 'calc(100vh - 70px)', display: 'flex', flexDirection: 'column' }}>
      <iframe
        src="/ZCMI_FCOI_Policy.pdf"
        title="ZCMI Financial Conflict of Interest Policy"
        style={{ flex: 1, width: '100%', border: 'none' }}
      />
    </div>
  );
};

export default FCOI;
