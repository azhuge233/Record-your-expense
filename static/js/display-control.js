$(window).resize(function() {
    var BigTable = document.getElementById('bigTbl');
    var SmallTable = document.getElementById('smallTbl');
    var DesktopTable = document.getElementById('desktopTbl');
    var MobileTable = document.getElementById('mobileTbl');
    var MoreInfoBtn = document.getElementById('moreBtn');

    if (window.innerWidth < 1424) {
        BigTable.style.display = "none";
        SmallTable.style.display = "";
    } else {
        BigTable.style.display = "";
        SmallTable.style.display = "none";
    }

    if(window.innerWidth < 900) {
        DesktopTable.style.display = "none";
        MobileTable.style.display = MoreInfoBtn.style.display = "";
    } else {
        DesktopTable.style.display = "";
        MobileTable.style.display = MoreInfoBtn.style.display = "none";
    }
   }
);

$(document).ready(function(){
    var BigTable = document.getElementById('bigTbl');
    var SmallTable = document.getElementById('smallTbl');
    var DesktopTable = document.getElementById('desktopTbl');
    var MobileTable = document.getElementById('mobileTbl');
    var MoreInfoBtn = document.getElementById('moreBtn');

    if (window.innerWidth < 1424) {
        BigTable.style.display = "none";
        SmallTable.style.display = "";
    } else {
        BigTable.style.display = "";
        SmallTable.style.display = "none";
    }

    if(window.innerWidth < 900) {
        DesktopTable.style.display = "none";
        MobileTable.style.display = MoreInfoBtn.style.display = "";
    } else {
        DesktopTable.style.display = "";
        MobileTable.style.display = MoreInfoBtn.style.display = "none";
    }
});

function hideinfo() {
    var Button = document.getElementById('moreBtn');
    var table = document.getElementById('mobileTbl');
    var trs = table.rows;

    for(var i = 0; i < trs.length; i++) {
        for(var j = 2; j <= 3; j++ ) {
            trs[i].cells[j].style.display = "none";
        }
    }

    Button.value = "More Info";
    Button.className = "btn is-primary";
    Button.onclick = function() { showinfo(); };
}

function showinfo() {
    var Button = document.getElementById('moreBtn');
    var table = document.getElementById('mobileTbl');
    var trs = table.rows;

    for(var i = 0; i < trs.length; i++) {
        for(var j = 2; j <= 3; j++ ) {
            trs[i].cells[j].style.display = "";
        }
    }

    Button.value = "Hide Info";
    Button.className = "btn is-warning";
    Button.onclick = function() { hideinfo(); };
}
