document.querySelectorAll('.tooltip').forEach(elem => {
    const word = elem.getAttribute('data-word');

    // Open dictionary URL in a new tab on click
    elem.addEventListener('click', () => {
        const dictionaryUrl = `https://hanyu.baidu.com/s?wd=${encodeURIComponent(word)}`;
        window.open(dictionaryUrl, '_blank');
    });
});
