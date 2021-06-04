
function getResponse() {
    let cipher = document.getElementById("cipher").value
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            document.getElementById("bits").innerHTML = result;
        }
    };
    xhr.open("GET", "/decrypting?cipher="+cipher, true);
    xhr.send(null);
}

