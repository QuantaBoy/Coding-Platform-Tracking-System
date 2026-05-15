// =====================================
// REGISTER FUNCTION
// =====================================
async function registerUser() {

    // Get name from input field
    const name = document.getElementById("name").value


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

    // Get email value
    const email = document.getElementById("email").value


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

                email,
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
        
        // Save the user's user_id for the complete profile page
        localStorage.setItem("user_id", data.user_id)

        alert("Login Working Successfully")
        window.location.href = "complete_profile.html"
    }
}