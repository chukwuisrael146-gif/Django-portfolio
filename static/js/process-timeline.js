document.addEventListener("DOMContentLoaded", () => {

    const stages = document.querySelectorAll(".timeline-stage");

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("active");

            }

        });

    }, {

        threshold: 0.2

    });

    stages.forEach(stage => observer.observe(stage));

});