// whenWindowResized.js

function whenWindowResized()
{
    let theElement = ge('clock');

    theElement.style.position = 'absolute';

    theElement.style.left = window.innerWidth / 2 - theElement.offsetWidth / 2 + 'px';

    theElement.style.top = window.innerHeight / 2 - theElement.offsetHeight / 2 + 'px';
}

//----//

// Dedicated to God the Father
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
// https://github.com/ChristopherTopalian
// https://github.com/ChristopherAndrewTopalian
// https://sites.google.com/view/CollegeOfScripting

