var var1;

function loader_func() {
    var1 = setTimeout(showPage, 1);
}

function showPage() {
    document.getElementById("loader").style.display = "none";
    document.getElementById("main-content").style.display = "block";
}

