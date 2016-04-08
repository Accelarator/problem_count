$(document).ready(function(){
    $("#title").mouseover(function(){
        $("#title").css("color", "white");
    });
    $("#title").mouseout(function(){
        $("#title").css("color","rgb(119,119,119)");
    });
    $("#title").click(function(){
        location.reload();
    });
    setInterval(function() {
        var times = new Date();
        var yy = times.getFullYear();
        var mm = times.getMonth()+1;
        var dd = times.getDate();
        var h = check(times.getHours());
        var m = check(times.getMinutes());
        var s = check(times.getSeconds());
        $("#server_time").text(yy+"-"+mm+"-"+dd+" "+h+":"+m+":"+s);
    }, 1000);


});

function check(x) {
    if (x < 10) {
        x = '0' + x;
    }
    return x;
}

function getTime() {
    alert("asd");
    document.getElementById('server_time').innerHTML = yy + "-" + mm + "-" + dd + " " + h + ":" + m + ":" + s;
    
}
