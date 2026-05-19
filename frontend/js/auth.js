// =====================================
// REGISTER FUNCTION
// =====================================
async function registerUser() {

    // Get name from input field
    const name = document.getElementById("name").value

    // Get roll number
    const roll_number = document.getElementById("roll_number").value

    // Get email
    const email = document.getElementById("email").value


    // Get password
    const password = document.getElementById("password").value


    // Send request to backend
    const response = await fetch(

        // FastAPI register endpoint
        "http://127.0.0.1:8000/register",

        {

            // HTTP request type
            method: "POST",


            // Request headers
            headers: {

                "Content-Type": "application/json"
            },


            // Convert JS object → JSON string
            body: JSON.stringify({
                roll_number,
                name,
                email,
                password
            })
        }
    )


    // Convert response into JSON
    const data = await response.json()


    // Show backend response
    alert(data.message)


    // Redirect after successful registration
    if (data.message === "User Registered Sucessfully") {

        window.location.href = "login.html"
    }
}



// =====================================
// LOGIN FUNCTION
// =====================================
async function loginUser() {

    // Get roll number value
    const roll_number = document.getElementById("roll_number").value


    // Get password value
    const password = document.getElementById("password").value


    // Send login request
    const response = await fetch(

        "http://127.0.0.1:8000/login",

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json"
            },


            // Convert object into JSON
            body: JSON.stringify({
                roll_number,
                password
            })
        }
    )


    // Convert response into JSON
    const data = await response.json()


    // Show backend message
    alert(data.message)


    // Temporary login success action
    if (data.message === "Login Successful") {
        
        // Save the user's roll_number for the complete profile page
        localStorage.setItem("roll_number", data.roll_number)

        alert("Login Working Successfully")
        window.location.href = "complete_profile.html"
    }
}