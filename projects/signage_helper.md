<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.3/dist/tailwind.min.css" />
    <title>Signage Letter Helper</title>
    <style>
        .dark-mode .bg-white {
            background-color: #1a1a1a;
        }

        .dark-mode .text-gray-700 {
            color: #f8f8f8;
        }

        .dark-mode .border {
            border-color: #333333;
        }

        .dark-mode .bg-blue-500 {
            background-color: #4a90e2;
        }

        .dark-mode .text-white {
            color: #f8f8f8;
        }
    </style>
</head>
<body class="bg-white relative dark-mode">
    <div class="flex flex-col items-center justify-center min-h-screen">
        <div class="w-full max-w-md p-4 bg-white rounded shadow-md">
            <h3 class="text-2xl font-semibold mb-4">Signage Letter Helper</h3>
            <form id="signage-form">
                <div class="mb-4">
                    <label for="old_message" class="block text-gray-700">Old Signage Message:</label>
                    <input type="text" id="old_message" name="old_message" class="w-full px-3 py-2 border rounded" required>
                    <button id="dark-mode-toggle" class="ml-4 p-2 text-black rounded shadow-md">🌓</button>
                </div>
                <div class="mb-4">
                    <label for="new_message" class="block text-gray-700">New Signage Message:</label>
                    <input type="text" id="new_message" name="new_message" class="w-full px-3 py-2 border rounded" required>
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded">Get Needed Letters</button>
            </form>
            <div id="results" class="mt-4"></div>
        </div>
    </div>

    <script>
        document.getElementById('signage-form').addEventListener('submit', function(event) {
            event.preventDefault();

            const oldMessage = document.getElementById('old_message').value;
            const newMessage = document.getElementById('new_message').value;

            const neededLetters = getNeededLetters(oldMessage, newMessage);

            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<h4 class="text-xl font-semibold mb-2">Letters needed to update the signage:</h4>';
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

        // Dark mode toggle
            const darkModeToggle = document.getElementById('dark-mode-toggle');
            document.body.appendChild(darkModeToggle);

            darkModeToggle.addEventListener('click', () => {
                document.body.classList.toggle('dark-mode');
                const isDarkModeOn = document.body.classList.contains('dark-mode');
                darkModeToggle.innerText = isDarkModeOn ? '☀️' : '🌑';
            });
        });
    </script>
</body>
</html>