/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault()
    let name = $("#name").val()
    let email = $("#email").val()
    let year = $("#year").val()
    let color = $("#color").val()
    let res = await axios.post("/api/get-lucky-num", {
        name, email, year, color
    })
    handleResponse(res)
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    $("#name-err").empty()
    $("#email-err").empty()
    $("#year-err").empty()
    $("#color-err").empty()
    if (resp.data.error) {
        for (let key in resp.data.error) {
            console.log(key)
            $(`#${key}-err`).append(`<p>${resp.data.error[key]}</p>`)
        }
    }
    else {
        $("#lucky-results").append(`<p>Your lucky number is ${resp.data.num.num} (${resp.data.num.fact})</p>`)
        $("#lucky-results").append(`<p>Your birth year is ${resp.data.year.year} (${resp.data.year.fact})</p>`)
    }
}


$("#lucky-form").on("submit", processForm);
