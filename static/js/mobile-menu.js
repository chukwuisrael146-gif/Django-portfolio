window.addEventListener("DOMContentLoaded", () => {

    const mobileMenu = document.getElementById("mobile-menu");
    const openMenu = document.getElementById("open-menu");
    const closeMenu = document.getElementById("close-menu");

    if (!mobileMenu || !openMenu || !closeMenu) return;

    function openMobileMenu() {
        mobileMenu.classList.remove("hidden");
        document.body.style.overflow = "hidden";
    }

    function closeMobileMenu() {
        mobileMenu.classList.add("hidden");
        document.body.style.overflow = "";
    }

    openMenu.addEventListener("click", openMobileMenu);

    closeMenu.addEventListener("click", closeMobileMenu);

    mobileMenu.addEventListener("click", (e) => {
        if (e.target === mobileMenu) {
            closeMobileMenu();
        }
    });

    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
            closeMobileMenu();
        }
    });

});