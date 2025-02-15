<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .hover-container {
      position: relative;
      display: inline-block;
      width: 200px; /* Match the width of the image */
      height: 200px; /* Match the height of the image */
    }

    .hover-container img {
      width: 100%; /* Ensure the image fills the container */
      height: 100%; /* Ensure the image fills the container */
    }

    .hover-text {
      visibility: hidden;
      width: 100%; /* Match the width of the container */
      background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
      color: white;
      text-align: center;
      border-radius: 6px;
      padding: 8px 0;
      position: absolute;
      z-index: 1;
      bottom: 0; /* Position the tooltip at the bottom of the image */
      left: 0;
      opacity: 0;
      transition: opacity 0.3s;
    }

    .hover-container:hover .hover-text {
      visibility: visible;
      opacity: 1;
    }
  </style>
</head>
<body>
  <div class="hover-container">
    <a href="https://open.spotify.com/album/78guAsers0klWl6RwzgDLd?si=p9FT--SZQEGQFjqe_j53iA">
      <img src="https://upload.wikimedia.org/wikipedia/en/a/ac/Audioslave_-_Audioslave.jpg" alt="Audioslave - Audioslave">
    </a>
    <div class="hover-text">Audioslave - Audioslave</div>
  </div>
</body>
</html>