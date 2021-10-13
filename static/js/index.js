// TODO: falta agreegar funcion de validacion 
const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");

navToggle.addEventListener("click", () => {
  navMenu.classList.toggle("nav-menu_visible");

  if (navMenu.classList.contains("nav-menu_visible")) {
    navToggle.classList.setAttribute("aria-label", "Cerrar menú");
  } else {
    navToggle.classList.setAttribute("aria-label", "Abrir menú");
  }
});
