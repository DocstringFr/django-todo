// ancien code de compatibilité, aujourd’hui inutile
if (window.XMLHttpRequest) { // Mozilla, Safari, IE7+...
    httpRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) { // IE 6 et antérieurs
    httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
}

const todos = document.querySelectorAll('.todo');

todos.forEach(item => {
    item.addEventListener('click', event => {
        let csrfTokenValue = item.parentNode.querySelector('[name=csrfmiddlewaretoken]').value;

        let headers = new Headers();
        headers.append('X-CSRFToken', csrfTokenValue);

        const request = new Request(`/update/${item.dataset.pk}/`, {method: 'POST', headers: headers});
        fetch(request).then(response => {
            if (response.status === 200) {
                item.classList.toggle("done");
            }
        })

    })
})
