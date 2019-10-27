/* function saveTextAsFile() {
  var textToWrite = document.getElementById('textArea').value;
  var textFileAsBlob = new Blob([ textToWrite ], { type: 'text/plain' });
  var fileNameToSaveAs = "dna_string.txt";

  var downloadLink = document.createElement("a");
  downloadLink.download = fileNameToSaveAs;
  downloadLink.innerHTML = "Download File";
  if (window.webkitURL != null) {
    // Chrome allows the link to be clicked without actually adding it to the DOM.
    downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
  } else {
    // Firefox requires the link to be added to the DOM before it can be clicked.
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
  }

  downloadLink.click();
}



var button = document.getElementById('save');
button.addEventListener('click', saveTextAsFile);

function destroyClickedElement(event) {
  // remove the link from the DOM
  document.body.removeChild(event.target);
}

*/

var A = "00";
var T = "01";
var G = "10";
var C = "11";
var userInput = document.getElementById('textArea').value;

/**
 * Function that converts a string into its binary representation
 * 
 * @see https://gist.github.com/eyecatchup/6742657
 * @author https://github.com/eyecatchup
 */
function stringToBinary(str, spaceSeparatedOctets) {
    function zeroPad(num) {
        return "00000000".slice(String(num).length) + num;
    }

    return str.replace(/[\s\S]/g, function(str) {
        str = zeroPad(str.charCodeAt().toString(2));
        return !1 == spaceSeparatedOctets ? str : str + " "
    });
};

var result = stringtoBinary(userInput);
document.getElementById('result').innerHTML = result;