const cta = document.querySelector("#about-cta");

const ctaObserver = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            cta.classList.add("in-view");

        }

    });

}, {

    threshold: .35

});

ctaObserver.observe(cta);