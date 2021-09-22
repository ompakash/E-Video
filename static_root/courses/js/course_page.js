var player;
document.onreadystatechange = function () {
    if (document.readyState == 'interactive') {
        player = document.getElementById("player")
        maintainRatio()
    }
}
function maintainRatio() {
    var w = player.clientWidth
    var h = (w * 9) / 16
    
    player.height = h
}
window.onresize = maintainRatio
