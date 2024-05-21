import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Navbar from "./components/Navbar";
import HomePage from "./components/HomePage";
import QuestionPage from "./components/QuestionPage";
import Login from "./components/Login";
import Register from "./components/Register";
import AskQuestion from "./components/AskQuestion";
import ProfilePage from "./components/ProfilePage";

const App = () => (
        <Router>
            <Navbar />
            <div className="mt-20">
                <Routes>
                    <Route path='/' element={<HomePage />} />
                    <Route path='/login' element={<Login />} />
                    <Route path='/register' element={<Register />} />
                    <Route path='/homePage' element={<HomePage />} />
                    <Route path='/askQuestion' element={<AskQuestion />} />
                    <Route path='/users/:userId' element={<ProfilePage />} />
                    <Route path='/questions/:questionId' element={<QuestionPage />} />

                    <Route path='*' element={<h1>Not Found</h1>} />
                </Routes>
            </div>
        </Router>
);

export default App;
