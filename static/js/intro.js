window.addEventListener("load", () => {

    const intro = document.getElementById("intro-screen");

    const video = document.getElementById("hero-video");

    video.classList.remove("opacity-0");

    setTimeout(() => {

        intro.classList.add(
            "opacity-0",
            "transition-opacity",
            "duration-1000"
        );

    }, 800);

    setTimeout(() => {

        intro.remove();

    }, 2000);

});