const funCards = document.querySelectorAll(".fun-card");

const funObserver = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show");

        }

    });

},{

    threshold:.2

});

funCards.forEach((card,index)=>{

    card.style.transitionDelay = `${index*120}ms`;

    funObserver.observe(card);

});