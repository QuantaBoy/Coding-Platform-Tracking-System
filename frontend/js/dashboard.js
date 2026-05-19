const API_BASE_URL = window.location.origin.includes("127.0.0.1:8000") || window.location.origin.includes("localhost:8000") 
    ? "" 
    : "http://127.0.0.1:8000";

// =========================================
// LOAD DASHBOARD DATA
// =========================================
async function loadDashboard() {


    // =====================================
    // GET USER ID
    // =====================================
    //
    // Retrieved from browser localStorage
    //
    const roll_number = localStorage.getItem("roll_number")


    // =====================================
    // FETCH DASHBOARD DATA
    // =====================================
    const response = await fetch(

        API_BASE_URL + `/dashboard/${roll_number}`
    )


    // =====================================
    // CONVERT RESPONSE TO JSON
    // =====================================
    const data = await response.json()


    // =====================================
    // EXTRACT CODEFORCES INFO
    // =====================================
    const info = data.codeforces_info


    // =====================================
    // DISPLAY USER INFO
    // =====================================
    document.getElementById("handle").innerText =

        info.handle


    document.getElementById("rank").innerText =

        info.rank


    document.getElementById("rating").innerText =

        info.rating


    document.getElementById("maxrating").innerText =

        info.maxrating



    // =====================================
    // DISPLAY SUBMISSIONS
    // =====================================
    const submissionsList = document.getElementById(

        "submissions-list"
    )


    // Loop through submissions
    data.submissions.forEach(submission => {


        // Create new list item
        const li = document.createElement("li")


        // Insert submission info
        li.innerText =

            `${submission.problem_name}
             | ${submission.verdict}
             | ${submission.language}`


        // Add item into list
        submissionsList.appendChild(li)
    })
}



// =========================================
// AUTOMATICALLY LOAD DASHBOARD
// =========================================
loadDashboard()