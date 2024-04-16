// Another random API - this time it is a random kanye quote

async function getKanyeQuote() {
    const kanyeURL = 'https://api.kanye.rest/';

    fetch(kanyeURL)
        .then(response => { 
            if (response.ok) {
                return response.json();
            }
        })
        .then (data => {
            const kanyeQuote = JSON.stringify(data.quote);
            console.log(`\n\nOur lord and saviour Kanye West once said: ${kanyeQuote}\n\n`);
        })

        .catch(error => {
            console.error(error);
        })
    }; 

module.exports = getKanyeQuote;