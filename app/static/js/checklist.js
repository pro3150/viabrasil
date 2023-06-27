const change = (event) => {
    const image = event.target
    if (image.className == "check_item checklist-true") {
        image.className = "check_item checklist-false"
        image.src = "/static/img/checklist-not-ok.png";
    } else {
        image.className = "check_item checklist-true"
        image.src = "/static/img/checklist.png";
    }
}

checklists = document.querySelectorAll(".check_item")

console.log(checklists)

checklists.forEach(element => {
    element.addEventListener("click", change)
});

// checklists.addEventListener("change", change)
