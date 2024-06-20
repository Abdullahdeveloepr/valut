function previewImage() {
    const fileInput = document.getElementById('file');
    const previewContainer = document.getElementById('previewContainer');

    // Clear previous preview
    while (previewContainer.firstChild) {
        previewContainer.removeChild(previewContainer.firstChild);
    }

    const files = fileInput.files;

    // Check if files were selected
    if (files.length === 0) {
        return;
    }

    // Check if the first file is an image
    const imageType = /^image\//;
    if (!imageType.test(files[0].type)) {
        return;
    }

    // Create an image element for preview
    const img = document.createElement('img');
    img.classList.add('preview-img');
    img.file = files[0];

    // Set up FileReader to read the selected file
    const reader = new FileReader();
    reader.onload = function(e) {
        img.src = e.target.result; // Set src attribute with data URL
    };
    reader.readAsDataURL(files[0]); // Read the selected file as a data URL

    // Append the preview image to the preview container
    previewContainer.appendChild(img);
}

// Drag and drop functionality
function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    const fileInput = document.getElementById('file');
    fileInput.files = event.dataTransfer.files;
    previewImage();
}

function handleDragOver(event) {
    event.preventDefault();
}

