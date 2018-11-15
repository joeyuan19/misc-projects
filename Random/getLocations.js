var getLocations = function() {
    var locs = [];
    $('.gmnoprint').each(function() {
        locs.push($(this).attr('title'));
    });
    var locs2 = [];
    for (var i = 0; i < locs.length; i++) {
        if (typeof locs[i] !== "undefined" && startswith(locs[i],"Position")) {
            locs2.push(locs[i])
        }
    }
    var s = "[";
    var i = 0;
    while (i < locs2.length) {
        s += locs2 + ",";
        i += 100;
    }
    return s + "]";
}
