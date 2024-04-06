import {Link, useNavigate} from "react-router-dom";
import axios from "axios";
import {useState} from "react";

const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = (e) => {
        e.preventDefault();
        console.log('Login');

        // const response = axios.post('http://localhost:8000/api/login', {
        //     email: e.target.email.value,
        //     password: e.target.password.value,
        // });
        //
        // console.log(response);

        navigate('/homePage');
    }

    return (
        <div className="flex items-center justify-center mt-48">
            <div className="card bg-gray-100 p-4 rounded-lg shadow-md">
                <h1 className="text-3xl font-bold mb-4">Login</h1>
                <form>
                    <label className="block mb-2">Email:</label>
                    <input
                        type="text"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="w-full px-3 py-2 border rounded"
                    />
                    <label className="block mt-2 mb-2">Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full px-3 py-2 border rounded"
                    />
                    <button
                        type="button"
                        onClick={handleLogin}
                        className="bg-blue-600 text-white px-4 py-2 rounded-xl mt-4 hover:bg-blue-500"
                    >
                        Login
                    </button>
                </form>
                <p className="mt-2">
                    Don't have an account? <Link to="/register" className="text-blue-600">Register</Link>
                </p>
            </div>
        </div>
    )
}

export default Login;