//testing console out and functions in vanilla js
insultURL = 'https://evilinsult.com/generate_insult.php?lang=en&type=json';

async function getInsult() {
    const response = await fetch(insultURL);
    const data = await response.json();
    
    console.log(`\n\nHere's an insult you could use sometime: \n\n${data.insult}\n\n`);
};

module.exports = getInsult;