const API_BASE_URL = window.location.origin.includes("127.0.0.1:8000") || window.location.origin.includes("localhost:8000") 
    ? "" 
    : "http://127.0.0.1:8000";

// =====================================
// LOAD PROFILE FUNCTION
// =====================================
async function loadProfile() {
    const roll_number = localStorage.getItem("roll_number");
    
    if (!roll_number) {
        alert("Please log in first!");
        window.location.href = "login.html";
        return;
    }

    try {
        const response = await fetch(API_BASE_URL + `/profile/${roll_number}`);
        const data = await response.json();

        if (response.ok && data.message !== "Profile not found") {
            // Update display fields in profile.html if they exist
            if (document.getElementById("display-name")) {
                document.getElementById("display-name").innerText = data.name || "N/A";
                document.getElementById("display-roll").innerText = roll_number;
                document.getElementById("display-email").innerText = data.email || "N/A";
            }
            
            // Populate inputs
            document.getElementById("leetcode").value = data.leetcode_username || "";
            document.getElementById("codeforces").value = data.codeforces_username || "";
            document.getElementById("hackerrank").value = data.hackerrank_username || "";
            document.getElementById("github").value = data.github_username || "";
        } else {
            // If it is complete_profile page, just leave blank. 
            // In profile.html, set roll number and placeholder details.
            if (document.getElementById("display-roll")) {
                document.getElementById("display-roll").innerText = roll_number;
                document.getElementById("display-name").innerText = "Not Set";
                document.getElementById("display-email").innerText = "Not Set";
            }
        }
    } catch (error) {
        console.error("Error loading profile:", error);
    }
}

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
        API_BASE_URL + "/completeprofile",
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
        window.location.href = "dashboard.html";
    }
}
