document.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem('theme');
  const isDark = savedTheme === 'dark';
  document.body.classList.toggle('dark', isDark);
  setThemeButton(isDark);

  const btn = document.querySelector('.theme-toggle-li');
  if (btn) btn.addEventListener('click', toggleTheme);
});

function toggleTheme() {
  const isDark = document.body.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
  setThemeButton(isDark, true);
}

function setThemeButton(isDark, animate = false) {
  const icon = document.querySelector('.theme-toggle-li i');
  const label = document.querySelector('.theme-toggle-li span');
  if (!icon || !label) return;

  if (animate) {
    icon.style.transition = 'transform 0.4s ease, opacity 0.3s ease';
    icon.style.transform = 'rotate(180deg)';
    icon.style.opacity = '0';
    label.style.opacity = '0';

    setTimeout(() => {
      icon.className = `fa-solid ${isDark ? 'fa-sun' : 'fa-moon'}`;
      label.textContent = isDark ? 'Modo Claro' : 'Modo Oscuro';
      icon.style.transform = 'rotate(0deg)';
      icon.style.opacity = '1';
      label.style.opacity = '1';
    }, 200);
  } else {
    icon.className = `fa-solid ${isDark ? 'fa-sun' : 'fa-moon'}`;
    label.textContent = isDark ? 'Modo Claro' : 'Modo Oscuro';
  }
}

window.toggleTheme = toggleTheme;
