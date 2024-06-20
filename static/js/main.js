let imgs = document.querySelectorAll('.image-wrapper .card-img-top');

imgs.forEach((img) => {
    img.addEventListener('click', (e) => {
        let imgSource = img.getAttribute('src');
        console.log(imgSource);

        let openImageWrapper = document.querySelector('.open-image-wrapper');
        let openImage = openImageWrapper.querySelector('img');

        if (openImageWrapper && openImage) {
            openImage.setAttribute('src', imgSource);
            openImageWrapper.style.display = 'flex';
        }
    });
});

document.querySelector('.open-image-wrapper').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) {
        e.currentTarget.style.display = 'none';
    }
});

document.querySelector('.close-icon').addEventListener('click', (e) => {
    document.querySelector('.open-image-wrapper').style.display = 'none';
});

const uploadContainer = document.getElementById('uploadContainer');

uploadContainer.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadContainer.classList.add('dragover');
});

uploadContainer.addEventListener('dragleave', () => {
    uploadContainer.classList.remove('dragover');
});

function deleteImage(imageName) {
    if (confirm("Are you sure you want to delete this image?")) {
        window.location.href = "/delete/" + imageName;
    }
}