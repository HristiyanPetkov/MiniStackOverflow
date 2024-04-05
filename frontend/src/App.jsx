import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Navbar from "./components/Navbar";
import HomePage from "./components/HomePage";
import QuestionPage from "./components/QuestionPage";

const App = () => (
        <Router>
            <Navbar />
            <Routes>
                <Route path='/homePage' element={<HomePage />} />
                <Route path='/' element={<HomePage />} />
                <Route path='/questions/:questionId' element={<QuestionPage />} />
            </Routes>
        </Router>
);

export default App;
