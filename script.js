function accordionSidebar(element) {
    const content = document.getElementById(element.id + '-content');

    if (element.checked) {
        content.style.height = content.scrollHeight + 'px'; // Define a altura para a altura total do conteúdo
        content.classList.remove('collapsed');
        content.classList.add('expanded');
    } else {
        // Primeiro, defina a altura atual para permitir a animação
        content.style.height = content.scrollHeight + 'px'; // Define a altura atual

        // Em seguida, ajuste a altura para 0 após um pequeno timeout
        setTimeout(() => {
            content.style.height = '0'; // Fecha o conteúdo
        }, 0);

        // Remova a classe expanded após a animação
        setTimeout(() => {
            content.classList.remove('expanded');
            content.classList.add('collapsed');
        }, 300); // Tempo deve coincidir com a duração da transição CSS
    }
}
