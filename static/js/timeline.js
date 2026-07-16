const items = document.querySelectorAll(".timeline-item");

const observer = new IntersectionObserver(

(entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.classList.add("active");

}

});

},

{

threshold:.35

}

);

items.forEach(item=>observer.observe(item));

const progress=document.getElementById("timeline-progress");

const container=document.getElementById("timeline-container");

window.addEventListener("scroll",()=>{

if(!progress||!container) return;

const rect=container.getBoundingClientRect();

const total=document.body.offsetHeight > container.offsetHeight ? container.offsetHeight : container.scrollHeight;

const visible=Math.min(Math.max(window.innerHeight-rect.top,0),total);

progress.style.height=visible+"px";

});