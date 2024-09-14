function addTown() {
    let town = document.getElementById('town').value
    let visit_date = document.getElementById('visit_date').value
    fetch('/town', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'town': town || 'Пустое',
                             'visit_date': visit_date || '11.04.24'})
    })
}

window.onload = ( () => {
    document.getElementById('visit_date').valueAsDate = new Date()
})