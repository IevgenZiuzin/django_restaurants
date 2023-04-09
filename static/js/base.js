window.onload = () =>{
    let searchInput = document.getElementById('searchinput')
    searchInput.addEventListener('input', async evt => {
        let data = {
            value: searchInput.value
        }
        await fetch("/search/", {
                method: 'POST',
                headers: {
                "X-CSRFToken": getCookie("csrftoken")},
                body: JSON.stringify(data)
            })
            .then(response => {
                if(response.ok){
                    return response.text()
                }
                else{
                    console.log(response.statusText, `\nstatus: ${response.status}`)
                }
            })
            .then(data => {
                document.getElementById('search-results').innerHTML = data
            })
    })
}

window.onclick = () => {
    document.getElementById('search-results').innerHTML = ''
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}