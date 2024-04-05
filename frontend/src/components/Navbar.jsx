import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';

const Navbar = () => {
    return (
        <nav className="fixed top-0 left-0 w-full bg-gray-700 p-4 z-10 flex justify-between items-center">
            <Link to="/homePage" className="text-white font-semibold">Home</Link>
            <div className="flex items-center">
                <Link to="/profile" className="text-white font-semibold mr-4">Profile</Link>
                <div className="w-8 h-8 flex justify-center items-center bg-gray-300 rounded-full">
                    <FontAwesomeIcon icon={faUser} className="text-gray-600" />
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
