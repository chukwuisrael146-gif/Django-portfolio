const mainImage = document.getElementById("gallery-main");

const thumbs = document.querySelectorAll(".gallery-thumb");

thumbs.forEach(button => {

    button.addEventListener("click", () => {

        mainImage.style.opacity = 0;

        setTimeout(() => {

            mainImage.src = button.dataset.image;

            mainImage.style.opacity = 1;

        }, 200);

        thumbs.forEach(t => t.classList.remove("active"));

        button.classList.add("active");

    });

});