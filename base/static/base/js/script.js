console.log('Hello World!');

function validate() {

    const author = document.querySelector('[name="author"]'),
        content = document.querySelector('[name="content"]'),
        image = document.querySelector('[name="image"]');

    if (!author.value || !content.value || !image.value) {
        console.log('Error'); // we need to show this error to user;
        return false;
    } else {
        console.log('Post Added!');
    }

}


