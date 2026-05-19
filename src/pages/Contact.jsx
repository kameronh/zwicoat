import React from 'react';
import Wrapper from '../assets/wrappers/ContactPageWrapper';

const Contact = () => {
  return (
    <Wrapper>
      <div className="contact">
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          gap: '2rem',
          fontFamily: 'SUSE, sans-serif',
        }}>
          <h2 style={{ fontSize: '2rem', fontWeight: '700', color: 'var(--grey-darkest)' }}>
            Get in Touch
          </h2>
          <div>
            <p style={{ fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: 'var(--grey-darker)', marginBottom: '0.4rem' }}>
              Email
            </p>
            <a
              href="mailto:info@zwicoat.com"
              style={{ color: 'var(--primary-1)', fontSize: '1.1rem', textDecoration: 'none' }}
            >
              info@zwicoat.com
            </a>
          </div>
          <div>
            <p style={{ fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: 'var(--grey-darker)', marginBottom: '0.4rem' }}>
              Phone
            </p>
            <a
              href="tel:+19176094598"
              style={{ color: 'var(--primary-1)', fontSize: '1.1rem', textDecoration: 'none' }}
            >
              (917) 609-4598
            </a>
          </div>
        </div>
      </div>
    </Wrapper>
  );
};

export default Contact;
