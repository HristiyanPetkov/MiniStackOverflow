import React, {useState} from 'react';

const user = {
    name: 'John Doe',
    email: 'john.doe@example.com',
}

const ProfilePage = () => {
    const [name, setName] = useState(user.name);
    const [email, setEmail] = useState(user.email);
    const [password, setPassword] = useState('');

    const updateProfile = () => {
        console.log('Update profile');

        // const response = axios.put('http://localhost:8000/api/profile', {
        //     name: name,
        //     email: email,
        //     password: password,
        // });
        //
        // console.log(response);

        console.log('Name:', name);
        console.log('Email:', email);
        console.log('Password:', password)
    }

    return (
        <div className="flex items-center justify-center mt-44">
            <div className="bg-white p-8 rounded-lg shadow-lg">
                <div className="text-center">
                    <h1 className="text-2xl font-bold mb-4">Edit Profile</h1>
                </div>
                <div>
                    <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                        Name
                    </label>
                    <input
                        type="text"
                        id="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        className="mt-1 p-2 block w-full border-gray-300 rounded-md"
                    />
                </div>
                <div className="mt-4">
                    <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                        Email
                    </label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="mt-1 p-2 block w-full border-gray-300 rounded-md"
                    />
                </div>
                <div className="mt-4">
                    <label htmlFor="password" className="block text-sm font-medium text-gray-700">
                        Password
                    </label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="mt-1 p-2 block w-full border-gray-300 rounded-md"
                    />
                </div>
                <div className="mt-6">
                    <button className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600" onClick={updateProfile}>
                        Save Changes
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ProfilePage;
