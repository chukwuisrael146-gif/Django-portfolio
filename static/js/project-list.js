const cta = document.querySelector(".project-cta");
const spotlight = document.getElementById("cta-spotlight");

if (cta) {

    cta.addEventListener("mousemove", (e) => {

        const rect = cta.getBoundingClientRect();

        spotlight.style.left = (e.clientX - rect.left) + "px";

        spotlight.style.top = (e.clientY - rect.top) + "px";

        spotlight.style.opacity = 1;

    });

    cta.addEventListener("mouseleave", () => {

        spotlight.style.opacity = 0;

    });

}

document.querySelectorAll(".magnetic").forEach(button => {

    button.addEventListener("mousemove", (e) => {

        const rect = button.getBoundingClientRect();

        const x = e.clientX - rect.left - rect.width / 2;

        const y = e.clientY - rect.top - rect.height / 2;

        button.style.transform = `translate(${x * .15}px,${y * .15}px)`;

    });

    button.addEventListener("mouseleave", () => {

        button.style.transform = "translate(0,0)";

    });

});

const card = document.querySelector(".project-cta");

if (card) {

    card.addEventListener("mousemove", (e) => {

        const rect = card.getBoundingClientRect();

        const x = e.clientX - rect.left;

        const y = e.clientY - rect.top;

        const rotateY = ((x / rect.width) - .5) * 8;

        const rotateX = ((y / rect.height) - .5) * -8;

        card.style.transform =

            `perspective(1400px)
rotateX(${rotateX}deg)
rotateY(${rotateY}deg)`;

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform =

            `perspective(1400px)
rotateX(0deg)
rotateY(0deg)`;

    });

}