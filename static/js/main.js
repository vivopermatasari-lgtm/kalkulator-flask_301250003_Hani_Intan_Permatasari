// =====================
// DARK MODE TOGGLE
// =====================
const toggleBtn = document.getElementById('toggleMode');
const html = document.documentElement;

// Load tema tersimpan
const savedTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-bs-theme', savedTheme);
updateToggleBtn(savedTheme);

toggleBtn.addEventListener('click', () => {
    const current = html.getAttribute('data-bs-theme');
    const newTheme = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-bs-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateToggleBtn(newTheme);
});

function updateToggleBtn(theme) {
    if (theme === 'dark') {
        toggleBtn.textContent = '☀️ Light Mode';
        toggleBtn.classList.remove('btn-outline-light');
        toggleBtn.classList.add('btn-warning');
    } else {
        toggleBtn.textContent = '🌙 Dark Mode';
        toggleBtn.classList.remove('btn-warning');
        toggleBtn.classList.add('btn-outline-light');
    }
}

// =====================
// ACTIVE NAVBAR
// =====================
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
        link.style.fontWeight = 'bold';
    }
});