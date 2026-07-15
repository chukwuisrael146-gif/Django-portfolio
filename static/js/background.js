window.addEventListener("DOMContentLoaded", () => {

    const blobs = document.querySelectorAll(".blob");

    if (!blobs.length) return;

    document.addEventListener("mousemove", (e) => {

        const x =
            (e.clientX / window.innerWidth - 0.5) * 50;

        const y =
            (e.clientY / window.innerHeight - 0.5) * 50;

        blobs.forEach((blob, index) => {

            const strength = (index + 1) * 0.35;

            blob.style.transform =
                `translate(${x * strength}px, ${y * strength}px)`;

        });

    });

});