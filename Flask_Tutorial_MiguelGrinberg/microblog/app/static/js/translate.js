async function translate(sourceElem, destElem, sourceLang, destLang){
    document.getElementById(destElem).innerHTML =
     '<img src="/static/loading.gif alt="Loading...">';
    
    const response = await fetch('/translate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json; charset=utf-8'},
        body: JSON.stringify({
            text: document.getElementById(sourceElem).innerText,
            source_language: sourceLang,
            dest_language: destLang
        })
    });

    const data = await response.json();
    document.getElementById(destElem).innerText = data.text;
    
    }