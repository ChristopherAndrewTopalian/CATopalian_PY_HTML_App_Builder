// whenLoaded.js

function whenLoaded()
{
    makeClock();

    window.onload = function()
    {
        whenWindowResized();
    };

    window.onresize = function()
    {
        whenWindowResized();
    };

    //-//

    if (ge('clock'))
    {
        ge('clock').innerHTML = new Date().toLocaleTimeString('en-US');
    }
}

//----//

// Dedicated to God the Father
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
// https://github.com/ChristopherTopalian
// https://github.com/ChristopherAndrewTopalian
// https://sites.google.com/view/CollegeOfScripting

