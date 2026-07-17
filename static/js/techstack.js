const techCards = document.querySelectorAll(".techstack-card");

const techObserver = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add("show");

        }

    });

}, {

    threshold: .2

});

techCards.forEach(card => {

    techObserver.observe(card);

});