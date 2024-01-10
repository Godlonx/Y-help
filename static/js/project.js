function copy(name)
{
    var data = document.getElementById(name);
    navigator.clipboard.writeText(data.value);
}