import {useState} from "react";
import {Link, useNavigate} from "react-router-dom";

const Register = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleRegister = (e) => {
        e.preventDefault();
        console.log('Register');

        // const response = axios.post('http://localhost:8000/api/register', {
        //     name: e.target.name.value,
        //     email: e.target.email.value,
        //     password: e.target.password.value,
        // });
        //
        // console.log(response);

        navigate('/');
    }

    return (
        <div className="flex items-center justify-center mt-44">
            <div className="card bg-gray-100 p-4 rounded-lg shadow-md">
                <h1 className="text-3xl font-bold mb-4">Register</h1>
                <form>
                    <label className="block mb-2">Name:</label>
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        className="w-full px-3 py-2 border rounded"
                    />
                    <label className="block mt-2 mb-2">Email:</label>
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
                        onClick={handleRegister}
                        className="bg-blue-600 text-white px-4 py-2 rounded-full mt-4 hover:bg-blue-500"
                    >
                        Register
                    </button>
                </form>
                <p className="mt-2">
                    Already have an account? <Link to="/login" className="text-blue-600">Login</Link>
                </p>
            </div>
        </div>
    );
}

export default Register;