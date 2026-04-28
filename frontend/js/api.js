const API_BASE_URL = 'http://localhost:8000/api';

class API {
    static getHeaders(auth = false) {
        const headers = { 'Content-Type': 'application/json' };
        if (auth) {
            const token = localStorage.getItem('token');
            if (token) headers['Authorization'] = `Bearer ${token}`;
        }
        return headers;
    }

    static async get(endpoint, auth = false) {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            headers: API.getHeaders(auth)
        });
        if (!response.ok) throw await response.json();
        return response.json();
    }

    static async post(endpoint, data, auth = false) {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: 'POST',
            headers: API.getHeaders(auth),
            body: JSON.stringify(data)
        });
        if (!response.ok) throw await response.json();
        return response.json();
    }

     static async put(endpoint, data, auth = true) {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: 'PUT',
            headers: API.getHeaders(auth),
            body: JSON.stringify(data)
        });
        if (!response.ok) throw await response.json();
        return response.json();
    }

    static async delete(endpoint, auth = true) {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: 'DELETE',
            headers: API.getHeaders(auth)
        });
        if (response.status === 204) return true;
        if (!response.ok) throw await response.json();
        return response.json();
    }
}
