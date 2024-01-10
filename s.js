document.getElementById('likeButton').addEventListener('click', function () {
    downloadImages(true);
});

document.getElementById('dislikeButton').addEventListener('click', function () {
    downloadImages(false);
});

function downloadImages(isLike) {
    const imageDivs = document.querySelectorAll('.Expand .keen-slider__slide [role="img"]');

    const imageUrls = Array.from(imageDivs).map(div => {
        const backgroundImage = div.style.backgroundImage;
        if (backgroundImage) {
            return backgroundImage.slice(5, -2).replace(/"/g, "");
        }
        return null;
    }).filter(url => url && url.startsWith('https://images-ssl.gotinder.com/'));

    // Send the data to our API
    fetch('http://127.0.0.1:5000/download_images', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image_urls: imageUrls, isLike: isLike }) 
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}


