// =====================================
// SUBMIT PROFILE FUNCTION
// =====================================
async function submitProfile() {

    // Get usernames from input fields
    const leetcode_username = document.getElementById("leetcode").value;
    const codeforces_username = document.getElementById("codeforces").value;
    const hackerrank_username = document.getElementById("hackerrank").value;
    const github_username = document.getElementById("github").value;

    // Retrieve the user_id saved during login
    const user_id_string = localStorage.getItem("user_id");

    // If there is no user_id, something went wrong (e.g., they didn't log in properly)
    if (!user_id_string) {
        alert("Please log in first!");
        window.location.href = "login.html";
        return;
    }

    // Convert user_id to an integer because the backend schema expects an int
    const user_id = parseInt(user_id_string);

    // Send request to backend
    const response = await fetch(
        "http://127.0.0.1:8000/completeprofile",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                user_id,
                leetcode_username,
                codeforces_username,
                hackerrank_username,
                github_username
            })
        }
    );

    // Convert response into JSON
    const data = await response.json();

    // Show backend response
    alert(data.message);

    // Optional: Redirect to a dashboard page if you create one later!
    if (data.message === "Profile Completed Successfully") {
        console.log("Profile has been saved!");
        // window.location.href = "dashboard.html";
    }
}
