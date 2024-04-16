//Restarting the landing page for this app, was previously unable to import and export modules.  

//import functions from two modules

const getInspiration = require('./getInspirationalQuote.js');
const getInsult = require('./getInsult.js');
const getKanyeQuote = require('./whatDidKanyeSay.js');

//create a function that will randomly select one of the two functions to run
function chooseFunction () {
    let random = Math.floor(Math.random()*3);

    if (random === 0) {
        getInspiration();
    } else if (random === 1) {
        getInsult();
    } else {
        getKanyeQuote();
    }
}; 

chooseFunction();