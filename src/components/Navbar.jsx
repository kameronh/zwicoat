import React from 'react';
import { NavLink } from 'react-router-dom';
import Wrapper from '../assets/wrappers/NavbarWrapper';

const Navbar = () => {
  return (
    <Wrapper>
      <nav className="navbar nav-fade">
        <div className="nav-center">
          <span className="logo">ZCMI</span>
          <div className="nav-links">
            <NavLink to="/" className="nav-link">
              Home
            </NavLink>
            <NavLink to="/technology" className="nav-link">
              Technology
            </NavLink>
            <NavLink to="/about" className="nav-link">
              About
            </NavLink>
            <NavLink to="/contact" className="nav-link">
              Contact
            </NavLink>
            <NavLink to="/fcoi" className="nav-link">
              FCOI Policy
            </NavLink>
          </div>
        </div>
      </nav>
    </Wrapper>
  );
};

export default Navbar;
