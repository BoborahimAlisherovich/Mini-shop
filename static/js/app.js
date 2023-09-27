let elBurger = document.querySelector(".burger");
let elSidebar = document.querySelector(".sidebar");
let elCrossBtn = document.querySelector(".sidebar__cross-btn");
let elContainer = document.querySelectorAll(".container")

elBurger.addEventListener("click", ()=>{
    elSidebar.classList.toggle("sidebar_active");
    elContainer.forEach(element => {
        element.classList.toggle("container_active")
    });
})
elCrossBtn.addEventListener("click", ()=>{
    elSidebar.classList.toggle("sidebar_active");
    elContainer.forEach(element => {
        element.classList.toggle("container_active")
    });
});