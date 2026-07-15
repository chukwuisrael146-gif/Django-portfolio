window.addEventListener("DOMContentLoaded", () => {

    const navbar = document.querySelector("header");

    if (navbar) {

        navbar.animate(

            [
                {
                    opacity: 0,
                    transform: "translateY(-80px)"
                },
                {
                    opacity: 1,
                    transform: "translateY(0)"
                }
            ],

            {
                duration: 900,
                easing: "ease",
                fill: "forwards"
            }

        );

    }

});