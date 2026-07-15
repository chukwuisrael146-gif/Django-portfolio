window.addEventListener("DOMContentLoaded", () => {
    const navbar = document.getElementById("navbar");

    if (!navbar) return;

    const updateNavbar = () => {
        if (window.scrollY > 60) {
            navbar.classList.add(
                "bg-[#17181c]/80",
                "backdrop-blur-2xl",
                "shadow-2xl",
                "shadow-black/40"
            );

            navbar.classList.remove("bg-white/5");
        } else {
            navbar.classList.remove(
                "bg-[#17181c]/80",
                "backdrop-blur-2xl",
                "shadow-2xl",
                "shadow-black/40"
            );

            navbar.classList.add("bg-white/5");
        }
    };

    updateNavbar();

    window.addEventListener("scroll", updateNavbar);
});