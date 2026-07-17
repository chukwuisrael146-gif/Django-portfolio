document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".experience-card");
    const dots = document.querySelectorAll(".progress-dot");

    if (!cards.length) return;

    const cardsArray = [...cards];

    // Tailwind `top-32` = 8rem = 128px. Cards are sticky there, so the
    // card whose top has reached this offset is the one currently on top.
    const STICKY_OFFSET = 128;

    const setActive = (index) => {

        cardsArray.forEach((card, i) =>
            card.classList.toggle("is-active", i === index)
        );

        dots.forEach((dot, i) =>
            dot.classList.toggle("active", i === index)
        );

    };

    let ticking = false;

    const update = () => {

        ticking = false;

        // The active card is the last one that has stuck at the top.
        // Every earlier card is also stuck (behind it), so the highest
        // index whose top has reached the offset is the visible one.
        let active = 0;

        cardsArray.forEach((card, i) => {

            if (card.getBoundingClientRect().top <= STICKY_OFFSET + 1) {
                active = i;
            }

        });

        setActive(active);

    };

    const onScroll = () => {

        if (!ticking) {
            ticking = true;
            requestAnimationFrame(update);
        }

    };

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });

    // Highlight the first card before any scrolling happens.
    setActive(0);
    update();

});
