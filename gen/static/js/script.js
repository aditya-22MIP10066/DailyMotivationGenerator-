// Ensuring the DOM is fully loaded before running the script.
document.addEventListener('DOMContentLoaded', () => {
    // Getting references to the necessary DOM elements.
    const generateBtn = document.getElementById('generate-btn');
    const moodSelect = document.getElementById('mood-select');  
    const motivationText = document.getElementById('motivation-text'); 

    // Adding an event listener to the generate button for click events.
    generateBtn.addEventListener('click', async () => {
        // Getting the currently selected value from the mood dropdown.
        const selectedMood = moodSelect.value;

        // Displaying a loading message while waiting for the API response.
        motivationText.textContent = "Generating motivation...";

        try {
            // POST request to Flask backend's /generate_motivation endpoint.
            const response = await fetch('/generate_motivation', {
                method: 'POST', // Specifying the HTTP method as POST.
                headers: {
                    'Content-Type': 'application/json', // Indicate that the body is JSON.
                },
                // Sending the selected mood/situation as a JSON string in the request body.
                body: JSON.stringify({ mood: selectedMood }),
            });

            // Parsing the JSON response from the backend.
            const data = await response.json();

            // if the HTTP response was successful (status code 200-299).
            if (response.ok) {
                // displaying the generated motivation text.
                motivationText.textContent = data.motivation;
            } else {
                // If there was an error (e.g., 400, 500), display the error message from the backend.
                motivationText.textContent = `Error: ${data.error || 'Something went wrong on the server.'}`;
            }
        } catch (error) {
            // Catching any network errors or issues with the fetch request itself.
            console.error('Error fetching motivation:', error);
            motivationText.textContent = "Failed to connect to the server. Please check internet connection.";
        }
    });
});
