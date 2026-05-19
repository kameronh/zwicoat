import React from 'react';
import { NavLink } from 'react-router-dom';
import Wrapper from '../assets/wrappers/FooterWrapper';

const Footer = () => {
  return (
    <Wrapper>
      <footer>
        <div className="footer-center">
          <div className="footer-logo">
            <h1 className="footer-header">ZCMI</h1>
          </div>
          <div className="footer-links">
            <NavLink to="/technology" className="footer-link">
              Technology
            </NavLink>
            <NavLink to="/about" className="footer-link">
              About
            </NavLink>
          </div>
          <div className="footer-info">
          </div>
        </div>
      </footer>
    </Wrapper>
  );
};

export default Footer;
