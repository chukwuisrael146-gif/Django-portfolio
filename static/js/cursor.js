window.addEventListener("DOMContentLoaded", () => {

    const cursor = document.getElementById("cursor");

    if (!cursor) return;

    document.addEventListener("mousemove", (e) => {

        cursor.style.opacity = "1";

        cursor.style.left = `${e.clientX}px`;

        cursor.style.top = `${e.clientY}px`;

    });

    const interactiveElements = document.querySelectorAll(
        "a, button, input, textarea"
    );

    interactiveElements.forEach((element) => {

        element.addEventListener("mouseenter", () => {

            cursor.classList.add(
                "w-12",
                "h-12",
                "bg-orange-500/20"
            );

        });

        element.addEventListener("mouseleave", () => {

            cursor.classList.remove(
                "w-12",
                "h-12",
                "bg-orange-500/20"
            );

        });

    });

});