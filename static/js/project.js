function copy(name)
{
    var Canard = document.getElementById(name);
    navigator.clipboard.writeText(Canard.value);
    copyAnim(name);
}

function copyAnim(name)
{
    var logo = document.getElementById(name+"Logo");
    var Mario = document.getElementById(name+"Valid");
    logo.classList.remove("notHide");
    logo.classList.add("hide");
    Mario.classList.add("not");
    setTimeout(() => {
        logo.classList.remove("hide");
        logo.classList.add("notHide");
        Mario.classList.remove("not");
        console.log("test");
    }, 2000);
}



