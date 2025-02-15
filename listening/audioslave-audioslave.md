<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .hover-container {
      position: relative;
      display: inline-block;
    }

    .hover-container img {
      width: 200px;
      height: 200px;
    }

    .hover-text {
      visibility: hidden;
      width: 220px;
      background-color: black;
      color: white;
      text-align: center;
      border-radius: 6px;
      padding: 8px 0;
      position: absolute;
      z-index: 1;
      bottom: 125%; /* Position the tooltip above the image */
      left: 50%;
      margin-left: -110px; /* Center the tooltip */
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