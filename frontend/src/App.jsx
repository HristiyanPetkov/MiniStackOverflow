import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Navbar from "./components/Navbar";
import HomePage from "./components/HomePage";

const App = () => (
        <Router>
            <Navbar />
            <Routes>
                <Route path='/homePage' element={<HomePage />} />
                <Route path='/' element={<HomePage />} />
            </Routes>
        </Router>
);

export default App;
