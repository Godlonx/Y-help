function copy(name)
{
    var data = document.getElementById(name);
    navigator.clipboard.writeText(data.value);
    copyAnim(name);
}

function copyAnim(name)
{
    var logo = document.getElementById(name+"Logo");
    var valid = document.getElementById(name+"Valid");
    logo.classList.remove("notHide");
    logo.classList.add("hide");
    valid.classList.add("not");
    setTimeout(() => {
        logo.classList.remove("hide");
        logo.classList.add("notHide");
        valid.classList.remove("not");
        console.log("test");
    }, 2000);
}



