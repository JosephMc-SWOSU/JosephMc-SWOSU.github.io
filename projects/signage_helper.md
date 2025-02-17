# Signage Letter Helper

## Instructions
Enter the old signage message and the new signage message to determine which letters you need to bring to update the signage.

## Form
<form id="signage-form">
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

<script>
    document.getElementById('signage-form').addEventListener('submit', function(event) {
        event.preventDefault();

        const oldMessage = document.getElementById('old_message').value;
        const newMessage = document.getElementById('new_message').value;

        const neededLetters = getNeededLetters(oldMessage, newMessage);

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

        const oldCounter = {};
        const newCounter = {};

        for (const char of oldMessage) {
            oldCounter[char] = (oldCounter[char] || 0) + 1;
        }

        for (const char of newMessage) {
            newCounter[char] = (newCounter[char] || 0) + 1;
        }

        const neededLetters = {};
        for (const [char, count] of Object.entries(newCounter)) {
            if (count > (oldCounter[char] || 0)) {
                neededLetters[char] = count - (oldCounter[char] || 0);
            }
        }

        return neededLetters;
    }
</script>