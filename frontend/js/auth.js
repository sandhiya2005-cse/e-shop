// Auth logic
document.addEventListener('DOMContentLoaded', () => {
    updateNavAuth();
});

function updateNavAuth() {
    const token = localStorage.getItem('token');
    const authLinks = document.getElementById('auth-links');
    if (!authLinks) return;

    if (token) {
        authLinks.innerHTML = `
            <a href="chatbot.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 font-medium flex items-center gap-1">Chatbot</a>
            <a href="admin.html" class="text-blue-600 hover:text-blue-800 px-3 py-2 font-bold flex items-center gap-1">Admin Panel</a>
            <a href="cart.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 font-medium flex items-center gap-1"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg> Cart (<span id="cart-count">0</span>)</a>
            <button onclick="logout()" class="ml-4 bg-gray-200 text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-300 transition font-medium">Logout</button>
        `;
        updateCartCount();
    } else {
        authLinks.innerHTML = `
            <a href="chatbot.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 font-medium flex items-center gap-1">Chatbot</a>
            <a href="auth.html" class="text-gray-600 hover:text-blue-600 px-3 py-2 font-medium">Login</a>
            <a href="auth.html" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition shadow-lg shadow-blue-500/30 font-medium">Sign Up</a>
        `;
    }
}

function logout() {
    localStorage.removeItem('token');
    window.location.href = 'index.html';
}

function updateCartCount() {
    const cartCountEl = document.getElementById('cart-count');
    if (cartCountEl) {
        const cart = JSON.parse(localStorage.getItem('cart') || '[]');
        const count = cart.reduce((sum, item) => sum + item.quantity, 0);
        cartCountEl.textContent = count;
    }
}
