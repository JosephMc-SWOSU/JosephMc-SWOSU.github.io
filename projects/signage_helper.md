# Signage Letter Helper

## Instructions
Enter the old signage message and the new signage message to determine which letters you need to bring to update the signage.

## Form
<form id="signage-form" onsubmit="return false;">
    <div>
        <label for="old_message">Old Signage Message:</label>
        <input type="text" id="old_message" name="old_message" required>
    </div>
    <div>
        <label for="new_message">New Signage Message:</label>
        <input type="text" id="new_message" name="new_message" required>
    </div>
    <button type="submit">Get Needed Letters</button>
</form>

<div id="results"></div>

<style>
    body.dark-mode {
        background-color: #1a1a1a;
        color: #f8f8f8;
    }

    body.dark-mode input {
        background-color: #333333;
        color: #f8f8f8;
        border: 1px solid #555555;
    }

    body.dark-mode label {
        color: #f8f8f8;
    }

    body.dark-mode button {
        background-color: #4a90e2;
        color: #f8f8f8;
    }

    body.dark-mode #results h4 {
        color: #f8f8f8;
    }
</style>

<script>
    console.log('Script loaded'); // Initial log to verify script execution

    document.addEventListener('DOMContentLoaded', function() {
        console.log('DOM fully loaded and parsed');
        const form = document.getElementById('signage-form');
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            console.log('Form submitted');

            const oldMessage = document.getElementById('old_message').value;
            const newMessage = document.getElementById('new_message').value;

            console.log('Old Message:', oldMessage);
            console.log('New Message:', newMessage);

            const neededLetters = getNeededLetters(oldMessage, newMessage);

            console.log('Needed Letters:', neededLetters);

            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<h4>Letters needed to update the signage:</h4>';
            const ul = document.createElement('ul');
            for (const [letter, count] of Object.entries(neededLetters)) {
                const li = document.createElement('li');
                li.textContent = `${letter}: ${count}`;
                ul.appendChild(li);
            }
            resultsDiv.appendChild(ul);
        });

        function getNeededLetters(oldMessage, newMessage) {
            oldMessage = oldMessage.replace(/\s+/g, '').toLowerCase();
            newMessage = newMessage.replace(/\s+/g, '').toLowerCase();

            console.log('Processed Old Message:', oldMessage);
            console.log('Processed New Message:', newMessage);

            const oldCounter = {};
            const newCounter = {};

            for (const char of oldMessage) {
                oldCounter[char] = (oldCounter[char] || 0) + 1;
            }

            for (const char of newMessage) {
                newCounter[char] = (newCounter[char] || 0) + 1;
            }

            console.log('Old Counter:', oldCounter);
            console.log('New Counter:', newCounter);

            const neededLetters = {};
            for (const [char, count] of Object.entries(newCounter)) {
                if (count > (oldCounter[char] || 0)) {
                    neededLetters[char] = count - (oldCounter[char] || 0);
                }
            }

            console.log('Calculated Needed Letters:', neededLetters);

            return neededLetters;
        }
    });
</script>