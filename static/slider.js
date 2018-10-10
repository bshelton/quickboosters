
var slideCol = document.getElementById("id1");
var slideSq = document.getElementById("id2");
var slidePic = document.getElementById("id3");
var y = document.getElementById("f");
var x = document.getElementById("u");
var z = document.getElementById("z");
y.innerHTML = slideCol.value;

slideCol.oninput = function() {
    y.innerHTML = this.value;
}

slideSq.oninput = function() {
    x.innerHTML = this.value;
}

slidePic.oninput = function() {
    z.innerHTML = this.value;
}
