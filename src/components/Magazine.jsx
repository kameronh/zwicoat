import React, { useRef } from 'react';
import HTMLFlipBook from 'react-pageflip';
import { NavLink } from 'react-router-dom';
import { BsArrowRight, BsArrowLeft } from 'react-icons/bs';


const Magazine = ({
  id,
  title,
  img,
  coverImg,
  authors,
  journal,
  summary,
  link,
}) => {
  const bookRef = useRef();

  const handleClose = () => {
    bookRef.current.pageFlip().flipPrev();
  };

  return (
    <div className="magazine-center">
      <HTMLFlipBook
        ref={bookRef}
        className="appear-up"
        showCover={true}
        width={350}
        height={500}
      >
        <div className="inside-cover-page">
          <BsArrowRight style={{ alignSelf: 'end', margin: '5px 5px 0 0', fontSize: '25px'}} />
          <h2 className="magazine-inside-title">{title}</h2>
          <p className="magazine-authors">Authors: {authors}</p>
          <p className="magazine-journal">Journal: {journal}</p>
          <img src={img} alt={'Inside cover image taken from ' + journal} className="magazine-inside-img" />
        </div>
        <div className="content-page">
          <button
            onClick={handleClose}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '4px',
              background: 'none',
              border: 'none',
              cursor: 'pointer',
              color: 'var(--primary-1)',
              fontSize: '14px',
              padding: '4px 0',
              alignSelf: 'flex-start',
            }}
          >
            <BsArrowLeft style={{ fontSize: '18px' }} />
            Close
          </button>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 48 48"
            width="48px"
            height="48px"
          >
            <path d="M 16.482422 8.9921875 A 1.50015 1.50015 0 0 0 15.943359 9.1074219 C 15.943359 9.1074219 13.068414 10.279429 10.357422 13.464844 C 7.6464301 16.650259 5 21.927419 5 30 A 1.50015 1.50015 0 0 0 5.015625 30.21875 A 8.5 8.5 0 0 0 13.5 39 A 8.5 8.5 0 0 0 13.5 22 A 8.5 8.5 0 0 0 8.7089844 23.480469 C 9.5777265 19.777157 11.122152 17.196657 12.642578 15.410156 C 14.931586 12.720571 17.056641 11.892578 17.056641 11.892578 A 1.50015 1.50015 0 0 0 16.482422 8.9921875 z M 37.482422 8.9921875 A 1.50015 1.50015 0 0 0 36.943359 9.1074219 C 36.943359 9.1074219 34.068414 10.279429 31.357422 13.464844 C 28.64643 16.650259 26 21.927419 26 30 A 1.50015 1.50015 0 0 0 26.015625 30.21875 A 8.5 8.5 0 0 0 34.5 39 A 8.5 8.5 0 0 0 34.5 22 A 8.5 8.5 0 0 0 29.708984 23.480469 C 30.577727 19.777157 32.122152 17.196657 33.642578 15.410156 C 35.931586 12.720571 38.056641 11.892578 38.056641 11.892578 A 1.50015 1.50015 0 0 0 37.482422 8.9921875 z" />
          </svg>
          <p className="content-body">{summary}</p>
          <NavLink to={link} className="magazine-link btn">
            Read
          </NavLink>
        </div>
      </HTMLFlipBook>
    </div>
  );
};

export default Magazine;
