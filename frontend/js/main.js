// Global Helper Functions
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `fixed bottom-4 right-4 text-white px-6 py-3 rounded-lg shadow-lg z-50 transform transition-all duration-300 translate-y-10 opacity-0 ${type === 'success' ? 'bg-green-500' : 'bg-red-500'}`;
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.remove('translate-y-10', 'opacity-0');
    }, 10);

    setTimeout(() => {
        toast.classList.add('translate-y-10', 'opacity-0');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function addToCart(product) {
    let cart = JSON.parse(localStorage.getItem('cart') || '[]');
    const existingIndex = cart.findIndex(item => item.id === product.id);
    
    if (existingIndex > -1) {
        cart[existingIndex].quantity += 1;
    } else {
        cart.push({...product, quantity: 1});
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    
    if (typeof updateCartCount === 'function') {
        updateCartCount();
    }
    showToast('Added to cart!');
}

function getCartTotal() {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    return cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
}

// Ensure products get random default image if none provided
function getProductImage(url, id) {
    if (url) return url;
    return `https://picsum.photos/seed/${id}/400/300`;
}
