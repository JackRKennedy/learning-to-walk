async function getInspiration() {
    let quote_id = Math.floor(Math.random()*1000);

    //const quoteAPI = `https://favqs.com/api/quotes/:${quote_id}`;
    const quoteOfTheDayAPI = await 'https://favqs.com/api/qotd';
    fetch(quoteOfTheDayAPI)
        .then(response => { 
            if (response.ok) {
                return response.json();
            }
        })
        .then (data => {
            const body = JSON.stringify(data.quote.body);
            const author = JSON.stringify(data.quote.author);
            console.log(`\n\nA little inspiration for you: \n\n${body} - ${author}\n\n`);
        })

        .catch(error => {
            console.error(error);
        })
    }; 

module.exports = getInspiration;