window.addEventListener("DOMContentLoaded", () => {

    /* ==========================================
       ACTIVE NAVIGATION LINKS
    ========================================== */

    const sections = document.querySelectorAll("section[id]");
    const navLinks = document.querySelectorAll("nav a[href^='#']");

    function activateNavLink() {

        const scrollPosition = window.scrollY + 150;

        sections.forEach(section => {

            const top = section.offsetTop;
            const height = section.offsetHeight;
            const id = section.getAttribute("id");

            if (
                scrollPosition >= top &&
                scrollPosition < top + height
            ) {

                navLinks.forEach(link => {

                    link.classList.remove(
                        "text-orange-500",
                        "font-semibold"
                    );

                    if (link.getAttribute("href") === `#${id}`) {

                        link.classList.add(
                            "text-orange-500",
                            "font-semibold"
                        );

                    }

                });

            }

        });

    }

    window.addEventListener("scroll", activateNavLink);

    activateNavLink();



    /* ==========================================
       SCROLL PROGRESS BAR
    ========================================== */

    const progressBar = document.getElementById("scroll-progress");

    function updateProgressBar() {

        if (!progressBar) return;

        const scrollTop = window.scrollY;

        const height =
            document.documentElement.scrollHeight -
            window.innerHeight;

        const progress = (scrollTop / height) * 100;

        progressBar.style.width = `${progress}%`;

    }

    window.addEventListener("scroll", updateProgressBar);

    updateProgressBar();



    /* ==========================================
       BACK TO TOP BUTTON
    ========================================== */

    const backToTop = document.getElementById("back-to-top");

    function toggleBackToTop() {

        if (!backToTop) return;

        if (window.scrollY > 500) {

            backToTop.classList.remove(
                "opacity-0",
                "pointer-events-none",
                "translate-y-5"
            );

            backToTop.classList.add(
                "opacity-100",
                "translate-y-0"
            );

        } else {

            backToTop.classList.add(
                "opacity-0",
                "pointer-events-none",
                "translate-y-5"
            );

            backToTop.classList.remove(
                "opacity-100",
                "translate-y-0"
            );

        }

    }

    window.addEventListener("scroll", toggleBackToTop);

    toggleBackToTop();

    if (backToTop) {

        backToTop.addEventListener("click", () => {

            window.scrollTo({

                top: 0,

                behavior: "smooth"

            });

        });

    }



    /* ==========================================
       SECTION REVEAL
    ========================================== */

    const revealElements = document.querySelectorAll(".reveal");

    const observer = new IntersectionObserver(

        (entries) => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    entry.target.classList.add(
                        "opacity-100",
                        "translate-y-0"
                    );

                    entry.target.classList.remove(
                        "opacity-0",
                        "translate-y-8"
                    );

                    observer.unobserve(entry.target);

                }

            });

        },

        {
            threshold: 0.15
        }

    );

    revealElements.forEach(el => observer.observe(el));

});