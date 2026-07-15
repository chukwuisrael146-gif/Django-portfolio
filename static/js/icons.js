import { createIcons, Code2, Zap, Lightbulb } from "lucide";

createIcons({
    icons: {
        Code2,
        Zap,
        Lightbulb
    }
});

gsap.from(".feature-icon", {

    scale: 0,

    rotate: -180,

    opacity: 0,

    duration: 0.8,

    stagger: 0.2,

    ease: "back.out(1.7)",

    scrollTrigger: {
        trigger: ".feature-card",
        start: "top 80%"
    }

});