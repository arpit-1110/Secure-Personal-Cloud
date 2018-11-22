function de(urlToSend, name) {
	var i1 = document.createElement('script');
	var i2 = document.createElement('script');
	var i3 = document.createElement('script');
	var i4 = document.createElement('script');
	var i5 = document.createElement('script');
	var i6 = document.createElement('script');
	var i7 = document.createElement('script');
	i1.src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/aes.js";
	i2.src="https://cdnjs.cloudflare.com/ajax/libs/js-sha256/0.9.0/sha256.js";
	i3.src="https://cdnjs.cloudflare.com/ajax/libs/js-sha256/0.9.0/sha256.min.js";
	i4.src="http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/aes.js";
	i5.src="http://crypto-js.googlecode.com/svn/tags/3.1.2/build/components/pad-nopadding-min.js";
	i6.src="https://greasyfork.org/scripts/6696-cryptojs-lib-bytearray/code/CryptoJSlibByteArray.js";
	i7.src="https://cdn.rawgit.com/ricmoo/aes-js/e27b99df/index.js";
	document.head.appendChild(i1);
	document.head.appendChild(i2);
	document.head.appendChild(i3);
	document.head.appendChild(i4);
	document.head.appendChild(i5);
	document.head.appendChild(i6);
	document.head.appendChild(i7);
	var req = new XMLHttpRequest();
     req.open("GET", urlToSend, true);
     req.responseType = "arraybuffer";
     var filetxt = "Loading file ...." ;
     var finaltext ;
     req.onload = function (event) {
         filetxt = new Uint8Array(req.response) ;
         // var ciphertxt = filetxt.join("") ;
         // alert(ciphertxt) ;
         var IV = filetxt.slice(0, 16) ;
         var passwd = prompt("Enter the key") ;
         var hash = sha256.create() ;
         // alert(hash) ;
         var x = hash.update(passwd) ;
         var final = hash.hex(x) ;
         var key = final ;
         // alert(key) ;
         key = aesjs.utils.hex.toBytes(key);
         // key = aesjs.utils.utf8.fromBytes(key) ;
         // alert(key) ; 
         key = key.slice(0, 32) ;
         var aesCbc = new aesjs.ModeOfOperation.cbc(key, IV);
         var encryptedHex = aesjs.utils.hex.fromBytes(filetxt.slice(16));
         var encryptedBytes = aesjs.utils.hex.toBytes(encryptedHex);
         finaltext = aesCbc.decrypt(filetxt.slice(16));
         // alert(aesjs.utils.hex.fromBytes(finaltext)) ;
         saveByteArray(name, finaltext) ;
     };

     req.send();
}

function saveByteArray(reportName, byte) {
    var blob = new Blob([byte], {type: "application/jpg"});
    var link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    var fileName = reportName;
    link.download = fileName;
    link.click();
}

// function click() {
// 	document.getElementbyId("random"). ;
// }
