$(window).resize(function() {
    var BigTable = document.getElementById('bigTbl');
    var SmallTable = document.getElementById('smallTbl');

    if (window.innerWidth < 1424) {
        BigTable.style.display = "none";
        SmallTable.style.display = "";
    } else {
        BigTable.style.display = "";
        SmallTable.style.display = "none";
    }
});