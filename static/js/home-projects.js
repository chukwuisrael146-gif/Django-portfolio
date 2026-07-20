document.addEventListener("DOMContentLoaded", () => {

    const previewCard = document.getElementById("project-preview-card");

    if (!previewCard) return;

    const image = document.getElementById("preview-image");
    const title = document.getElementById("preview-title");
    const description = document.getElementById("preview-description");
    const category = document.getElementById("preview-category");
    const link = document.getElementById("preview-link");

    const items = document.querySelectorAll(".project-item");

    function changeProject(item) {

        items.forEach(card => card.classList.remove("active"));

        item.classList.add("active");

        previewCard.classList.add("preview-changing");

        setTimeout(() => {

            image.src = item.dataset.image;

            title.textContent = item.dataset.title;

            description.textContent = item.dataset.description;

            category.textContent = item.dataset.category;

            link.href = item.dataset.url;

            previewCard.classList.remove("preview-changing");

        }, 250);

    }

    items.forEach(item => {

        item.addEventListener("mouseenter", () => {

            changeProject(item);

        });

    });

});

const card = document.getElementById("project-preview-card");

if (card) {

    card.addEventListener("mousemove", (e) => {

        const rect = card.getBoundingClientRect();

        const x = e.clientX - rect.left;

        const y = e.clientY - rect.top;

        const rotateY = ((x / rect.width) - .5) * 10;

        const rotateX = ((y / rect.height) - .5) * -10;

        card.style.transform = `
perspective(1400px)
rotateX(${rotateX}deg)
rotateY(${rotateY}deg)
translateY(-8px)
`;

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = `
perspective(1400px)
rotateX(0deg)
rotateY(0deg)
translateY(0px)
`;

    });

}