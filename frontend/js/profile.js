// =====================================
// SUBMIT PROFILE FUNCTION
// =====================================
async function submitProfile() {

    // Get usernames from input fields
    const leetcode_username = document.getElementById("leetcode").value;
    const codeforces_username = document.getElementById("codeforces").value;
    const hackerrank_username = document.getElementById("hackerrank").value;
    const github_username = document.getElementById("github").value;

    // Retrieve the roll_number saved during login
    const roll_number = localStorage.getItem("roll_number");

    // If there is no roll_number, something went wrong (e.g., they didn't log in properly)
    if (!roll_number) {
        alert("Please log in first!");
        window.location.href = "login.html";
        return;
    }

    // Send request to backend
    const response = await fetch(
        "http://127.0.0.1:8000/completeprofile",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                roll_number,
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
