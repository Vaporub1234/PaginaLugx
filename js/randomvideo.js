const videos = [
    "assets/videos/COD.mp4",
    "assets/videos/Wartales.mp4",
    "assets/videos/NewArc.mp4"   
];


const randomVideo = videos[Math.floor(Math.random() * videos.length)];

const videoElement = document.getElementById('random-video');
videoElement.src = randomVideo;
