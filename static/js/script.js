document.querySelectorAll('.code-block').forEach(block => {
    const button = document.createElement('button');
    button.innerText = 'Copy';
    button.className = 'copy-button';
    block.appendChild(button);

    button.addEventListener('click', () => {
        const code = block.querySelector('code').innerText;
        navigator.clipboard.writeText(code).then(() => {
            button.innerText = 'Copied!';
            setTimeout(() => button.innerText = 'Copy', 2000);
        });
    });
});