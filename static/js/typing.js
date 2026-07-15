window.addEventListener("DOMContentLoaded", () => {

    const text = document.getElementById("typing-text");

    if (!text) return;

    const words = [

        "Full Stack Developer",

        "Backend Engineer",

        "Python Developer",

        "Django Specialist",

        "UI Enthusiast",


    ];

    let wordIndex = 0;
    let charIndex = 0;
    let deleting = false;

    function type(){

        const current = words[wordIndex];

        if(!deleting){

            text.textContent =
                current.substring(0,charIndex++);

            if(charIndex > current.length){

                deleting = true;

                setTimeout(type,1500);

                return;

            }

        }else{

            text.textContent =
                current.substring(0,charIndex--);

            if(charIndex < 0){

                deleting = false;

                wordIndex =
                    (wordIndex+1)%words.length;

            }

        }

        setTimeout(type,deleting?40:80);

    }

    type();

});